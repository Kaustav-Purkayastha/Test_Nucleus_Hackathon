import sqlite3
from contextlib import closing

class Database:
    def __init__(self, db_path='test_nucleus.db'):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=None):
        with closing(self.connect()) as conn, closing(conn.cursor()) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()

    def fetch_query(self, query, params=None):
        with closing(self.connect()) as conn, closing(conn.cursor()) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def insert_data(self, query, data):
        with closing(self.connect()) as conn, closing(conn.cursor()) as cursor:
            cursor.executemany(query, data)
            conn.commit()
