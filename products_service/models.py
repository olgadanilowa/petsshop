from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

class Goods(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(256))
    price=db.Column(db.Integer)
    quantity=db.Column(db.String)
    description=db.Column(db.String)

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'quantity':self.quantity,
            'description':self.description
        }
