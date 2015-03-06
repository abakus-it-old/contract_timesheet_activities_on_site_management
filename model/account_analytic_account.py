from openerp import models, fields, api

class account_analytic_account_improvements(models.Model):
    _inherit = ['account.analytic.account']
    
    on_site_product = fields.Many2one('product.product', string="On site Product", index=True)