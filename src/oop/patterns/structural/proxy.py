"""Module For Proxy Pattern"""

from abc import ABC, abstractmethod


# Step 1: Define the BankAccount interface
class BankAccount(ABC):
    """Abstract base class for a bank account."""

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit an amount into the bank account."""

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the bank account."""


# Step 2: Implement the Real BankAccount
class RealBankAccount(BankAccount):
    """The real bank account that performs operations."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        """Initialize the bank account with an initial balance."""
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the bank account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the bank account if funds are sufficient."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print(f"Insufficient funds. Current balance: ${self.balance}.")


# Step 3: Implement the Proxy (BankAccountProxy)
class BankAccountProxy(BankAccount):
    """Proxy that controls access to the real bank account."""

    def __init__(self, real_account: RealBankAccount, user_authenticated: bool) -> None:
        """Initialize the proxy with a real bank account and user authentication status."""
        self._real_account = real_account
        self._user_authenticated = user_authenticated

    def deposit(self, amount: float) -> None:
        """Check authentication before allowing deposit."""
        if self._user_authenticated:
            self._real_account.deposit(amount)
        else:
            print("Access denied. User is not authenticated.")

    def withdraw(self, amount: float) -> None:
        """Check authentication before allowing withdrawal."""
        if self._user_authenticated:
            self._real_account.withdraw(amount)
        else:
            print("Access denied. User is not authenticated.")
