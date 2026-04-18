# -*- coding: utf-8 -*-
{
    'name': 'HTTP Limits | Fix 413 Error',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Fix "413: Request Entity Too Large" — Increase HTTP upload & form size limits',
    'description': """
HTTP Limits | Fix 413: Request Entity Too Large
================================================

Resolve the **Request Entity Too Large** error by increasing Werkzeug / Odoo
HTTP request size limits. Configurable from Settings — no code changes needed.

Features
--------
* Fixes 413 error on large file uploads and form submissions
* Configurable max content length (default 512 MB)
* Configurable max form memory size (default 512 MB)
* Settings UI under General Settings → HTTP Limits
* Works instantly on install — zero configuration required
* Limits persist across server restarts
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
