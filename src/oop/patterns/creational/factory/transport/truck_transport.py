"""Module of Truck Transport Method of Factory Design Pattern"""

from src.oop.patterns.creational.factory.transport.transport import Transport


class TruckTransport(Transport):
    """Truck Transport Class to used in Factory design pattern for delivering by Truck Option."""

    def deliver(self) -> str:
        """Return deliver result."""
        return "Delivering by land in a truck."
