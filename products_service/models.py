from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

class Goods(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(256))
    price=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    description=db.Column(db.String)

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'quantity':self.quantity,
            'description':self.description
        }
class Basket(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    basket_id=db.Column(db.String(256))
    user_id=db.Column(db.String(256))
    product_id=db.Column(db.String(256))
    quantity=db.Column(db.Integer)
    sum=db.Column(db.Integer)

    def serialize(self):
        return {
            'id':self.id,
            'basket_id':self.basket_id,
            'user_id':self.user_id,
            'product_id':self.product_id,
            'quantity':self.quantity,
            'sum':self.sum

        }
