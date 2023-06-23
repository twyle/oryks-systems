from dotenv import load_dotenv
import os
from .config import Config
from flask import Flask

load_dotenv()

def set_configuration(app: Flask) -> None:
    """Set the application configuration.

    The application configuration will depend on the
    environment i.e Test, Development, Staging or Production.

    Parameters
    ----------
    app: flask.Flask
        A flask app instance
    """
    config_name = os.environ.get("FLASK_ENV", 'Development')
    app.config.from_object(Config[config_name])