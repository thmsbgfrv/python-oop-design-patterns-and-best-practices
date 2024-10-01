"""Module of Truck Transport Method of Factory Design Pattern"""

from oop.patterns.creational.factory.transport.transport import Transport


class TruckTransport(Transport):
    """Truck Transport Class to used in Factory design pattern for delivering by Truck Option."""

    # pylint: disable=too-few-public-methods

    def deliver(self) -> str:
        """Return deliver result."""
        return "Delivering by land in a truck."
