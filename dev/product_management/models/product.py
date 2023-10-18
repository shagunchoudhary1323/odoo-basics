from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = 'product.management.product'
    _description = 'Product Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Char(string='ID', required=True,track_visibility="True", copy=False, readonly=True,
                             index=True, default=lambda self: _('New'))
    name = fields.Char(string='Product Name',track_visibility="True", required=True)
    description = fields.Text(track_visibility="True",string='Description')
    price = fields.Float(string='Price',track_visibility="True", digits=(10, 2))
    category_id = fields.Many2one('product.management.category', track_visibility="True",string='Category')
    image = fields.Binary(string='Product Image', attachment=True,track_visibility="True")


@api.model
def create(self, vals):
    if 'id' not in vals:
        vals['id'] = self.env['ir.sequence'].next_by_code('product.management.product') or _('New')
        return super(Product, self).create(vals)

@api.constrains('price')
def _check_non_negative_price(self):
    for product in self:
        if product.price < 0:
            raise ValidationError("Price must be non-negative.")

