from app import db
from datetime import datetime


class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    student = db.relationship('Students', backref='subjects', lazy=True)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birth_date = db.Column(db.Date, nullable=False, default=datetime.now())
    mark = db.Column(db.Float, nullable=False, default=5.0)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    status = db.Column(db.String(4), nullable=False, default='free')