from __future__ import annotations

from flask import Flask

from . import utils
from .routes import bp


def create_app() -> Flask:
    """Factory to create the Flask application."""
    utils.ALL_ARTICLES = utils.load_articles()
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app
