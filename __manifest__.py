# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 14 pour FINSEN',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 14 pour FINSEN
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale_management',
        'account',
        'purchase',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

