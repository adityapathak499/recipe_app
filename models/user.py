from flask_login import UserMixin
import sqlite3

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        conn = sqlite3.connect('recipes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE id=?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return User(user[0], user[1], user[2], user[3])
        return None

    @staticmethod
    def get_by_username(username):
        conn = sqlite3.connect('recipes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE username=?', (username,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return User(user[0], user[1], user[2], user[3])
        return None
