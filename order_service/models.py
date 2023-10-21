from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    delivery_adress=db.Column(db.String(256))
    order_status=db.Column(db.String(256))
    order_comment=db.Column(db.String(256))
    promocode=db.Column(db.Boolean)

    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'delivery_status':self.delivery_status,
            'order_status':self.order_status,
            'order_comment':self.order_comment,
            'promocode':self.promocode
        }
