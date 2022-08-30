
{
    'name': 'Housekeeping',
    'version': '1.0.0',
    'author': 'javis',
    'depends': ['hotel'],
    'license': 'AGPL-3',
    'demo': [
        'views/Husekeeping_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/Housekeeping_report.xml',
        'views/activity_detail.xml',
        'wizard/housekeeping_wizard.xml',
        'views/Housekeeping_view.xml',
    ],
    'images': ['static/description/HouseKeeping.png'],
    'installable': True,
    'auto_install': False,
}
