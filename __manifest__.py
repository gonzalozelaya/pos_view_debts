# -*- coding: utf-8 -*-
{
    'name': "Pos_pending_invoices",

    'summary': """
        Allows to see pending invoices in POS""",

    'description': """
        Allows to see pending invoices in POS even if debts are on another company 
    """,

    'author': "OutsourceArg",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account','point_of_sale'],
    "assets": {
        "point_of_sale._assets_pos": [
            "/fix_pos/static/src/xml/pending_invoices.xml",
            "/fix_pos/static/src/xml/partner_list.xml",
            "/fix_pos/static/src/js/partner_list.js",
            "/fix_pos/static/src/js/debt_list.js",
            "/fix_pos/static/src/xml/debt_list.xml",
        ],
    },
    'data':['views/pos_config.xml']

}