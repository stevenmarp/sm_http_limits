# -*- coding: utf-8 -*-
{
    'name': 'HTTP Limits | Fix 413 Error',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Fix "413: Request Entity Too Large" — Increase HTTP upload & form size limits',
    'description': """
HTTP Limits | Fix 413: Request Entity Too Large
================================================

Resolve the **Request Entity Too Large** error by increasing Werkzeug / Odoo
HTTP request size limits. Configurable from Settings — no code changes needed.
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/browse?repo_maintainer_id=512936',
    'license': 'OPL-1',
    'depends': ['base', 'base_setup'],
    'data': [
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.gif', 'static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 0.00,
    'currency': 'USD',
}
