import frappe
from frappe import _
from frappe.utils import nowdate, add_days
import requests


@frappe.whitelist()
def new_joinee_alert(doc, method):
    if doc.enabled:
        frappe.sendmail(
            recipients=['ragavendragj12@gmail.com'],
            sender=frappe.session.user,
            subject=doc.first_name,
            message="newly joined",
            reference_doctype=doc.doctype,
            reference_name=doc.name,
        )
        frappe.msgprint("Email Sent")
