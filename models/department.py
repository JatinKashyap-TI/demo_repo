from odoo import models,fields
import logging
_logger=logging.getLogger(__name__)
class Department(models.Model):
    _inherit="hr.department"
    employees=fields.Many2many('hr.employee',string="Employees",can_create=False)

   

    def fun_one(self):
        # Create a new context and add a value
        new_context = dict(self.env.context)
        new_context["hello"] = "hello world"  # Add new context key-value

        _logger.info(f"############################################ {self.env.context.get('hello')}")  # Log the original context
        _logger.info(f"############################################ {new_context.get('hello')}")  # Log the new context

        # Call fun_two with the modified context using with_context
        return self.with_context(new_context).fun_two()  # Pass new context with with_context

    def fun_two(self):
        # Access the context set in fun_one
        new_context = dict(self.env.context)
        _logger.info(f"############################################ {new_context.get('hello')}")  # Access the passed context

        # Add 'hi' to the context and pass it to final_context
        return self.with_context(hi='hi').final_context()  # Adding 'hi' to the context using with_context

    def final_context(self):
        # Access the context set in fun_two
        new_context = dict(self.env.context)

        # Log context value for 'hi' and 'hello'
        _logger.info(f"############################################ {new_context.get('hi')}")  # This should now return 'hi'
        _logger.info(f"############################################ {new_context.get('hello')}")  # Log the 'hello' context from fun_one
        _logger.info(f"############################################ {new_context}")  # Log the entire current context

        # Modify context: remove 'hi' if it exists
        if 'hi' in new_context:
            del new_context['hi']

        _logger.info(f"############################################ {new_context}")  # Log modified context after removing 'hi'
