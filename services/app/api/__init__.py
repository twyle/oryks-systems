from flask import Flask
from .blueprints import register_blueprints


def create_app() -> Flask:
    """Create the Flask App."""
    app = Flask(__name__)
    
    register_blueprints(app)
    
    app.shell_context_processor({"app": app})

    return app