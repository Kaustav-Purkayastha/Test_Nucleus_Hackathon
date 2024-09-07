import datetime
from database import Database
from utils import (validate_email_format, validate_phone_number_format, validate_url_format,
                   remove_trailing_spaces, check_length, is_not_null, check_min_value,
                   check_date_validity, check_data_consistency)


class TestDispatcher:
    def __init__(self, db):
        self.db = db

    def execute_tests(self):
        test_configs = self.db.fetch_query("""
            SELECT tc.config_id, m.table_name, m.field_name, td.function_name, td.parameters 
            FROM test_configuration tc
            JOIN metadata m ON tc.metadata_id = m.id
            JOIN test_definitions td ON tc.test_id = td.test_id
        """)

        for config in test_configs:
            config_id, table_name, field_name, function_name, parameters = config

            # Safe handling of parameters
            try:
                if 'max_length' in parameters:
                    # Handle tests requiring max_length
                    parameters = parameters.format(table_name=table_name, field_name=field_name, max_length=255)
                elif 'min_value' in parameters:
                    # Handle tests requiring min_value
                    parameters = parameters.format(table_name=table_name, field_name=field_name, min_value=0)
                elif 'related_table' in parameters:
                    # Handle tests requiring related_table and related_field
                    parameters = parameters.format(table_name=table_name, field_name=field_name,
                                                   related_table='related_table', related_field='related_field')
                else:
                    # Format for other tests
                    parameters = parameters.format(table_name=table_name, field_name=field_name)

                # Call the test function dynamically
                test_passed, test_output = getattr(self, function_name)(table_name, field_name, parameters)
                self.log_test_result(config_id, test_passed, test_output)
                self.audit_log("TEST_EXECUTED", table_name, field_name)
                log_level = "INFO" if test_passed else "WARNING"
                self.log_message(log_level, f"Test {function_name} on {table_name}.{field_name}: {test_output}")

            except Exception as e:
                # Handle any exceptions during test execution
                self.log_message("ERROR", f"Failed to execute {function_name} on {table_name}.{field_name}: {str(e)}")

    def check_not_null(self, table_name, field_name, parameters):
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {field_name} IS NULL;"
        result = self.db.fetch_query(query)
        test_passed = result[0][0] == 0
        test_output = f"{field_name} in {table_name} has {'no' if test_passed else ''} NULL values."
        return test_passed, test_output

    def check_length(self, table_name, field_name, parameters):
        max_length = int(parameters.split(", ")[-1])
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        exceeding_values = [value for value in data if not check_length(value[0], max_length)]
        test_passed = len(exceeding_values) == 0
        test_output = f"{field_name} in {table_name} {'meets' if test_passed else 'exceeds'} length limit of {max_length}."
        return test_passed, test_output

    def check_no_trailing_spaces(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        values_with_spaces = [value for value in data if value[0] != remove_trailing_spaces(value[0])]
        test_passed = len(values_with_spaces) == 0
        test_output = f"{field_name} in {table_name} {'has no' if test_passed else 'has'} trailing spaces."
        return test_passed, test_output

    def check_email_format(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        invalid_emails = [email for email in data if not validate_email_format(email[0])]
        test_passed = len(invalid_emails) == 0
        test_output = f"All emails in {field_name} of {table_name} {'are' if test_passed else 'are not'} in valid format."
        return test_passed, test_output

    def check_unique_values(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        values = [value[0] for value in data]
        unique_values = list(set(values))
        test_passed = len(values) == len(unique_values)
        test_output = f"All values in {field_name} of {table_name} {'are' if test_passed else 'are not'} unique."
        return test_passed, test_output

    def check_phone_number_format(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        invalid_phone_numbers = [phone_number for phone_number in data if
                                 not validate_phone_number_format(phone_number[0])]
        test_passed = len(invalid_phone_numbers) == 0
        test_output = f"All phone numbers in {field_name} of {table_name} {'are' if test_passed else 'are not'} in valid format."
        return test_passed, test_output

    def check_url_format(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        invalid_urls = [url for url in data if not validate_url_format(url[0])]
        test_passed = len(invalid_urls) == 0
        test_output = f"All URLs in {field_name} of {table_name} {'are' if test_passed else 'are not'} in valid format."
        return test_passed, test_output

    def check_date_validity(self, table_name, field_name, parameters):
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        invalid_dates = [date_str for date_str in data if not check_date_validity(date_str[0])]
        test_passed = len(invalid_dates) == 0
        test_output = f"All dates in {field_name} of {table_name} {'are' if test_passed else 'are not'} valid."
        return test_passed, test_output

    def check_min_value(self, table_name, field_name, parameters):
        min_value = int(parameters.split(", ")[-1])
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        below_min_values = [value for value in data if not check_min_value(value[0], min_value)]
        test_passed = len(below_min_values) == 0
        test_output = f"All values in {field_name} of {table_name} {'meet' if test_passed else 'do not meet'} the minimum value of {min_value}."
        return test_passed, test_output

    def check_data_consistency(self, table_name, field_name, parameters):
        related_table, related_field = parameters.split(", ")[2:4]
        query = f"SELECT {field_name} FROM {table_name}"
        data = self.db.fetch_query(query)
        related_values = [value[0] for value in self.db.fetch_query(f"SELECT {related_field} FROM {related_table}")]
        inconsistent_values = [value for value in data if not check_data_consistency(value[0], related_values)]
        test_passed = len(inconsistent_values) == 0
        test_output = f"Data in {field_name} of {table_name} is {'consistent' if test_passed else 'inconsistent'} with {related_table}.{related_field}."
        return test_passed, test_output

    def log_test_result(self, config_id, test_passed, test_output):
        self.db.execute_query("""
            INSERT INTO test_results (config_id, test_passed, test_output) 
            VALUES (?, ?, ?)
        """, (config_id, test_passed, test_output))

    def audit_log(self, operation, table_name, field_name):
        self.db.execute_query("""
            INSERT INTO audit_logs (operation, table_name, field_name) 
            VALUES (?, ?, ?)
        """, (operation, table_name, field_name))

    def log_message(self, log_level, message):
        self.db.execute_query("""
            INSERT INTO logs (log_level, message) 
            VALUES (?, ?)
        """, (log_level, message))
