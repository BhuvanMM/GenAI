from flask import Flask

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Import parts of our application
    with app.app_context():
        from . import main
        return app