from flask_restful import Resource
from app import db
from models import Dock
from flask import request,jsonify

class DockResource(Resource):
    def post(self):
        """Create a new dock"""
        data = request.get_json()
        hubcode = data.get("hubcode")
        dock_no = data.get("dock_no")
        docking_status = data.get("docking_status")

        # Create a new Dock instance
        dock = Dock(hubcode=hubcode, dock_no=dock_no, docking_status=docking_status)

        # Add to the database and commit
        db.session.add(dock)
        db.session.commit()

        return {"message": "Dock added successfully"}, 201

    def get(self):
        """Get details of all docks"""
        docks = Dock.query.all()
        result = [{"hubcode": dock.hubcode, "dock_no": dock.dock_no, "docking_status": dock.docking_status} for dock in
                  docks]
        return {"docks": result}, 200

    class DockStatusResource(Resource):
        def patch(self, dock_no):
            """Update the docking_status of a dock by its dock_no"""
            parser = reqparse.RequestParser()
            parser.add_argument('docking_status', type=bool, required=True, help="docking_status is required")
            args = parser.parse_args()

            dock = Dock.query.filter_by(dock_no=dock_no).first()
            if not dock:
                return {"message": f"Dock with dock_no '{dock_no}' not found."}, 404

            dock.docking_status = args['docking_status']
            db.session.commit()

            return {"message": f"Docking status updated for dock_no '{dock_no}'.",
                    "docking_status": dock.docking_status}, 200
