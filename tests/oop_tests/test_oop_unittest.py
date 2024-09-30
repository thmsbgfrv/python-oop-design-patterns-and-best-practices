# tests/oop_tests/test_oop_unittest.py

"""
This module contains unit tests for the OOP class.
"""

import unittest

from oop.oop import OOP  # Ensure you import the OOP class


class TestOOP(unittest.TestCase):
    """
    Unit tests for the OOP class methods.
    """

    def setUp(self) -> None:
        """Create an instance of OOP before each test."""
        self.oop_test = OOP()  # Create an instance of OOP

    def test_always_true(self) -> None:
        """Test that the always_true method returns True."""
        self.assertTrue(self.oop_test.always_true())

    def test_always_false(self) -> None:
        """Test that the always_false method returns False."""
        self.assertFalse(self.oop_test.always_false())


if __name__ == "__main__":
    unittest.main()
