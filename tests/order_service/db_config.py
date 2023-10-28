import sqlite3

class DbConnect:
    url = '../../order_service/instance/database/orders.db'

    def __init__(self):
        db = sqlite3.connect(self.url)
        self.cursor=db.cursor()

    def select_orders_from_db(self):
        orders = self.cursor.execute('SELECT * from orders').fetchall()
        return orders

    def select_order_by_id(self, order_id):
        r = self.cursor.execute(f'SELECT * from user WHERE id={order_id}').fetchall()
        return r
