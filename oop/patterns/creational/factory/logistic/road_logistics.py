"""Road Logistics Module for Factory Design Pattern."""
from oop.patterns.creational.factory.logistic.logistics import Logistics
from oop.patterns.creational.factory.transport.transport import Transport
from oop.patterns.creational.factory.transport.truck_transport import TruckTransport


class RoadLogistics(Logistics):
    """Road Logistics Main Class"""

    def create_transport(self) -> Transport:
        """Create and Return Proper Transport Instance."""
        return TruckTransport()
