from flask import Blueprint
from flask_restful import Api
from resources import DockResource

# Initialize Blueprint and API
main_bp = Blueprint('main', __name__)
api = Api(main_bp)

def initialize_routes(app):
    """Register routes with the app"""
    app.register_blueprint(main_bp)

    # Register DockResource for POST request on /add_dock
    api.add_resource(DockResource, '/add_dock')
