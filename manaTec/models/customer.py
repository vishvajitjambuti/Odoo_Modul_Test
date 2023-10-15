from odoo import api, fields, models

class CustomerChecklist(models.Model):
    _name = "customer.checklist"
    _description = "customer Details "
    ref = fields.Char(string='Ref')
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    active = fields.Boolean(string='Active', default=True)
    selection_1 = fields.Boolean(string="Is Selected_1")
    selection_2 = fields.Boolean(string="Is Selected_2")
    selection_3 = fields.Boolean(string="Is Selected_3")
    selection_4 = fields.Boolean(string="Is Selected_4")

    selection_progress = fields.Integer(string='Selection Progress', compute='_compute_selection')

    @api.depends('selection_1', 'selection_2', 'selection_3', 'selection_4')
    def _compute_selection(self):
        for rec in self:
            sum_select= sum([rec.selection_1, rec.selection_2, rec.selection_3, rec.selection_4])
            per = (sum_select/4) * 100
            rec.selection_progress = per

