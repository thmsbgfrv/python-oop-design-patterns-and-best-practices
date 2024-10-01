"""Module of Ship Transport Method tests of Factory Design Pattern"""

from oop.patterns.creational.factory.transport.ship_transport import ShipTransport
from oop.patterns.creational.factory.transport.transport import Transport


class TestShipTransport:
    """Test cases of ShipTransport"""

    def test_ship_transport_object_creation(self) -> None:
        """Test if Ship Transport object can be created."""
        ship: ShipTransport = ShipTransport()

        # assert if object is instance of ShipTransport
        assert isinstance(ship, ShipTransport), f"Expected {ship} to be instance of {ShipTransport.__name__}"

    def test_ship_transport_object_is_instance_of_transport(self) -> None:
        """Test if ship object is also instance of Transport abstract class."""
        ship: ShipTransport = ShipTransport()

        # assert if object is instance of ShipTransport
        assert isinstance(ship, Transport), f'Expected {ship} to be instance of {Transport.__name__}'

    def test_ship_transport_deliver(self) -> None:
        """Test if ship transport can deliver, and result."""
        ship: ShipTransport = ShipTransport()

        # assert if deliver result as expected
        assert ship.deliver() == "Delivering by sea in a ship."
