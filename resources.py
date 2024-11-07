from flask import request, jsonify
from app import db
from models import Dock


def get_all_docks():
    docks = Dock.query.all()
    return jsonify([dock.to_dict() for dock in docks]), 200


def update_docking_status(hubcode):
    data = request.get_json()
    docking_status = data.get("docking_status", None)

    if docking_status is None:
        return jsonify({"error": "Missing docking_status in payload"}), 400

    dock = Dock.query.filter_by(hubcode=hubcode).first()
    if not dock:
        return jsonify({"error": "Dock not found"}), 404

    dock.docking_status = docking_status
    db.session.commit()
    return jsonify(dock.to_dict()), 200
