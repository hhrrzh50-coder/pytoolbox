import unittest
from datetime import date

from pytoolbox import (
    calculate_pi,
    clamp,
    days_between,
    deduplicate,
    is_email,
    is_url,
    mean,
    median,
    random_choice,
    random_password,
    slugify,
    truncate,
)


class ToolboxTests(unittest.TestCase):
    def test_pi_calculation(self):
        self.assertEqual(calculate_pi(10), "3.1415926536")
        self.assertEqual(calculate_pi(0), "3")

    def test_random_helpers(self):
        password = random_password(20, symbols=True)
        self.assertEqual(len(password), 20)
        self.assertIn(random_choice([1, 2, 3]), [1, 2, 3])

    def test_text_helpers(self):
        self.assertEqual(deduplicate([1, 2, 1, 3]), [1, 2, 3])
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(truncate("abcdefgh", 5), "ab...")

    def test_math_helpers(self):
        self.assertEqual(clamp(12, 0, 10), 10)
        self.assertEqual(mean([2, 4, 6]), 4)
        self.assertEqual(median([1, 9, 3]), 3)

    def test_time_helper(self):
        self.assertEqual(days_between(date(2024, 1, 1), date(2024, 1, 4)), 3)

    def test_validators(self):
        self.assertTrue(is_email("dev@example.com"))
        self.assertFalse(is_email("not-an-email"))
        self.assertTrue(is_url("https://example.com"))
        self.assertFalse(is_url("example.com"))


if __name__ == "__main__":
    unittest.main()
