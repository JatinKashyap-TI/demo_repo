from odoo import models , fields , api
class Referal(models.Model):
    _inherit="utm.campaign"

    tag_ids=fields.Many2many('hr.department')
    role=fields.Char(string="Role", placeholder="e.g. backend development ")