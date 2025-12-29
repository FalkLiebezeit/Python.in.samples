#!/usr/bin/env python3
"""
Simple Flask example app.

Optimized and commented version of the original `HelloWorld.py`.
Provides an application factory (`create_app`) for easier testing and
reads host/port/debug configuration from environment variables.
"""

from __future__ import annotations
import os
from typing import Optional
from flask import Flask


def create_app(debug: bool = False) -> Flask:
    """
    Application factory. Returns a configured Flask application.

    Args:
        debug: Whether to enable Flask debug mode.

    Returns:
        A configured `Flask` instance with routes registered.
    """
    app = Flask(__name__)
    app.debug = debug

    @app.route("/")
    def hello() -> str:
        """Return a friendly greeting for the root path.

        Kept intentionally simple for demonstration and tests.
        """
        return "Hello, World!"

    return app


# Module-level app useful for WSGI servers (e.g., gunicorn) or imports.
app: Flask = create_app()


def _env_bool(name: str, default: bool = False) -> bool:
    """Read an environment variable and interpret common truthy values.

    Accepts: '1', 'true', 'yes', 'on' (case-insensitive) as True.
    """
    val = os.getenv(name)
    if val is None:
        return default
    return val.lower() in ("1", "true", "yes", "on")


if __name__ == "__main__":
    # Configuration from environment variables with safe defaults.
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    debug = _env_bool("FLASK_DEBUG", False)

    # Create the app with the chosen debug setting and run it.
    app = create_app(debug=debug)
    app.run(host=host, port=port, debug=debug)