# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Product Subscription',
    'category': 'Website',
    'summary': "Website Product Subsciption",

    'version': '13.0.1',
    'description': """
Website Product Subsciption
==================
This module allows to If product is out of stock in eCommerce then customer can send request(subscribe) and When product is available, admin can Send email to all the subscribe User.
        """,
    'author': 'Odoo Helper',
    'depends': ['website_sale','website_sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/assets.xml',
        'views/template.xml',
        'views/product_view.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 28.16,
    'currency': 'USD',

    'application': True,
    'installable': True,
    'auto_install': False,
}

