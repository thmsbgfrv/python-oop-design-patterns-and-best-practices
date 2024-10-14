"""Module for demonstrating the State Pattern in a user account system."""

from abc import ABC, abstractmethod


class AccountState(ABC):
    """Abstract base class for user account states."""

    @abstractmethod
    def activate(self) -> None:
        """Activate the account."""

    @abstractmethod
    def suspend(self) -> None:
        """Suspend the account."""

    @abstractmethod
    def deactivate(self) -> None:
        """Deactivate the account."""


class ActiveState(AccountState):
    """Concrete state representing an active account."""

    def activate(self) -> None:
        """Account is already active."""
        print("The account is already active.")

    def suspend(self) -> None:
        """Suspend the active account."""
        print("Suspending the account.")

    def deactivate(self) -> None:
        """Deactivate the active account."""
        print("Deactivating the account.")


class SuspendedState(AccountState):
    """Concrete state representing a suspended account."""

    def activate(self) -> None:
        """Activate the suspended account."""
        print("Activating the suspended account.")

    def suspend(self) -> None:
        """Account is already suspended."""
        print("The account is already suspended.")

    def deactivate(self) -> None:
        """Deactivate the suspended account."""
        print("Deactivating the suspended account.")


class InactiveState(AccountState):
    """Concrete state representing an inactive account."""

    def activate(self) -> None:
        """Activate the inactive account."""
        print("Activating the inactive account.")

    def suspend(self) -> None:
        """Cannot suspend an inactive account."""
        print("Cannot suspend an inactive account.")

    def deactivate(self) -> None:
        """Account is already inactive."""
        print("The account is already inactive.")


class UserAccount:
    """Context class that holds a reference to a UserAccountState."""

    def __init__(self) -> None:
        """Initialize the user account with the active state."""
        self.state: AccountState = ActiveState()

    def set_state(self, state: AccountState) -> None:
        """Set a new state for the user account."""
        self.state = state

    def activate(self) -> None:
        """Activate the current state."""
        self.state.activate()
        if isinstance(self.state, InactiveState):
            self.set_state(ActiveState())

    def suspend(self) -> None:
        """Suspend the current state."""
        self.state.suspend()
        if isinstance(self.state, ActiveState):
            self.set_state(SuspendedState())

    def deactivate(self) -> None:
        """Deactivate the current state."""
        self.state.deactivate()
        if isinstance(self.state, (ActiveState, SuspendedState)):  # Merged the conditions
            self.set_state(InactiveState())
