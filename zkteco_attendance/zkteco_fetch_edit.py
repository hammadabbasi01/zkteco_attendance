from zk import ZK
import frappe
from datetime import datetime


def get_device_connection(device):
    return ZK(
        device.ip_address,
        port=int(device.port or 4370),
        timeout=10,
        password=0,
        force_udp=False,
        ommit_ping=True
    )


def fetch_attendance_from_device(device):
    zk = get_device_connection(device)

    conn = zk.connect()
    conn.disable_device()

    attendance = conn.get_attendance()

    conn.enable_device()
    conn.disconnect()

    return attendance


def get_employee_by_device_id(device_id):
    return frappe.db.get_value(
        "Employee",
        {"attendance_device_id": device_id},
        "name"
    )


# def create_attendance_log(emp, timestamp, log_type="IN"):

#     # Prevent duplicate entry
#     exists = frappe.db.exists(
#         "Employee Checkin",
#         {
#             "employee": emp,
#             "time": timestamp
#         }
#     )

#     if exists:
#         return False

#     doc = frappe.new_doc("Employee Checkin")
#     doc.employee = emp
#     doc.time = timestamp
#     doc.log_type = log_type
#     doc.save(ignore_permissions=True)

#     return True



def create_attendance_log(emp, timestamp, log_type="IN"):

    exists = frappe.db.exists(
        "Employee Checkin",
        {
            "employee": emp,
            "time": timestamp
        }
    )

    if exists:
        return False

    doc = frappe.new_doc("Employee Checkin")
    doc.employee = emp
    doc.time = timestamp
    doc.log_type = log_type

    # Auto assign shift
    try:
        doc.fetch_shift()
    except:
        from erpnext.hr.doctype.employee_checkin.employee_checkin import get_employee_shift
        shift = get_employee_shift(emp, timestamp)
        if shift:
            doc.shift = shift

    doc.save(ignore_permissions=True)

    return True

@frappe.whitelist()
def fetch_zkt_attendance(device):

    device = frappe.get_doc("ZKT Device", device)

    try:
        attendance = fetch_attendance_from_device(device)

        count = 0

        for log in attendance:

            emp_id = log.user_id
            timestamp = log.timestamp

            # Get Punch Type
            punch = getattr(log, "punch", 0)

            # Convert Punch to IN / OUT
            if punch == 0:
                log_type = "IN"
            elif punch == 1:
                log_type = "OUT"
            else:
                log_type = "IN"

            emp = frappe.db.get_value(
                "Employee",
                {"attendance_device_id": emp_id},
                "name"
            )

            if emp:
                created = create_attendance_log(emp, timestamp, log_type)

                if created:
                    count += 1

        device.last_sync = frappe.utils.now()
        device.save()

        return f"{count} attendance records synced successfully"

    except Exception as e:
        frappe.log_error(str(e), "ZKT Sync Error")
        frappe.throw(str(e))


def auto_sync_all_devices():

    devices = frappe.get_all(
        "ZKT Device",
        filters={"enable_sync": 1},
        pluck="name"
    )

    for d in devices:
        try:
            fetch_zkt_attendance(d)
        except Exception as e:
            frappe.log_error(str(e), "ZKT Auto Sync Error")
