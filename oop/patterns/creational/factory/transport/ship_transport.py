"""Module of Ship Transport Method of Factory Design Pattern"""
from oop.patterns.creational.factory.transport.transport import Transport


class ShipTransport(Transport):
    """ShipTransport class to handle ship transports for Factory design pattern."""

    def deliver(self) -> str:
        """Return deliver result."""
        return "Delivering by sea in a ship."
