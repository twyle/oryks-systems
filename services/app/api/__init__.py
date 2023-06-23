from flask import Flask
from .blueprints import register_blueprints
from .config import set_configuration


def create_app() -> Flask:
    """Create the Flask App."""
    app = Flask(__name__)
    set_configuration(app)
    register_blueprints(app)
    
    app.shell_context_processor({"app": app})

    return app