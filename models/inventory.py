from odoo import models,fields,api
from odoo.exceptions import ValidationError
class Inventory(models.Model):
    _inherit="product.product"

    emp=fields.Many2many('hr.employee')
    detailed_type=fields.Selection([('ho','hi'),('hi','hi2'),],string="type")
    is_emp=fields.Boolean();

    @api.model
    def create(self,vals):
        if vals.get('type') == 'service':
            raise ValidationError("error")
        return super(Inventory,self).create(vals);
    def write(self, vals):
        if vals.get('type') == 'service':
            raise ValidationError("service not allowed.")
        return super(Inventory, self).write(vals)
    def action_inv_save(self):
        if not self.emp :
            raise ValidationError("Fill the form first")
        else:
            return(
                {
                    "name":"Confirm Inventory",
                    "type":"ir.actions.act_window",
                    "res_model":"inv.conf",
                    "view_mode":"form",
                    "target":"new",
                    "context":{
                     "default_prod":self.name,
                     "default_emp":self.emp.ids,
                     "active_id":self.id
                    }
                }
            )