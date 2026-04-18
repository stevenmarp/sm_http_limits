# -*- coding: utf-8 -*-
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)

# Default limits (512 MB)
DEFAULT_LIMIT = 512 * 1024 * 1024

_max_content_length = DEFAULT_LIMIT
_max_form_memory_size = DEFAULT_LIMIT


def _apply_limits():
    """Apply the current limits to odoo.http."""
    try:
        import odoo.http as http
        # Odoo 17+ exposes DEFAULT_MAX_CONTENT_LENGTH
        if hasattr(http, 'DEFAULT_MAX_CONTENT_LENGTH'):
            http.DEFAULT_MAX_CONTENT_LENGTH = _max_content_length

        # Patch HTTPRequest.__init__ to also set max_form_memory_size
        if hasattr(http, 'HTTPRequest') and not getattr(http.HTTPRequest, '_sm_patched', False):
            _orig_init = http.HTTPRequest.__init__

            def _patched_init(self, environ):
                _orig_init(self, environ)
                self.max_content_length = _max_content_length
                self.max_form_memory_size = _max_form_memory_size

            http.HTTPRequest.__init__ = _patched_init
            http.HTTPRequest._sm_patched = True

    except Exception:
        _logger.warning("sm_http_limits: could not patch odoo.http, trying werkzeug directly")
        try:
            from werkzeug.wrappers import Request
            Request.max_content_length = _max_content_length
            Request.max_form_memory_size = _max_form_memory_size
        except Exception:
            _logger.exception("sm_http_limits: failed to apply HTTP limits")


# Apply immediately on module import (server load)
_apply_limits()


class SmHttpLimits(models.AbstractModel):
    _name = 'sm.http.limits'
    _description = 'HTTP Limits Patcher'

    def _register_hook(self):
        """Reload limits from ir.config_parameter on server start."""
        global _max_content_length, _max_form_memory_size
        ICP = self.env['ir.config_parameter'].sudo()
        _max_content_length = int(
            ICP.get_param('sm_http_limits.max_content_length', str(DEFAULT_LIMIT))
        )
        _max_form_memory_size = int(
            ICP.get_param('sm_http_limits.max_form_memory_size', str(DEFAULT_LIMIT))
        )
        _apply_limits()
        _logger.info(
            "sm_http_limits: max_content_length=%s MB, max_form_memory_size=%s MB",
            _max_content_length // (1024 * 1024),
            _max_form_memory_size // (1024 * 1024),
        )
