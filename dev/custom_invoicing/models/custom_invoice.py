from odoo import models, fields

class CustomInvoice(models.Model):
    _name = 'custom_invoicing.invoice'
    _description = 'Custom Invoices'

    customer_id = fields.Many2one('res.partner', string='Customer')
    order_number = fields.Char(string='Order Number')
    due_date = fields.Date(string='Due Date')
    reference = fields.Char(string='Reference')
    product_line_ids = fields.Many2many('product.management.product', string='Product Lines')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    ], default='draft', string='Status')

    def action_send_invoice(self):
        self.write({'state': 'sent'})

    def action_mark_paid(self):
        self.write({'state': 'paid'})

