app_name = "zkteco_attendance"
app_title = "ZKTeco Attendance"
app_publisher = "hammad"
app_description = "ZKTeco Attendance"
app_email = "hammad@srptechs.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "zkteco_attendance",
# 		"logo": "/assets/zkteco_attendance/logo.png",
# 		"title": "ZKTeco Attendance",
# 		"route": "/zkteco_attendance",
# 		"has_permission": "zkteco_attendance.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zkteco_attendance/css/zkteco_attendance.css"
# app_include_js = "/assets/zkteco_attendance/js/zkteco_attendance.js"

# include js, css files in header of web template
# web_include_css = "/assets/zkteco_attendance/css/zkteco_attendance.css"
# web_include_js = "/assets/zkteco_attendance/js/zkteco_attendance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "zkteco_attendance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "zkteco_attendance/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "zkteco_attendance.utils.jinja_methods",
# 	"filters": "zkteco_attendance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "zkteco_attendance.install.before_install"
# after_install = "zkteco_attendance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "zkteco_attendance.uninstall.before_uninstall"
# after_uninstall = "zkteco_attendance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "zkteco_attendance.utils.before_app_install"
# after_app_install = "zkteco_attendance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "zkteco_attendance.utils.before_app_uninstall"
# after_app_uninstall = "zkteco_attendance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zkteco_attendance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------
scheduler_events = {
    "cron": {
        "*/5 * * * *": [
            "zkteco_attendance.zkteco_fetch_edit.fetch_zkteco_attendance"
        ]
    }
}
# scheduler_events = {
# 	"all": [
# 		"zkteco_attendance.tasks.all"
# 	],
# 	"daily": [
# 		"zkteco_attendance.tasks.daily"
# 	],
# 	"hourly": [
# 		"zkteco_attendance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zkteco_attendance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"zkteco_attendance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "zkteco_attendance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zkteco_attendance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zkteco_attendance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["zkteco_attendance.utils.before_request"]
# after_request = ["zkteco_attendance.utils.after_request"]

# Job Events
# ----------
# before_job = ["zkteco_attendance.utils.before_job"]
# after_job = ["zkteco_attendance.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"zkteco_attendance.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

