#!/usr/bin/env python3
"""
Minimal Flask application.

This file provides a small, documented and test-friendly Flask app.
It uses an application factory (`create_app`) and reads runtime
configuration from environment variables to avoid hardcoding debug
settings in the `__main__` block.
"""

from __future__ import annotations
import os
from flask import Flask


def create_app(debug: bool = False) -> Flask:
    """
    Create and configure a Flask application.

    Args:
        debug: Whether to enable Flask debug mode for development.

    Returns:
        Configured `Flask` application instance.
    """
    app = Flask(__name__)
    app.debug = debug

    @app.route("/")
    def hello() -> str:
        """Return a friendly German greeting for the root path."""
        return "Hallo von Flask!"

    return app


# Module-level application (useful for WSGI servers or imports)
app: Flask = create_app()


def _env_bool(name: str, default: bool = False) -> bool:
    """Interpret common truthy environment variable values as boolean.

    Recognised truthy values: '1', 'true', 'yes', 'on' (case-insensitive).
    """
    val = os.getenv(name)
    if val is None:
        return default
    return val.lower() in ("1", "true", "yes", "on")


if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    debug = _env_bool("FLASK_DEBUG", False)

    app = create_app(debug=debug)
    app.run(host=host, port=port, debug=debug)
