"""Template tests module"""

import unittest
from unittest.mock import MagicMock, patch

from src.oop.patterns.behavioral.template import AdminAction, RegularUserAction


class TestTemplateMethodPattern(unittest.TestCase):
    """Test cases for the Template Method Pattern."""

    @patch("builtins.print")
    def test_admin_action(self, mock_print: MagicMock) -> None:
        """Test the admin action."""
        admin_action = AdminAction()
        admin_action.perform_action()

        # Check the expected calls to print
        mock_print.assert_any_call("Logging in...")
        mock_print.assert_any_call("Performing admin action...")
        mock_print.assert_any_call("Logging out...")

        # Ensure the correct number of calls
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_regular_user_action(self, mock_print: MagicMock) -> None:
        """Test the regular user action."""
        user_action = RegularUserAction()
        user_action.perform_action()

        # Check the expected calls to print
        mock_print.assert_any_call("Logging in...")
        mock_print.assert_any_call("Performing regular user action...")
        mock_print.assert_any_call("Logging out...")

        # Ensure the correct number of calls
        self.assertEqual(mock_print.call_count, 3)
