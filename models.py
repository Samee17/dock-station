from app import db


class Dock(db.Model):
    __tablename__ = 'docks'

    hubcode = db.Column(db.String(10), primary_key=True, unique=True, nullable=False)
    dock_no = db.Column(db.String(20), nullable=False)
    docking_status = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, hubcode, dock_no, docking_status=False):
        self.hubcode = hubcode
        self.dock_no = dock_no
        self.docking_status = docking_status

    def to_dict(self):
        return {
            "hubcode": self.hubcode,
            "dock_no": self.dock_no,
            "docking_status": self.docking_status
        }
