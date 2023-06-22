from flask import Flask
from .home.views import home

def register_blueprints(app: Flask) -> None:
    """Register the application blueprints.

    Parameters
    ----------
    app: flask.Flask
        A flask app instance
    """
    app.register_blueprint(home)