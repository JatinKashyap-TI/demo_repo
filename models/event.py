from odoo import models, fields

class CustomCalendarEvent(models.Model):
    _inherit = 'calendar.event'