"""Adapter Design pattern module"""
from typing import Protocol, runtime_checkable


# Step 1: Define the Target interface for payment processing
@runtime_checkable
class PaymentProcessor(Protocol):
    """Protocol for the Payment Processor interface."""

    def process_payment(self, amount: float) -> str:
        """Method to process payment and return a confirmation message."""


# Step 2: Create the PayPal Payment class
class PayPalPayment:
    """Class representing the PayPal payment processing system."""

    def make_payment(self, amount: float) -> str:
        """Method to process payment through PayPal.

        Args:
            amount (float): The amount to be paid.

        Returns:
            str: Confirmation message from PayPal.
        """
        return f"PayPal: Processed payment of ${amount:.2f}"


# Step 3: Create the Stripe Payment class
class StripePayment:
    """Class representing the Stripe payment processing system."""

    def charge(self, amount: float) -> str:
        """Method to process payment through Stripe.

        Args:
            amount (float): The amount to be charged.

        Returns:
            str: Confirmation message from Stripe.
        """
        return f"Stripe: Charged ${amount:.2f}"


# Step 4: Create the PayPal Adapter
class PayPalAdapter(PaymentProcessor):
    """Adapter for PayPal payment processing."""

    def __init__(self, paypal_payment: PayPalPayment) -> None:
        """Initialize the PayPal adapter.

        Args:
            paypal_payment (PayPalPayment): An instance of PayPalPayment to adapt.
        """
        self._paypal_payment = paypal_payment

    def process_payment(self, amount: float) -> str:
        """Process payment using the PayPal payment method.

        Args:
            amount (float): The amount to be paid.

        Returns:
            str: Confirmation message from the PayPal adapter.
        """
        return self._paypal_payment.make_payment(amount)


# Step 5: Create the Stripe Adapter
class StripeAdapter(PaymentProcessor):
    """Adapter for Stripe payment processing."""

    def __init__(self, stripe_payment: StripePayment) -> None:
        """Initialize the Stripe adapter.

        Args:
            stripe_payment (StripePayment): An instance of StripePayment to adapt.
        """
        self._stripe_payment = stripe_payment

    def process_payment(self, amount: float) -> str:
        """Process payment using the Stripe payment method.

        Args:
            amount (float): The amount to be charged.

        Returns:
            str: Confirmation message from the Stripe adapter.
        """
        return self._stripe_payment.charge(amount)
