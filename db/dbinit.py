import sqlite3


def init():
    with sqlite3.connect('test.db') as conn :
        conn.execute('''DROP TABLE IF EXISTS last_update_id;''')
        conn.commit()
        conn.execute('''
                CREATE TABLE last_update_id(
                  id INT NOT NULL 
                );
            ''')
        conn.execute('''INSERT INTO last_update_id VALUES (0)''')

if __name__ == '__main__':
   init()

