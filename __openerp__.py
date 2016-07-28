{
    'name': 'Blancoamor - Sales Customization',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','product','sale','account'],
    'data': [
	#'security/ir.model.access.csv',
	#'security/security.xml',
	'wizard/wizard_view.xml',
	'sale_view.xml',
	'ba_data.xml',
    ],
    'demo': [
    ],
    'qweb': [],
    'installable': True,
}
