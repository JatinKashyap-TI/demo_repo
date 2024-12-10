from odoo import models , fields , api 
import logging
_logger_=logging.getLogger(__name__)
class Resconf(models.TransientModel):
    _inherit="res.config.settings"
    max_employee = fields.Integer(string="Employees Limit")
    pan_card_required = fields.Boolean(string='PAN Card Required',default=False)
    passport_number_required = fields.Boolean(string='Passport Number Required',default=False)

    def get_values(self):
        res = super(Resconf , self).get_values();
        max_employee=int(self.env['ir.config_parameter'].sudo().get_param('office_management.max_employee_limit',default=25))
        pan_card_required=self.env['ir.config_parameter'].sudo().get_param('office_management.pan_card_required',default=False)
        passport_number_required=self.env['ir.config_parameter'].sudo().get_param('office_management.passport_number_required',default=False)
       
        res.update(
            max_employee=int(max_employee),
            pan_card_required=pan_card_required,
            passport_number_required=passport_number_required
        )
        company = self.env.company
        _logger_.info(f"######################################################company {company.name}#############################################################")
        
        if pan_card_required:
            company.write({
                'pan_card_required': True,
                'passport_number_required': False
            })
        elif passport_number_required:
            company.write({
                'passport_number_required': True,
                'pan_card_required': False
            })
        else:
            company.write({
                'pan_card_required': False,
                'passport_number_required': False
            })
        _logger_.info(f"######################################################pan_card_required {pan_card_required}#############################################################")
        _logger_.info(f"passport_number_required {passport_number_required}")
        return res;

    def set_values(self):
        super(Resconf,self).set_values();
        self.env['ir.config_parameter'].sudo().set_param('office_management.max_employee_limit',self.max_employee)
        self.env['ir.config_parameter'].sudo().set_param('office_management.pan_card_required',self.pan_card_required)
        self.env['ir.config_parameter'].sudo().set_param('office_management.passport_number_required',self.passport_number_required)
        # self.env['res.company'].search([]).write(
        #     {
        #         'pan_card_required':self.pan_card_required, 
        #         'passport_number_required':self.passport_number_required
        #     }
        # )