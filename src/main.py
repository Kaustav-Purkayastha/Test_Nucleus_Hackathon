from database import Database
from test_dispatcher import TestDispatcher

def display_results(db):
    results = db.fetch_query("""
        SELECT tr.config_id, m.table_name, m.field_name, td.test_name, tr.test_passed, tr.test_output, tr.timestamp
        FROM test_results tr
        JOIN test_configuration tc ON tr.config_id = tc.config_id
        JOIN metadata m ON tc.metadata_id = m.id
        JOIN test_definitions td ON tc.test_id = td.test_id
    """)

    print("\nTest Results:")
    print("-" * 50)
    for result in results:
        config_id, table_name, field_name, test_name, test_passed, test_output, timestamp = result
        status = "PASS" if test_passed else "FAIL"
        print(
            f"[{timestamp}] Config ID: {config_id}, Table: {table_name}, Field: {field_name}, Test: {test_name}, Status: {status}, Output: {test_output}")
    print("-" * 50)

def main():
    # Initialize database connection
    db = Database()

    # Initialize Test Dispatcher
    test_dispatcher = TestDispatcher(db)

    # Execute the tests
    test_dispatcher.execute_tests()

    # Display the results
    display_results(db)

if __name__ == "__main__":
    main()
