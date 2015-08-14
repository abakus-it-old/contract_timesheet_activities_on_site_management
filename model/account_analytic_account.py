from openerp import models, fields, api

class account_analytic_account_improvements(models.Model):
    _inherit = ['account.analytic.account']
    
    on_site_product = fields.Many2one('product.product', string="Travel Product", index=True)
    on_site_product_price = fields.Float("Price per travel")

    @api.one
    @api.onchange('on_site_product')
    def _set_on_site_product_price(self):
        self.on_site_product_price = self.on_site_product.lst_price