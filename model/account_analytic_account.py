from openerp import models, fields, api

class account_analytic_account_improvements(models.Model):
    _inherit = ['account.analytic.account']
    
    on_site_product = fields.Many2one('product.product', string="Travel Product", index=True)
    on_site_invoice_by_km = fields.Boolean(string="Invoice by km", help="True: price = km * on site product public price, False: price = on site product public price")
    on_site_distance_in_km = fields.Float("Distance in km")