

{
    'name': ' Reservation ',
    'version': '1.0.0',
    'author': 'javis ',
    'category': ' reservation' ,
    'depends': ['hotel', 'stock','category', 'mail'],
    'license': 'AGPL-3',
    'demo': [
        'views/reservation_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/reservation_wizard.xml',
        'report/reservation_report.xml',
        'views/reservation_sequence.xml',
        'views/reservation_view.xml',
        'views/report_checkin.xml',
        'views/report_checkout.xml',
        'views/room_num.xml',
        
       
    ],
    'js': ['static/src/js/room_summary.js', ],
    'qweb': ['static/src/xml/room_summary.xml'],
    'css': ['static/src/css/room_summary.css'],
    'installable': True,
    'auto_install': False,
}
