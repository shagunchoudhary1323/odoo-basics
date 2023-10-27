from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = 'product.management.product'
    _description = 'Product Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Char(string='Sequence',default=lambda self: ('New'))
    name = fields.Char(string='Product Name',required=True ,track_visibility="True")
    description = fields.Text(track_visibility="True",string='Description')
    price = fields.Float(string='Price',track_visibility="True", digits=(10, 2))
    category_id = fields.Many2one('product.management.category', track_visibility="True",string='Category')
    image = fields.Binary(string='Product Image', attachment=True,track_visibility="True")

    def action_product_list(self):
        print("hii,hello",self.read()[0])
        data = {'docs': self}
        d={
            "model":"product.management.product",
            'form': self.read()[0]
        }
        print("d=",d)

        return self.env['report'].get_action(self, 'product_management.report_product_list', data=data)

    def create(self, vals):
        if 'sequence' not in vals:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('product.management.product') or ('New')
            return super(Product, self).create(vals)

@api.constrains('price')
def _check_non_negative_price(self):
    for product in self:
        if product.price < 0:
            raise ValidationError("Price must be non-negative.")

