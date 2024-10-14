"""Module for Mediator Pattern in a Chat Application"""

from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    """Abstract Mediator class."""

    @abstractmethod
    def send(self, message: str, colleague: 'Colleague') -> None:
        """Send a message from one colleague to others."""


class Colleague(ABC):
    """Abstract Colleague class."""

    def __init__(self, mediator: Mediator) -> None:
        """Initialize the colleague with a mediator."""
        self.mediator: Mediator = mediator

    @abstractmethod
    def send(self, message: str) -> None:
        """Send a message through the mediator."""

    @abstractmethod
    def receive(self, message: str) -> None:
        """Receive a message from the mediator."""


class ChatRoom(Mediator):
    """Concrete Mediator class for managing chat interactions."""

    def __init__(self) -> None:
        """Initialize the chat room with a list of colleagues."""
        self.colleagues: List[Colleague] = []

    def add_colleague(self, colleague: Colleague) -> None:
        """Add a colleague to the chat room."""
        self.colleagues.append(colleague)

    def send(self, message: str, colleague: Colleague) -> None:
        """Send a message from one colleague to all others."""
        for c in self.colleagues:
            if c != colleague:  # Do not send the message back to the sender
                c.receive(message)


class User(Colleague):
    """Concrete Colleague class representing a user in the chat room."""

    def __init__(self, name: str, mediator: Mediator) -> None:
        """Initialize the user with a name and a mediator."""
        super().__init__(mediator)
        self.name: str = name

    def send(self, message: str) -> None:
        """Send a message to the chat room."""
        print(f"{self.name}: Sending message: {message}")
        self.mediator.send(message, self)

    def receive(self, message: str) -> None:
        """Receive a message from the chat room."""
        print(f"{self.name}: Received message: {message}")
