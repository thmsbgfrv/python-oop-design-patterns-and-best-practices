"""Module for state tests"""
import unittest
from unittest.mock import MagicMock, patch

from oop.patterns.behavioral.state import UserAccount


class TestUserAccount(unittest.TestCase):
    """Tests for the UserAccount class using the State Pattern."""

    def setUp(self) -> None:
        """Set up a UserAccount instance for testing."""
        self.user_account = UserAccount()

    @patch('builtins.print')
    def test_activate_active_account(self, mock_print: MagicMock) -> None:
        """Test activating an already active account."""
        self.user_account.activate()
        mock_print.assert_called_once_with("The account is already active.")

    @patch('builtins.print')
    def test_suspend_active_account(self, mock_print: MagicMock) -> None:
        """Test suspending an active account."""
        self.user_account.suspend()
        mock_print.assert_called_once_with("Suspending the account.")

    @patch('builtins.print')
    def test_activate_suspended_account(self, mock_print: MagicMock) -> None:
        """Test activating a suspended account."""
        self.user_account.suspend()  # First suspend to change the state
        self.user_account.activate()
        mock_print.assert_called_with("Activating the suspended account.")

    @patch('builtins.print')
    def test_deactivate_active_account(self, mock_print: MagicMock) -> None:
        """Test deactivating an active account."""
        self.user_account.deactivate()
        mock_print.assert_called_with("Deactivating the account.")

    @patch('builtins.print')
    def test_deactivate_suspended_account(self, mock_print: MagicMock) -> None:
        """Test deactivating a suspended account."""
        self.user_account.suspend()  # Change to suspended state
        self.user_account.deactivate()
        mock_print.assert_called_with("Deactivating the suspended account.")

    @patch('builtins.print')
    def test_deactivate_inactive_account(self, mock_print: MagicMock) -> None:
        """Test deactivating an inactive account."""
        self.user_account.deactivate()  # First deactivate to change to inactive state
        self.user_account.deactivate()
        mock_print.assert_called_with("The account is already inactive.")

    @patch('builtins.print')
    def test_suspend_inactive_account(self, mock_print: MagicMock) -> None:
        """Test suspending an inactive account."""
        self.user_account.deactivate()  # Change to inactive state
        self.user_account.suspend()
        mock_print.assert_called_with("Cannot suspend an inactive account.")
