```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a memory database for fast testing
        print(f'successful SQLite connection with id {id(conn)}')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_players_table = """ CREATE TABLE IF NOT EXISTS players (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        team text NOT NULL,
                                        position text NOT NULL
                                    ); """

    sql_create_performance_table = """CREATE TABLE IF NOT EXISTS performance (
                                    id integer PRIMARY KEY,
                                    player_id integer NOT NULL,
                                    game_date text NOT NULL,
                                    metric text NOT NULL,
                                    value real NOT NULL,
                                    FOREIGN KEY (player_id) REFERENCES players (id)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_performance_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```