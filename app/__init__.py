# flask_app/app/__init__.py

from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Import routes
        from app import routes
        
    return app
