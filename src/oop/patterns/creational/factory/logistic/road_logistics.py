"""Road Logistics Module for Factory Design Pattern."""

from src.oop.patterns.creational.factory.logistic.logistics import Logistics
from src.oop.patterns.creational.factory.transport.transport import Transport
from src.oop.patterns.creational.factory.transport.truck_transport import TruckTransport


class RoadLogistics(Logistics):
    """Road Logistics Main Class"""

    def create_transport(self) -> Transport:
        """Create and Return Proper Transport Instance."""
        return TruckTransport()
