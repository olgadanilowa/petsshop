import sqlite3


class DbConnect:
    url = '../../user_service/instance/database/user.db'

    def __init__(self):
        db = sqlite3.connect(self.url)
        self.cursor=db.cursor()

    def select_users_from_db(self):
        user = self.cursor.execute('SELECT * from user').fetchall()
        return user

    def count_users_db(self):
        user = self.cursor.execute('SELECT COUNT(*) from user').fetchall()
        return user[0][0]
