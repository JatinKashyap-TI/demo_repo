from odoo import models, fields ,api

class new_model(models.TransientModel):
    _inherit="crm.lead2opportunity.partner"
    action = fields.Selection([
        ('create', 'Create a new customer'),
        ('exist', 'Link to an existing customer')
    ], string='Related Customer', compute='_compute_action', readonly=False, store=True, compute_sudo=False)


    @api.depends('lead_id')
    def _compute_action(self):
        for convert in self:
            if not convert.lead_id:
                convert.action = False
            else:
                partner = convert.lead_id._find_matching_partner()
                if partner:
                    convert.action = 'exist'
                elif convert.lead_id.contact_name:
                    convert.action = 'create'
                else:
                    convert.action = False

    def _convert_and_allocate(self, leads, user_ids, team_id=False):
        self.ensure_one()

        for lead in leads:
            if lead.active :
                self._convert_handle_partner(
                    lead, self.action, self.partner_id.id or lead.partner_id.id)

            lead.convert_opportunity(lead.partner_id, user_ids=False, team_id=False)

        leads_to_allocate = leads
        if not self.force_assignment:
            leads_to_allocate = leads_to_allocate.filtered(lambda lead: not lead.user_id)

        if user_ids:
            leads_to_allocate._handle_salesmen_assignment(user_ids, team_id=team_id)