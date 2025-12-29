#!/usr/bin/env python3
"""
A small Flask app that displays the current local date and time.

Provides an application factory `create_app()` for easy testing and WSGI
integration. The root route `/` renders a simple template showing the
current timestamp.
"""
from __future__ import annotations
import os
from datetime import datetime
from flask import Flask, render_template, jsonify


def create_app(debug: bool = False) -> Flask:
    """Create and configure the Flask application.

    Args:
        debug: Enable Flask debug mode when True.

    Returns:
        Configured Flask app instance.
    """
    app = Flask(__name__, template_folder="templates")
    app.debug = debug

    @app.route("/")

    def index() -> str:
        """Render the index template with the current datetime."""
        now = datetime.now().astimezone()
        # ISO-like compact timestamp and human-friendly format
        iso_ts = now.isoformat(sep=" ", timespec="seconds")
        human_ts = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        return render_template("index.html", iso=iso_ts, human=human_ts)

    @app.route('/api/time')
    
    def api_time():
        """Return the current datetime as JSON (iso and human-readable).

        This endpoint is polled by the client every second to update the
        displayed time without reloading the page.
        """
        now = datetime.now().astimezone()
        iso_ts = now.isoformat(sep=" ", timespec="seconds")
        human_ts = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        return jsonify({"iso": iso_ts, "human": human_ts})

    return app


# Module-level app for WSGI servers / convenience imports
app: Flask = create_app()


def _env_bool(name: str, default: bool = False) -> bool:
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
