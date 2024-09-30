# tests/test_oop_test.py

"""
This module contains unit tests for the OOP class.
"""

import pytest

from oop.oop import OOP


class TestOOP:
    """
    Test cases for the OOP class methods.
    """

    @pytest.fixture
    def oop_test(self) -> OOP:
        """
        Fixture to create an instance of the OOP class for testing.
        """
        return OOP()

    def test_always_true(self, oop_test: OOP) -> None:
        """
        Test that the always_true method returns True.
        """
        assert oop_test.always_true() is True

    def test_always_false(self, oop_test: OOP) -> None:
        """
        Test that the always_false method returns False.
        """
        assert oop_test.always_false() is False
