from database import Database

def setup_tables_with_test_data(db):
    # Create tables
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100),
            phone_number VARCHAR(15)
        );
    ''')
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS "order" (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date DATE,
            total_amount DECIMAL(10, 2),
            shipping_address VARCHAR(255),
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        );
    ''')
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name VARCHAR(100),
            price DECIMAL(10, 2),
            stock_quantity INTEGER
        );
    ''')

    # Insert data into customer table
    db.insert_data('''
        INSERT INTO customer (customer_id, first_name, last_name, email, phone_number) 
        VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890'),  # Valid
        (2, 'Jane', 'Smith', 'jane.smith@example.com', '098-765-4321'),  # Valid
        (3, 'Alice', 'Brown', None, '321-654-0987'),  # Null email (will pass Check Not Null if nullable is True)
        (4, 'Bob', 'Johnson', 'bob.johnson@example.com', ' '),  # Trailing space in phone number (Check No Trailing Spaces will fail)
        (5, 'Charlie', 'McCarthy', 'charliemc@example', '321-654-0987')  # Invalid email format (Check Email Format will fail)
    ])

    # Insert data into order table
    db.insert_data('''
        INSERT INTO "order" (order_id, customer_id, order_date, total_amount, shipping_address) 
        VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 1, '2023-09-01', 250.00, '123 Main St'),  # Valid
        (2, 2, '2023-09-02', 150.00, '456 Elm St'),  # Valid
        (3, 3, '2023-09-03', 500.00, '789 Oak St'),  # Valid
        (4, 4, '2023-09-04', -50.00, '246 Pine St'), # Negative total amount (Check Minimum Value will fail)
        (5, 5, '2023-09-05', 100.00, None)           # Null shipping address (Check Not Null will pass if nullable is True)
    ])

    # Insert data into product table
    db.insert_data('''
        INSERT INTO product (product_id, product_name, price, stock_quantity) 
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Widget', 19.99, 100),  # Valid
        (2, 'Gadget', 29.99, 50),   # Valid
        (3, 'Gizmo', 49.99, 50),    # Valid
        (4, 'Widget', 19.99, 50),   # Duplicate product_name (Check Unique Values will fail)
        (5, 'Thing', 99.99, -10)    # Negative stock_quantity (Check Minimum Value will fail)
    ])

if __name__ == "__main__":
    db = Database()
    setup_tables_with_test_data(db)
