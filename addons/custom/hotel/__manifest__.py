

{
    'name': 'Hotel Management',
    'version': '1.0.0',
    'author': 'javis',
        'category': ' hotel  ' ,

    
    'license': "AGPL-3",
    'demo': ['views/hotel_data.xml'],
    'data': [
            'security/hotel_security.xml',
            'security/ir.model.access.csv',
            'views/hotel_sequence.xml',
            'views/report.xml',
            'views/report_management.xml',
            'views/hotel_view.xml',
            'wizard/hotel_wizard.xml',
    ],
    'css': ['static/src/css/room_kanban.css'],
    'auto_install': False,
    'installable': True,
    'application': True
}
