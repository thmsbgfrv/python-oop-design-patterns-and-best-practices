"""Test module for bridge.py"""

import unittest
from unittest.mock import MagicMock

from src.oop.patterns.structural.bridge import (
    CreditCardPayment,
    CryptoPayment,
    CryptoProcessor,
    PayPalPayment,
    PayPalProcessor,
    StripeProcessor,
)


class TestPaymentSystem(unittest.TestCase):
    """Test cases for the payment system."""

    def test_credit_card_payment_with_stripe(self) -> None:
        """Test credit card payment processing using Stripe."""
        processor = StripeProcessor()
        credit_card_payment = CreditCardPayment(card_number="1234-5678-9876-5432", processor=processor)
        result = credit_card_payment.pay(100.0)
        self.assertEqual(result, "Using Credit Card 1234-5678-9876-5432: Processing payment of $100.0 via Stripe.")

    def test_paypal_payment_with_paypal(self) -> None:
        """Test PayPal payment processing using PayPal processor."""
        processor = PayPalProcessor()
        paypal_payment = PayPalPayment(paypal_account="user@example.com", processor=processor)
        result = paypal_payment.pay(50.0)
        self.assertEqual(result, "Using PayPal Account user@example.com: Processing payment of $50.0 via PayPal.")

    def test_crypto_payment_with_cryptoapi(self) -> None:
        """Test cryptocurrency payment processing using CryptoAPI."""
        processor = CryptoProcessor()
        crypto_payment = CryptoPayment(wallet_address="abc123wallet", processor=processor)
        result = crypto_payment.pay(200.0)
        self.assertEqual(result, "Using Wallet abc123wallet: Processing payment of $200.0 via CryptoAPI.")

    def test_mocked_processor(self) -> None:
        """Test with mocked payment processor."""
        mock_processor = MagicMock()
        mock_processor.process_payment.return_value = "Mocked payment processing"

        # Credit Card payment with mocked processor
        credit_card_payment = CreditCardPayment(card_number="1234-5678-9876-5432", processor=mock_processor)
        result = credit_card_payment.pay(100.0)
        self.assertEqual(result, "Using Credit Card 1234-5678-9876-5432: Mocked payment processing")
