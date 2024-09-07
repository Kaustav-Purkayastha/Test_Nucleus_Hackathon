import unittest
from database import Database
import os

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = 'test_database.db'
        cls.db = Database(db_path=cls.db_path)
        cls.create_test_tables()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.db_path)

    @classmethod
    def create_test_tables(cls):
        cls.db.execute_query("""
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

    def test_insert_data(self):
        self.db.execute_query("INSERT INTO test_table (name) VALUES (?)", ('test_name',))
        result = self.db.fetch_query("SELECT name FROM test_table WHERE id = 1")
        self.assertEqual(result[0][0], 'test_name')

    def test_fetch_query(self):
        self.db.execute_query("INSERT INTO test_table (name) VALUES (?)", ('fetch_test',))
        result = self.db.fetch_query("SELECT name FROM test_table WHERE name = ?", ('fetch_test',))
        self.assertEqual(result[0][0], 'fetch_test')

if __name__ == '__main__':
    unittest.main()
