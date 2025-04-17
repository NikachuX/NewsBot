import sqlite3 as sq

class DataBase:

    def __init__(self):
        self.db = sq.connect('users.db')
        self.db.close()

    def db_conect(self):
        self.db = sq.connect('users.db')
        self.db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS users(user_id TEXT, time TEXT, categories TEXT, position INTEGER)")
        self.db.commit()
        self.db.close()

    def set_user(self, user_id):
        self.db = sq.connect('users.db')
        self.db.cursor().execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        result = self.db.cursor().fetchone()
        if result is None:
            self.db.cursor().execute("INSERT INTO users (user_id) VALUES (?)",(user_id,))
        self.db.commit()
        self.db.close()

    def add_cat(self, user_id, categories):
        self.db = sq.connect('users.db')
        self.db.cursor().execute("UPDATE users SET categories = ? WHERE user_id = ?",
        (categories, user_id))
        self.db.commit()
        self.db.close()

    def get_cat(self, user_id):
        self.db = sq.connect('users.db')
        cat = str(db.db.cursor().execute("SELECT categories FROM users WHERE user_id = ?", (user_id,)).fetchone()[0])
        self.db.close()
        return cat

db = DataBase()

