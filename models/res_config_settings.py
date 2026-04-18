# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    http_max_content_length = fields.Integer(
        string='Max Content Length (MB)',
        default=512,
        help='Maximum size of the entire HTTP request body in megabytes. '
             'Increase this to allow larger file uploads.',
    )
    http_max_form_memory_size = fields.Integer(
        string='Max Form Memory Size (MB)',
        default=512,
        help='Maximum size of form data stored in memory in megabytes. '
             'Increase this to allow larger form submissions.',
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        ICP = self.env['ir.config_parameter'].sudo()
        default_bytes = str(512 * 1024 * 1024)
        res['http_max_content_length'] = int(
            ICP.get_param('sm_http_limits.max_content_length', default_bytes)
        ) // (1024 * 1024)
        res['http_max_form_memory_size'] = int(
            ICP.get_param('sm_http_limits.max_form_memory_size', default_bytes)
        ) // (1024 * 1024)
        return res

    def set_values(self):
        super().set_values()
        ICP = self.env['ir.config_parameter'].sudo()
        content_bytes = self.http_max_content_length * 1024 * 1024
        form_bytes = self.http_max_form_memory_size * 1024 * 1024
        ICP.set_param('sm_http_limits.max_content_length', str(content_bytes))
        ICP.set_param('sm_http_limits.max_form_memory_size', str(form_bytes))

        # Apply immediately without restart
        from . import http_limits
        http_limits._max_content_length = content_bytes
        http_limits._max_form_memory_size = form_bytes
        http_limits._apply_limits()
