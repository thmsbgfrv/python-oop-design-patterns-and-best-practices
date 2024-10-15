"""Module Test for Proxy"""

import unittest
from io import StringIO
from unittest.mock import patch

from src.oop.patterns.structural.proxy import BankAccountProxy, RealBankAccount


class TestBankAccountProxy(unittest.TestCase):
    """Test cases for the Proxy design pattern using BankAccountProxy."""

    @patch("sys.stdout", new_callable=StringIO)
    def test_unauthenticated_access(self, mock_stdout: StringIO) -> None:
        """Test that unauthenticated users cannot deposit or withdraw."""
        real_account = RealBankAccount(initial_balance=100.0)
        proxy = BankAccountProxy(real_account, user_authenticated=False)

        # Attempt to deposit and withdraw as an unauthenticated user
        proxy.deposit(50.0)
        proxy.withdraw(20.0)

        # Check the print output
        self.assertIn("Access denied. User is not authenticated.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticated_access(self, mock_stdout: StringIO) -> None:
        """Test that authenticated users can deposit and withdraw."""
        real_account = RealBankAccount(initial_balance=100.0)
        proxy = BankAccountProxy(real_account, user_authenticated=True)

        # Attempt to deposit and withdraw as an authenticated user
        proxy.deposit(50.0)  # Expected output: Deposited $50.0. New balance is $150.0.
        self.assertEqual(real_account.balance, 150.0)

        proxy.withdraw(20.0)  # Expected output: Withdrew $20.0. New balance is $130.0.
        self.assertEqual(real_account.balance, 130.0)

        # Check the print output
        self.assertIn("Deposited $50.0. New balance is $150.0.", mock_stdout.getvalue())
        self.assertIn("Withdrew $20.0. New balance is $130.0.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticated_access_insufficient_balance(self, mock_stdout: StringIO) -> None:
        """Test that authenticated users can deposit and withdraw."""
        real_account = RealBankAccount(initial_balance=50.0)
        proxy = BankAccountProxy(real_account, user_authenticated=True)

        # Attempt to withdraw from insufficient balance
        proxy.withdraw(70.0)  # Expected output: Insufficient funds. Current balance: 50.0.

        # Check the print output
        self.assertIn("Insufficient funds. Current balance: $50.0.\n", mock_stdout.getvalue())
