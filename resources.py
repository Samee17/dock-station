from flask_restful import Resource, reqparse
from app import db
from models import Dock
from flask import request

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
    def get(self, hubcode, dock_no):
        """Get the docking status for a specific dock"""
        dock = Dock.query.filter_by(hubcode=hubcode, dock_no=dock_no).first()

        if dock:
            return {'dock_no': dock.dock_no, 'hubcode': dock.hubcode, 'docking_status': dock.docking_status}, 200
        else:
            return {'message': 'Dock not found'}, 404

    def put(self):
        """Update the docking status for a specific dock using payload"""
        # Get data from the request payload
        data = request.get_json()

        # Extract values from the JSON payload
        hubcode = data.get('hubcode')
        dock_no = data.get('dock_no')
        docking_status = data.get('docking_status')

        # Ensure that all necessary data is provided
        if not hubcode or not dock_no or docking_status is None:
            return {'message': 'hubcode, dock_no, and docking_status are required'}, 400

        # Find the dock entry based on hubcode and dock_no
        dock = Dock.query.filter_by(hubcode=hubcode, dock_no=dock_no).first()

        if not dock:
            return {'message': 'Dock not found'}, 404

        # Update the docking status
        dock.docking_status = docking_status

        # Commit changes to the database
        db.session.commit()

        return {'message': f'Docking status for dock {dock_no} at hub {hubcode} updated to {docking_status}'}, 200
