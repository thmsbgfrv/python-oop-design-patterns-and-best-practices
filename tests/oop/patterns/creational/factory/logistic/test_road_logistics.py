"""Road Logistics Tests for Factory Design Pattern"""

from src.oop.patterns.creational.factory.logistic.logistics import Logistics
from src.oop.patterns.creational.factory.logistic.road_logistics import RoadLogistics
from src.oop.patterns.creational.factory.transport.transport import Transport
from src.oop.patterns.creational.factory.transport.truck_transport import TruckTransport


class TestRoadLogistics:
    """Test Cases For Road Logistics."""

    road_logistic: RoadLogistics

    @classmethod
    def setup_class(cls) -> None:
        """Setup Class When Test Initialized"""
        cls.road_logistic = RoadLogistics()

    def test_road_logistic_object_creation(self) -> None:
        """Test if object created as expected instance."""

        # assert if road_logistics is instance of proper class
        assert isinstance(
            self.road_logistic, RoadLogistics
        ), f"Expected {self.road_logistic} to be instance of {RoadLogistics.__name__}."

    def test_road_logistic_object_is_instance_of_logistics_abstract(self) -> None:
        """Test if object inherits from Logistics abstract class"""

        # assert if road_logistics is inherited from proper class
        assert isinstance(
            self.road_logistic, Logistics
        ), f"Expected {self.road_logistic} to be instance of {Logistics.__name__}."

    def test_road_logistic_create_transport_return_transport(self) -> None:
        """Test if create_transport method returns transport object"""
        transport: Transport = self.road_logistic.create_transport()

        # assert if create_transport creates transport properly
        assert isinstance(transport, Transport), f"Expected {transport} to be instance of {Transport.__name__}"

    def test_road_logistic_create_truck_transport_return_transport(self) -> None:
        """Test if create_transport method returns transport object"""
        truck: Transport = self.road_logistic.create_transport()

        # assert if create_transport creates truck transport properly
        assert isinstance(truck, TruckTransport), f"Expected {truck} to be instance of {TruckTransport.__name__}"

    def test_road_logistics_plan_delivery(self) -> None:
        """Test If Road Logistics plan_delivery works as expected."""
        result = self.road_logistic.plan_delivery()

        # assert true if plan delivery works as expected
        assert result == "Logistics: Delivering by land in a truck."
