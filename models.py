from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Subjects(UserMixin, db.Model):
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



class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(64), Index=True, Unique=True)
    email = db.Column(db.String(120), Index=True, Unique=True)
    password_hash = db.Column(db.String(120))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)