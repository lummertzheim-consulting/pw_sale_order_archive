# -*- coding: utf-8 -*-
{
    'name': 'Sale order archive/unarchive | Archive Sales Reocrds',
    'version': '19.0.1.0',
    'author': "Preway IT Solutions",
    'category': 'Sales',
    'depends': ['sale'],
    'summary': 'This app helps you to archive or unarchive sale orders | Sales Archive Records | Sales Unarchive Records',
    'description': """This app helps you to archive or unarchive sale orders""",
    'data': [
        'security/sale_security.xml',
        'views/sale_order_view.xml',
    ],
    'price': 8.0,
    'currency': "EUR",
    'live_test_url': 'https://youtu.be/pd-bdNMAyQs',
    "images":["static/description/Banner.png"],
    'application': True,
    'installable': True,
    "license": "LGPL-3",
}
