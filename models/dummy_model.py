from odoo import models, fields , api 
import logging
_logger_=logging.getLogger(__name__)
class Dummy_model(models.Model):
    _name="dummy_model"

    def fun_one(self):
        new_context=dict(self.env.context)
        new_context["hello"]="hello world"
        _logger_.info(f"############################################{self.env.context.get("hello")}")

        return self.fun_two(new_context)
    
    def fun_two(self):
        _logger_.info(f"############################################{self.env.context.get("hello")}")
        return self.final_context(self.with_context(hi='hi'))
    def final_context(self):
        _logger_.info(f"############################################{self.env.context.get("hi")}")
        new_context=dict(self.env.context)
        _logger_.info(f"############################################{new_context}")
        del new_context['hi']
        _logger_.info(f"############################################{new_context}")

