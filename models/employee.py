from odoo import models,fields,api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class Employees(models.Model):
    _inherit="hr.employee"
    attend=fields.Char()
    salary = fields.Float(string='Salary')
    expected_appraisal = fields.Float(string='Expected Appraisal')

    def action_print_report(self): 
        for record in self:
            return self.env.ref("office_management.template_report").report_action(record)
        

    @api.model
    def create(self,vals):
        max_emp=int(self.env['ir.config_parameter'].sudo().get_param('office_management.max_employee_limit'))
        _logger.info(f"###################################################################{max_emp,self.env.x.name}")
        emp_count=self.search_count([]);
        if emp_count>=max_emp :
            raise ValidationError("Can not create more employees")
        return super(Employees,self).create(vals)
        
