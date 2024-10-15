"""Module of Truck Transport  Tests Method of Factory Design Pattern"""

from src.oop.patterns.creational.factory.transport.transport import Transport
from src.oop.patterns.creational.factory.transport.truck_transport import TruckTransport


class TestTruckTransport:
    """Test Truck Transport Class"""

    def test_truck_object_creation(self) -> None:
        """Test if track transport object can be created."""
        truck: TruckTransport = TruckTransport()

        # assert if object is instance of TruckTransport
        assert isinstance(truck, TruckTransport), f"Expected {truck} to be instance of {TruckTransport.__name__}"

    def test_truck_object_is_instance_of_transport(self) -> None:
        """Test if track transport object can be created."""
        truck: TruckTransport = TruckTransport()

        # assert if object is instance of TruckTransport
        assert isinstance(truck, Transport), f"Expected {truck} to be instance of {Transport.__name__}"

    def test_truck_deliver(self) -> None:
        """Test if track can deliver and result of deliver."""
        truck: TruckTransport = TruckTransport()

        # assert if truck deliver result equal expected
        assert truck.deliver() == "Delivering by land in a truck."
