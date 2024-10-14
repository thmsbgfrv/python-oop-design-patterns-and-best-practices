"""Module implementing the Template Method Pattern for user actions in a web application."""

from abc import ABC, abstractmethod


class UserAction(ABC):
    """Abstract base class for user actions."""

    def perform_action(self) -> None:
        """Template method that defines the algorithm for performing an action."""
        self.login()
        self.do_action()
        self.logout()

    @abstractmethod
    def do_action(self) -> None:
        """Abstract method to perform the specific action. Must be implemented by subclasses."""

    def login(self) -> None:
        """Simulate user login."""
        print("Logging in...")

    def logout(self) -> None:
        """Simulate user logout."""
        print("Logging out...")


class AdminAction(UserAction):
    """Concrete class for admin user actions."""

    def do_action(self) -> None:
        """Perform admin-specific action."""
        print("Performing admin action...")


class RegularUserAction(UserAction):
    """Concrete class for regular user actions."""

    def do_action(self) -> None:
        """Perform regular user-specific action."""
        print("Performing regular user action...")
