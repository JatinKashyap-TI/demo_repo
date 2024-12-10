from odoo import models , fields , api 
from odoo.exceptions import ValidationError

class Invconf(models.TransientModel):
    _name="inv.conf"

    prod=fields.Char(readonly=True)
    emp=fields.Char(readonly=True)

    @api.model
    def default_get(self,fields):
        res=super(Invconf,self).default_get(fields)
        if self.env.context.get('default_prod') and self.env.context.get('default_emp'):
            employee=self.env['hr.employee'].browse(self.env.context.get('default_emp'));
            res.update(
                {
                    'prod':self.env.context.get('default_prod'),
                    'emp':employee.name
                }
            )
        return res
    def confirm_inventory(self):
        latest_record=self.env['product.product'].browse(self.env.context.get('active_id'))
        latest_record.unlink()
        self.env['product.product'].create(
            {
                'name':self.env.context.get('default_prod'),
                'emp':self.env.context.get('default_emp')
            }
        )
        return ({
            "type":"ir.actions.act_window_close"
        })  
    def cancel_inventory(self):
        latest_record=self.env['product.product'].browse(self.env.context.get('active_id'))
        latest_record.unlink()
        return ({
            "type":"ir.actions.act_window_close"
        })