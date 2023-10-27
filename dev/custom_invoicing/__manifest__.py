{
    'name': 'Custom Invoicing Module',
    'version': '1.0',
    'summary': 'Enhance the invoicing process in Odoo',
    'description': 'A custom module for creating and managing invoices.',
    'category': 'Sales/Invoicing',
    'author': 'Shagun',
    'depends': ['base', 'account'],
    'data': [
        'views/custom_invoice_view.xml',
        'views/custom_invoice_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
