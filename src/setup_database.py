import sqlite3

def execute_sql_file(db, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()

def setup_database():
    db = sqlite3.connect('test_nucleus.db')
    execute_sql_file(db, 'sql\create_tables.sql')
    execute_sql_file(db, 'sql\insert_data.sql')
    db.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")
