{
    'name': "Invoice Report Customization",
    'summary': "Tax Invoice Qweb/PDF Report",
    'author': "IT Soft Creations",
    'website': "+923015902110",
    'category': 'PDF Report',
    'version': '16.1.0.1.0',
    'depends': ['base', 'account_accountant', 'sale_management'],
    'license': 'LGPL-3',
    'data': [
        # 'security/ir.model.access.csv',
        'reports/account_move_reports_ext.xml',
        # 'reports/invoice_report.xml',

    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
