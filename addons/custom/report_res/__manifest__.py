
{
    'name': 'report',
    'version': '1.0.0',
    'author': 'javis',
    'category': ' report category' ,

    'depends': ['reservation'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/report_hotel_reservation_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
