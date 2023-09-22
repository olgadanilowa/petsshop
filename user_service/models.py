from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(256),unique=True)
    email=db.Column(db.String(256),unique=True)
    date_birth=db.Column(db.String(10))

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'date_birth':self.date_birth
        }
