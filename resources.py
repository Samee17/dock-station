from flask_restful import Resource
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
