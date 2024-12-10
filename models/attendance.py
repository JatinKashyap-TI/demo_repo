from odoo import models , fields ,api
from datetime import datetime , timedelta
class Attendance(models.Model):
    _inherit="hr.attendance"

    chk_in=fields.Selection([('waiting',"waiting"),('in',"Ckeck in")] ,string="Check_in" )
    chk_out=fields.Selection([('waiting',"waiting"),('out',"Ckeck out")], string="check_out" )


    # @api.depends('chk_in')
    # def _compute_chkin(self):
    #     for record in self:
    #         if record.chk_in == 'in':
    #             record.check_in=datetime.now()

                
    # @api.depends('chk_out')
    # def _compute_chkout(self):
    #     for record in self:
    #         if record.chk_out == 'out':
    #             record.check_out=datetime.now()

    @api.model
    def create(self,vals):
        if vals['chk_in']=='in':
            vals['check_in']=datetime.now()
        return super(Attendance,self).create(vals)
    
    def write(self,vals):
        if vals['chk_out']=='out':
            vals['check_out']=datetime.now()
        return super(Attendance,self).write(vals)