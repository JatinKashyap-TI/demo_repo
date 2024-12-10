from odoo import models, fields
import logging
class ResCompany(models.Model):
    _inherit = 'res.company'
    pan_card_required = fields.Boolean(string="PAN Card Required", company_dependent=True)
    passport_number_required = fields.Boolean(string="Passport Number Required", company_dependent=True)