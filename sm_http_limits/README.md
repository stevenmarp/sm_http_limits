# HTTP Limits | Fix 413: Request Entity Too Large

Fix the "413: Request Entity Too Large" error in Odoo by increasing HTTP
request size limits. Configurable from Settings — no code changes needed.

## Features

- Fixes 413 error on large file uploads and form submissions
- Configurable max content length (default 512 MB)
- Configurable max form memory size (default 512 MB)
- Settings UI under General Settings → HTTP Limits
- Works instantly on install — zero configuration required
- Limits persist across server restarts
- Zero external dependencies
- Community & Enterprise compatible

## Installation

Install from the Odoo Apps store or copy the module folder to your addons path.

## Configuration

After installation, go to **Settings → HTTP Limits** to adjust the limits.
Default values (512 MB) work for most use cases.

## License

OPL-1
