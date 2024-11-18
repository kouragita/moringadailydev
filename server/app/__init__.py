import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

# Import your models
from app.models import db

# Extensions
ma = Marshmallow()
migrate = Migrate()

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/*": {"origins": "*"}})
    api = Api(app)

    # Register routes
    from .routes import register_routes
    register_routes(api)

    # # Register error handlers
    # from .utils.helpers import register_error_handlers
    # register_error_handlers(app)

    return app
