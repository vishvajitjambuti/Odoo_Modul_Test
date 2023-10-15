from odoo import models, fields, api, _

class StarRating(models.Model):
    _name = 'star.rating'
    _description = 'Star Rating'

    user_name = fields.Char(string='User Name', required=True)
    rating = fields.Float(string='Rating', digits=(3, 2))
    rating_system = fields.Selection([('1', 'very low'), ('2', 'low'), ('3', 'Normal'), ('4', 'High'), ('5', 'Very High')], string ="rating")
    progress = fields.Integer(string="Progress", compute='_compute_progress')

    @api.depends('rating_system')
    def _compute_progress(self):
        for rec in self:
            if rec.rating_system == '1':
                progress  = 20
            elif rec.rating_system == '2':
                progress = 40
            elif rec.rating_system == '3':
                progress = 60
            elif rec.rating_system == '4':
                progress = 80
            elif rec.rating_system == '5':
                progress = 100
            else:
                progree = 0
            rec.progress = progress

