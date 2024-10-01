"""Ship Logistics Module for Factory design Pattern"""
from oop.patterns.creational.factory.logistic.logistics import Logistics
from oop.patterns.creational.factory.transport.ship_transport import ShipTransport
from oop.patterns.creational.factory.transport.transport import Transport


class ShipLogistics(Logistics):
    """Ship Logistics Class."""

    def create_transport(self) -> Transport:
        """Create and Return proper Transport"""
        return ShipTransport()
