# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ledger_filter"
app_title = "Ledger Filter"
app_publisher = "erpnext"
app_description = "Filter ledger by creation time"
app_icon = "octicon octicon-settings"
app_color = "green"
app_email = "email@ledger.info"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ledger_filter/css/ledger_filter.css"
# app_include_js = "/assets/ledger_filter/js/ledger_filter.js"

# include js, css files in header of web template
# web_include_css = "/assets/ledger_filter/css/ledger_filter.css"
# web_include_js = "/assets/ledger_filter/js/ledger_filter.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ledger_filter.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ledger_filter.install.before_install"
# after_install = "ledger_filter.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ledger_filter.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ledger_filter.tasks.all"
# 	],
# 	"daily": [
# 		"ledger_filter.tasks.daily"
# 	],
# 	"hourly": [
# 		"ledger_filter.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ledger_filter.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ledger_filter.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ledger_filter.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ledger_filter.event.get_events"
# }

