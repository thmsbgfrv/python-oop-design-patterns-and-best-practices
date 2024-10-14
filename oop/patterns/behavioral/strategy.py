"""
Module Of Strategy Pattern

This module contains the implementation of the Strategy design pattern, where
a context can choose among different algorithms or strategies at runtime.
"""

from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):
    """Abstract base class for payment strategies."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process the payment for a given amount."""


# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentStrategy):
    """Payment strategy for paying by credit card."""

    def __init__(self, card_number: str) -> None:
        self._card_number = card_number

    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount} using card {self._card_number}")


# Concrete Strategy 2: PayPal Payment
class PayPalPayment(PaymentStrategy):
    """Payment strategy for paying via PayPal."""

    def __init__(self, email: str) -> None:
        self._email = email

    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount} using PayPal account {self._email}")


# Concrete Strategy 3: Bank Transfer Payment
class BankTransferPayment(PaymentStrategy):
    """Payment strategy for paying via bank transfer."""

    def __init__(self, account_number: str) -> None:
        self._account_number = account_number

    def pay(self, amount: float) -> None:
        print(f"Processing bank transfer of ${amount} to account {self._account_number}")


# Context
class PaymentContext:
    """The context class that uses a payment strategy to process payments."""

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Set or change the payment strategy at runtime."""
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        """Process the payment using the current strategy."""
        self._strategy.pay(amount)
