
{
    'name': 'amenity',
    'version': '1.0.0',
    'author': 'javis',
    'category': ' amentiy category' ,
    'depends': ['hotel','restaurent','food'],
    'license': 'AGPL-3',
    'demo': [
        'views/amenity_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/amenity_report.xml',
        'wizard/amenity_wizard.xml',
        'views/res_table.xml',
        'views/kot.xml',
        'views/bill.xml',
        'views/folio_order_report.xml',
        'views/amenity_sequence.xml',
        'views/amenity_view.xml',
    ],
    'installable': True
}
