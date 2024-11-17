from flask import Blueprint
from flask_restful import Api
from resources import DockResource

# Initialize Blueprint and API
main_bp = Blueprint('main', __name__)
api = Api(main_bp)

def initialize_routes(app):
    """Register routes with the app"""
    app.register_blueprint(main_bp)

    # Register DockResource for POST request on /add_dock with a custom endpoint
    api.add_resource(DockResource, '/add_dock', endpoint='add_dock')
    # Register DockResource for both POST and GET requests on /dock with a custom endpoint
    api.add_resource(DockResource, '/dock', endpoint='dock')
    # Register DockStatusResource for PATCH request on /dock_status/<dock_no>
    api.add_resource(DockStatusResource, '/dock_status/<string:dock_no>', endpoint='dock_status')

