"""Test Module for Ship Logistics for Factory Design Pattern"""
from oop.patterns.creational.factory.logistic.logistics import Logistics
from oop.patterns.creational.factory.logistic.ship_logistics import ShipLogistics
from oop.patterns.creational.factory.transport.ship_transport import ShipTransport
from oop.patterns.creational.factory.transport.transport import Transport


class TestShipTransport:
    """Tests for Ship Transport Class"""

    ship_logistic: ShipLogistics

    @classmethod
    def setup_class(cls) -> None:
        """Setup class for init value."""
        cls.ship_logistic = ShipLogistics()

    def test_ship_logistics_object_creation(self) -> None:
        """Test if ship logistic instance can create."""

        # assert true if instance created properly
        assert isinstance(self.ship_logistic, ShipLogistics), \
            f"Expected {self.ship_logistic} is to be created from {ShipLogistics.__name__}"

    def test_ship_logistics_object_inherited_properly(self) -> None:
        """Test if ship logistics instance inherited from Logistics."""

        # assert true if instance inherited from proper class
        assert isinstance(self.ship_logistic, Logistics), \
            f"Expected {self.ship_logistic} is inhertied from {Logistics.__name__}"

    def test_ship_logistics_can_create_transport(self) -> None:
        """Check if Transport can create through create_transport method"""
        transport: Transport = self.ship_logistic.create_transport()

        # assert true if transport is Transport Object
        assert isinstance(transport, Transport), \
            f"Expected {transport} is to be {Transport.__name__}"

    def test_ship_logistics_can_create_ship_transport(self) -> None:
        """Check if logistics can create ShipTransport."""
        ship: Transport = self.ship_logistic.create_transport()

        # assert true if ship is ShipTransport instance
        assert isinstance(ship, ShipTransport), f"Expected {ship} is to be instance of {ShipTransport.__name__}"

    def test_ship_logistics_can_plan_delivery(self) -> None:
        """Test if ShipLogistics can plan delivery properly."""
        result: str = self.ship_logistic.plan_delivery()

        # assert true if plan delivery return expected result
        assert result == 'Logistics: Delivering by sea in a ship.'
