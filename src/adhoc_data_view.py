import sqlite3


def list_tables_and_data(db_path='test_nucleus.db'):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get a list of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Iterate over each table and print its contents
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        column_names = [description[1] for description in cursor.fetchall()]
        print(f"Columns: {', '.join(column_names)}")

        # Print rows
        for row in rows:
            print(row)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    list_tables_and_data()
