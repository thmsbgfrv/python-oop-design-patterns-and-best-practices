"""Ship Logistics Module for Factory design Pattern"""

from src.oop.patterns.creational.factory.logistic.logistics import Logistics
from src.oop.patterns.creational.factory.transport.ship_transport import ShipTransport
from src.oop.patterns.creational.factory.transport.transport import Transport


class ShipLogistics(Logistics):
    """Ship Logistics Class."""

    def create_transport(self) -> Transport:
        """Create and Return proper Transport"""
        return ShipTransport()
