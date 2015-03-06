from openerp import models, fields, api

class account_analytic_line_improvements(models.Model):
    _inherit = ['account.analytic.line']

    on_site = fields.Boolean(string="On site", default=False)