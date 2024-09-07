-- Inserting data into metadata table
INSERT INTO metadata (table_name, field_name, data_type, is_nullable, is_primary_key, is_testable, description)
VALUES
('customer', 'customer_id', 'INT', 0, 1, 1, 'Primary key for customer table'),
('customer', 'first_name', 'VARCHAR', 0, 0, 1, 'First name of the customer'),
('customer', 'last_name', 'VARCHAR', 0, 0, 1, 'Last name of the customer'),
('customer', 'email', 'VARCHAR', 1, 0, 1, 'Email address of the customer'),
('order', 'order_id', 'INT', 0, 1, 1, 'Primary key for order table'),
('order', 'customer_id', 'INT', 0, 0, 1, 'Foreign key linking to customer table'),
('order', 'order_date', 'DATE', 0, 0, 1, 'Date when the order was placed'),
('order', 'total_amount', 'DECIMAL', 0, 0, 1, 'Total amount of the order'),
('product', 'product_id', 'INT', 0, 1, 1, 'Primary key for product table'),
('product', 'product_name', 'VARCHAR', 0, 0, 1, 'Name of the product'),
('product', 'price', 'DECIMAL', 0, 0, 1, 'Price of the product'),
('product', 'stock_quantity', 'INT', 0, 0, 1, 'Available stock quantity'),
('customer', 'phone_number', 'VARCHAR', 1, 0, 1, 'Phone number of the customer'),
('order', 'shipping_address', 'VARCHAR', 1, 0, 1, 'Shipping address for the order');


-- Inserting data into test_definitions table
INSERT INTO test_definitions (test_name, test_description, test_type, function_name, parameters)
VALUES
('Check Not Null', 'Ensure no null values exist', 'SQL', 'check_not_null', '{table_name}, {field_name}'),
('Check Length', 'Ensure data length does not exceed max length', 'SQL', 'check_length', '{table_name}, {field_name}, {max_length}'),
('Check No Trailing Spaces', 'Ensure no trailing spaces in data', 'SQL', 'check_no_trailing_spaces', '{table_name}, {field_name}'),
('Check Email Format', 'Ensure valid email format', 'REGEX', 'check_email_format', '{table_name}, {field_name}'),
('Check Unique Values', 'Ensure all values in a column are unique', 'SQL', 'check_unique_values', '{table_name}, {field_name}'),
('Check Phone Number Format', 'Ensure phone numbers follow the correct format', 'REGEX', 'check_phone_number_format', '{table_name}, {field_name}'),
('Check URL Format', 'Ensure URLs are in a valid format', 'REGEX', 'check_url_format', '{table_name}, {field_name}'),
('Check Date Validity', 'Ensure dates are valid', 'PYTHON', 'check_date_validity', '{table_name}, {field_name}'),
('Check Minimum Value', 'Ensure numeric values are above a minimum threshold', 'PYTHON', 'check_min_value', '{table_name}, {field_name}, {min_value}'),
('Check Data Consistency', 'Ensure related data across tables is consistent', 'PYTHON', 'check_data_consistency', '{table_name}, {field_name}, {related_table}, {related_field}');


-- Inserting data into test_configuration table
INSERT INTO test_configuration (metadata_id, test_id)
VALUES
(1, 1),  -- Check Not Null on customer_id
(2, 2),  -- Check Length on first_name
(3, 2),  -- Check Length on last_name
(4, 4),  -- Check Email Format on email
(5, 1),  -- Check Not Null on order_id
(6, 1),  -- Check Not Null on customer_id in order table
(7, 1),  -- Check Not Null on order_date
(8, 2),  -- Check Length on total_amount
(9, 5),  -- Check Unique Values on product_id
(10, 6), -- Check Phone Number Format on phone_number
(11, 7), -- Check URL Format on shipping_address (assuming URLs are stored here for some reason)
(12, 8), -- Check Date Validity on order_date
(13, 9), -- Check Minimum Value on price
(14, 10) -- Check Data Consistency between order and customer tables
;


