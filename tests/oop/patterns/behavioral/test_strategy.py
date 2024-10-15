"""
Test Module for Strategy Pattern

This module contains unit tests for the Strategy design pattern,
capturing and verifying print statements for payment processing.
"""

import unittest
from io import StringIO
from unittest.mock import patch

from src.oop.patterns.behavioral.strategy import BankTransferPayment, CreditCardPayment, PaymentContext, PayPalPayment


class TestStrategyPattern(unittest.TestCase):
    """Unit tests for the Strategy Pattern implementation."""

    @patch("sys.stdout", new_callable=StringIO)
    def test_credit_card_payment(self, mock_stdout: StringIO) -> None:
        """Test payment with a credit card strategy."""
        strategy = CreditCardPayment("1111-2222-3333-4444")
        context = PaymentContext(strategy)
        context.process_payment(150.0)

        # Assert print output
        self.assertIn("Processing credit card payment of $150.0 using card 1111-2222-3333-4444", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_paypal_payment(self, mock_stdout: StringIO) -> None:
        """Test payment with a PayPal strategy."""
        strategy = PayPalPayment("user@paypal.com")
        context = PaymentContext(strategy)
        context.process_payment(250.0)

        # Assert print output
        self.assertIn(
            "Processing PayPal payment of $250.0 using PayPal account user@paypal.com", mock_stdout.getvalue()
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_bank_transfer_payment(self, mock_stdout: StringIO) -> None:
        """Test payment with a bank transfer strategy."""
        strategy = BankTransferPayment("AB123456789")
        context = PaymentContext(strategy)
        context.process_payment(350.0)

        # Assert print output
        self.assertIn("Processing bank transfer of $350.0 to account AB123456789", mock_stdout.getvalue())
