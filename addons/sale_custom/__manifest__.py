# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# 

{
    'name': 'Sales Custom Report',
    'version': '17.0.1.0',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': [
        'base', 
        'sale'
    ],
    'data': [
        'reports/ir_actions_report.xml',
        'reports/report_sale_order_custom1.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}