from odoo import models , fields , api 
from odoo.exceptions import ValidationError
class Payconfirm(models.TransientModel):
    _name="pay.conf"

    employee_name=fields.Char()
    amount=fields.Float()

    def default_get(self,fields):
        res=super(Payconfirm,self).default_get(fields)
        if self.env.context.get("default_amount") and self.env.context.get('default_employee'):
            employee=self.env['hr.employee'].browse(self.env.context.get("default_employee"))
            res.update(
                {
                    'employee_name':employee.name,
                    'amount':self.env.context.get('default_amount')
                }
            )
        return res;
    def confirm_payment(self):
        latest_record=self.env['account.payment'].browse(self.env.context.get('active_id'))
        latest_record.unlink()
        self.env['account.payment'].create(
            {
                'employee':self.env.context.get('default_employee'),
                'e_name':self.env['hr.employee'].browse(self.env.context.get('default_employee')).name,
                'amount':self.env.context.get('default_amount')
            }
        )
        return {'type':"ir.actions.act_window_close"}
    def cancel_payment(self):
        latest_record=self.env['account.payment'].browse(self.env.context.get('active_id'))
        latest_record.unlink()
        return {'type':"ir.actions.act_window_close"}