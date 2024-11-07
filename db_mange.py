from app import app, db
from models import Dock

@app.cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.create_all()
    print("Database tables created successfully.")

@app.cli.command("drop_db")
def drop_db():
    """Drops the database tables."""
    db.drop_all()
    print("Database tables dropped successfully.")

@app.cli.command("seed_db")
def seed_db():
    """Adds some initial data to the database."""
    sample_dock = Dock(hubcode="HUB001", dock_no="DCK01", docking_status=False)
    db.session.add(sample_dock)
    db.session.commit()
    print("Database seeded successfully.")
