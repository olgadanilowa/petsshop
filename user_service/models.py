import json
from time import strftime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(256), unique=True)
    date_birth = db.Column(db.String(10))
    customer_type = db.Column(db.String(256))
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))
    token_issue_time = db.Column(db.Time)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'date_birth': self.date_birth,
            'customer_type': self.customer_type,
            'password': self.password
        }

    def logged_in(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'date_birth': self.date_birth,
            'customer_type': self.customer_type,
            'password': self.password,
            'token': self.token,
            'token_issue_time': self.token_issue_time.strftime("%H:%M:%S")
        }
