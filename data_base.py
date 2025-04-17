import sqlite3 as sq

class DataBase:

    def __init__(self):
        self.db = sq.connect('users.db')
        self.db.close()

    def db_conect(self):
        self.db = sq.connect('users.db')
        self.db.cursor().execute(
            """CREATE TABLE IF NOT EXISTS users(user_id TEXT, science TEXT, culture TEXT, economy TEXT,
            sport TEXT, world TEXT)""")
        self.db.commit()
        self.db.close()

    def set_user(self, user_id):
        self.db = sq.connect('users.db')
        result = self.db.cursor().execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()
        if result is None:
            self.db.cursor().execute("INSERT INTO users (user_id) VALUES (?)",(user_id,))
            self.db.commit()
        self.db.close()

    def add_cat(self, user_id, categories, text):
        self.db = sq.connect('users.db')
        self.db.cursor().execute(f"UPDATE users SET {categories} = ? WHERE user_id = ?",
        (text, user_id))
        self.db.commit()
        self.db.close()

    def get_cat(self, user_id):
        self.db = sq.connect('users.db')
        cats = self.db.cursor().execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()[0][1:]
        cats = [cat for cat in cats if cat is not None]
        self.db.close()
        return cats

db = DataBase()

