import re

def validate_email_format(email):
    """
    Validate email format using a regex pattern.
    :param email: Email address to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone_number_format(phone_number):
    """
    Validate phone number format using a regex pattern.
    :param phone_number: Phone number to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^\+?\d{1,4}[\s.-]?\(?\d{1,3}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,9}$"
    return bool(re.match(pattern, phone_number))

def validate_url_format(url):
    """
    Validate URL format using a regex pattern.
    :param url: URL to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^(https?:\/\/)?([\w\d\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
    return bool(re.match(pattern, url))

def is_not_null(value):
    """
    Check if the value is not null.
    :param value: Value to check
    :return: True if not null, False otherwise
    """
    return value is not None

def check_length(value, max_length):
    """
    Check if the length of the value does not exceed max_length.
    :param value: Value to check
    :param max_length: Maximum allowed length
    :return: True if length is within limit, False otherwise
    """
    return len(value) <= max_length

def remove_trailing_spaces(value):
    """
    Remove trailing spaces from the value.
    :param value: Value to process
    :return: Value with trailing spaces removed
    """
    return value.strip()

def check_min_value(value, min_value):
    """
    Check if the value is greater than or equal to the minimum value.
    :param value: Value to check
    :param min_value: Minimum allowed value
    :return: True if value is above or equal to min_value, False otherwise
    """
    return value >= min_value

def check_date_validity(date_str):
    """
    Check if the date string is a valid date.
    :param date_str: Date string to validate
    :return: True if valid date, False otherwise
    """
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def check_data_consistency(value, related_values):
    """
    Check if the value exists in the list of related values for consistency.
    :param value: Value to check
    :param related_values: List of related values to check against
    :return: True if value is in related values, False otherwise
    """
    return value in related_values
