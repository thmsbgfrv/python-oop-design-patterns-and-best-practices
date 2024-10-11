"""Module of bridge"""
from abc import ABC, abstractmethod
from typing import Protocol


# Step 1: Define the Payment Processor interface (Implementation)
class PaymentProcessor(Protocol):
    """Abstract class for processing payments."""

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Process a payment of the given amount."""


# Step 2: Implement Concrete Payment Processors
class StripeProcessor(PaymentProcessor):
    """Concrete processor that uses Stripe to process payments."""

    def process_payment(self, amount: float) -> str:
        """Process the payment using Stripe."""
        return f"Processing payment of ${amount} via Stripe."


class PayPalProcessor(PaymentProcessor):
    """Concrete processor that uses PayPal to process payments."""

    def process_payment(self, amount: float) -> str:
        """Process the payment using PayPal."""
        return f"Processing payment of ${amount} via PayPal."


class CryptoProcessor(PaymentProcessor):
    """Concrete processor that uses a cryptocurrency API to process payments."""

    def process_payment(self, amount: float) -> str:
        """Process the payment using a cryptocurrency API."""
        return f"Processing payment of ${amount} via CryptoAPI."


# Step 3: Define the Payment Method abstraction
class PaymentMethod(ABC):
    """Abstract class for different payment methods."""

    def __init__(self, processor: PaymentProcessor) -> None:
        """Initialize the payment method with a specific processor."""
        self.processor = processor

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Pay a specific amount."""


# Step 4: Implement Concrete Payment Methods
class CreditCardPayment(PaymentMethod):
    """Concrete payment method for credit cards."""

    def __init__(self, card_number: str, processor: PaymentProcessor) -> None:
        """Initialize the credit card payment method with card details and processor."""
        super().__init__(processor)
        self.card_number = card_number

    def pay(self, amount: float) -> str:
        """Pay the given amount using the credit card."""
        return f"Using Credit Card {self.card_number}: {self.processor.process_payment(amount)}"


class PayPalPayment(PaymentMethod):
    """Concrete payment method for PayPal."""

    def __init__(self, paypal_account: str, processor: PaymentProcessor) -> None:
        """Initialize the PayPal payment method with PayPal account details and processor."""
        super().__init__(processor)
        self.paypal_account = paypal_account

    def pay(self, amount: float) -> str:
        """Pay the given amount using PayPal."""
        return f"Using PayPal Account {self.paypal_account}: {self.processor.process_payment(amount)}"


class CryptoPayment(PaymentMethod):
    """Concrete payment method for cryptocurrency."""

    def __init__(self, wallet_address: str, processor: PaymentProcessor) -> None:
        """Initialize the crypto payment method with wallet details and processor."""
        super().__init__(processor)
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        """Pay the given amount using cryptocurrency."""
        return f"Using Wallet {self.wallet_address}: {self.processor.process_payment(amount)}"
