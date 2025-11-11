#!/usr/bin/env python3
"""
Simple HTTP server with path rewriting for the Fin.ai replica.
This server rewrites Next.js paths to local asset paths.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import os

class RewriteHandler(SimpleHTTPRequestHandler):
    """HTTP handler that rewrites Next.js paths to local paths."""

    def translate_path(self, path):
        """Translate Next.js paths to local file paths."""
        # Remove query parameters
        path = path.split('?')[0]

        # Rewrite Next.js paths
        if path.startswith('/_next/static/css/'):
            # CSS files: /_next/static/css/file.css -> ./assets/file.css
            filename = path.replace('/_next/static/css/', '')
            path = f'/assets/{filename}'
        elif path.startswith('/_next/static/media/'):
            # Font files: /_next/static/media/file.woff2 -> ./fonts/file.woff2
            filename = path.replace('/_next/static/media/', '')
            path = f'/fonts/{filename}'
        elif path.startswith('/_next/image'):
            # Next.js Image API - return 404, we can't replicate this
            return None
        elif path.startswith('/img/home/'):
            # Images: /img/home/file.webp -> ./images/file.webp
            filename = path.replace('/img/home/', '')
            path = f'/images/{filename}'

        # Call parent's translate_path with the rewritten path
        return super().translate_path(path)

    def log_message(self, format, *args):
        """Log HTTP requests with better formatting."""
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))

def run_server(port=8000):
    """Start the HTTP server."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, RewriteHandler)
    print(f"🚀 Server running at http://localhost:{port}")
    print(f"📝 Press Ctrl+C to stop")
    print("")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        sys.exit(0)

if __name__ == '__main__':
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_server(3000)
