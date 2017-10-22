from sqlalchemy import event

from app.database import db

class TestPlan(db.Model):
    __tablename__ = 'test_plan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(180), unique=False)
    status = db.Column(db.String(20), unique=False)

    test_case = db.relationship("TestCase", backref="test_plan", lazy="dynamic")
    user = db.relationship("User", backref="test_plan", lazy="dynamic")
