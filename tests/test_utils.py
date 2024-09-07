import unittest
from utils import validate_email_format, is_not_null, check_length, remove_trailing_spaces

class TestUtils(unittest.TestCase):
    def test_validate_email_format(self):
        self.assertTrue(validate_email_format("test@example.com"))
        self.assertFalse(validate_email_format("invalid-email"))

    def test_is_not_null(self):
        self.assertTrue(is_not_null("value"))
        self.assertFalse(is_not_null(None))

    def test_check_length(self):
        self.assertTrue(check_length("short", 10))
        self.assertFalse(check_length("too long string", 10))

    def test_remove_trailing_spaces(self):
        self.assertEqual(remove_trailing_spaces("  value  "), "value")
        self.assertEqual(remove_trailing_spaces("no_space"), "no_space")

if __name__ == '__main__':
    unittest.main()
