
{
    'name': 'Restauranr',
    'version': '1.0.0',
    'author': 'javis',
    'category': ' restaurants' ,
    'depends': ['hotel','category'],
    'license': 'AGPL-3',
    'category': 'room category ' ,
    'demo': ['views/manage_data.xml'],
    'data': ['security/ir.model.access.csv',
             'views/pos_restaurent_view.xml',
             'views/manage_report.xml',
            ],
    'qweb': ['static/src/xml/*.xml'],
    'auto_install': False,
    'installable': True
}
