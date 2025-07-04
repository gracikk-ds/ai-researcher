"""Web application for the paper research website."""

from flask import Flask

from webapp import utils
from webapp.routes import bp


def create_app() -> Flask:
    """Create the Flask application.

    Returns:
        Flask: The Flask application.
    """
    utils.ALL_ARTICLES = utils.load_articles()
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
