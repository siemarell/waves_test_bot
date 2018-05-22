import sqlite3


def get_last_update_index():
    with sqlite3.connect('test.db') as conn:
        return conn.execute("SELECT id FROM last_update_id").fetchall()[0][0]


def update_last_update_index(id):
    with sqlite3.connect('test.db') as conn:
        conn.execute("UPDATE last_update_id SET id = ?", (id,))


