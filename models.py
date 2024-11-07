from app import db

class Dock(db.Model):
    __tablename__ = 'docks'

    id = db.Column(db.Integer, primary_key=True)
    hubcode = db.Column(db.String(50), unique=True, nullable=False)
    dock_no = db.Column(db.String(50), unique=True, nullable=False)
    docking_status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Dock {self.hubcode}, {self.dock_no}>'
