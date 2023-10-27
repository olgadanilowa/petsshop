import sqlite3

class DbConnect:
    url = '../../products_service/instance/database/goods.db'

    def __init__(self):
        db = sqlite3.connect(self.url)
        self.cursor=db.cursor()

    def select_product_from_db(self):
        product = self.cursor.execute('SELECT * from goods').fetchall()
        return product

    def select_order_by_id(self, product_id):
        r = self.cursor.execute(f'SELECT * from goods WHERE id={product_id}').fetchall()
        return r
