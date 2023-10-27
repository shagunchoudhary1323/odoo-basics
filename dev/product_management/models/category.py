from odoo import models, fields, api

class ProductCategory(models.Model):
    _name = 'product.management.category'
    _description = 'Product Category'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Category Name', track_visibility="True", required=True)
    product_ids = fields.One2many('product.management.product', 'category_id', track_visibility="True", string='Products')
