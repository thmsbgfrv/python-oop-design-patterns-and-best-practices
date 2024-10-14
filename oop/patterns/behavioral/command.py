"""Module for demonstrating the Command Pattern in an online order system."""

from abc import ABC, abstractmethod


class Order:
    """Represents an order in the online system."""

    def place(self) -> None:
        """Place the order."""
        print("Order has been placed.")

    def cancel(self) -> None:
        """Cancel the order."""
        print("Order has been canceled.")


class Command(ABC):
    """Command interface for executing commands."""

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""

    @abstractmethod
    def undo(self) -> None:
        """Undo the command."""


class PlaceOrderCommand(Command):
    """Command to place an order."""

    def __init__(self, order: Order) -> None:
        self.order = order

    def execute(self) -> None:
        """Place the order."""
        self.order.place()

    def undo(self) -> None:
        """Undo the place order action by canceling the order."""
        self.order.cancel()


class CancelOrderCommand(Command):
    """Command to cancel an order."""

    def __init__(self, order: Order) -> None:
        self.order = order

    def execute(self) -> None:
        """Cancel the order."""
        self.order.cancel()

    def undo(self) -> None:
        """Undo the cancel order action by placing the order."""
        self.order.place()


class OrderInvoker:
    """Invoker that triggers the commands."""

    def __init__(self) -> None:
        self.commands: list[Command] = []
        self.history: list[Command] = []

    def set_command(self, command: Command) -> None:
        """Set a command to be executed."""
        self.commands.append(command)

    def press_button(self) -> None:
        """Execute the last command set."""
        if self.commands:
            command = self.commands.pop()
            command.execute()
            self.history.append(command)

    def press_undo(self) -> None:
        """Undo the last command executed."""
        if self.history:
            command = self.history.pop()
            command.undo()
