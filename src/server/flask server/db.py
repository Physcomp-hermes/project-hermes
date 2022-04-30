import sqlite3

DATABASE_NAME = "hermes.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME, detect_types=sqlite3.PARSE_DECLTYPES)
    return conn


def create_tables():
    tables = [
        '''CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				Interest TEXT NOT NULL
            )''',

    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

#
# from datetime import datetime
#
# db = get_db()
# c = db.cursor()
# c.execute('select * from actor')
# print(datetime.fromisoformat(c.fetchall()[0][2]))
