# flask_app/app/__init__.py

from flask import Flask, session
from app.config import Config
from flask_session import Session  # Assuming Flask-Session is used for session management

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    print("Initialized ...")  # Debugging statement

    # Initialize session
    Session(app)

    # Register routes directly without app context
    from app.routes import register_routes
    register_routes(app)

    return app
