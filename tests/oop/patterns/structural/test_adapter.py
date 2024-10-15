"""Tests of Adapter.py"""

import unittest

from src.oop.patterns.structural.adapter import (
    PaymentProcessor,
    PayPalAdapter,
    PayPalPayment,
    StripeAdapter,
    StripePayment,
)


class TestPaymentAdapter(unittest.TestCase):
    """Test case for the Payment Adapter design pattern implementation."""

    def test_paypal_payment(self) -> None:
        """Test the PayPal payment processing."""
        paypal_payment = PayPalPayment()
        adapter: PaymentProcessor = PayPalAdapter(paypal_payment)
        self.assertEqual(adapter.process_payment(50.0), "PayPal: Processed payment of $50.00")

    def test_stripe_payment(self) -> None:
        """Test the Stripe payment processing."""
        stripe_payment = StripePayment()
        adapter: PaymentProcessor = StripeAdapter(stripe_payment)
        self.assertEqual(adapter.process_payment(75.0), "Stripe: Charged $75.00")
