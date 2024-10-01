""" Logistics Module Tests to test Logistics Module """
import unittest

from oop.patterns.creational.abstract_factory.logistics import (
    AbstractFactory,
    RoadLogisticsFactory,
    SeaLogisticsFactory,
)
from oop.patterns.creational.abstract_factory.packagings import AbstractPackaging, BoxPackaging, ContainerPackaging
from oop.patterns.creational.abstract_factory.transports import AbstractTransport, SeaTransport, TruckTransport


class TestRoadLogistics(unittest.TestCase):
    """Test Road Logistics Class Methods"""

    road_logistic: RoadLogisticsFactory

    @classmethod
    def setUpClass(cls) -> None:
        """setup instance for testing"""
        cls.road_logistic = RoadLogisticsFactory()

    def test_road_logistics_instance_created_properly(self) -> None:
        """Test if road_logistic created properly and inherited from expected class"""

        self.assertTrue(isinstance(self.road_logistic, RoadLogisticsFactory))
        self.assertTrue(isinstance(self.road_logistic, AbstractFactory))

    def test_create_transport(self) -> None:
        """ Test if create_transport returns TruckTransport(Transport)"""
        truck: AbstractTransport = self.road_logistic.create_transport()

        # assert if truck is AbstractTransport and TruckTransport
        self.assertTrue(isinstance(truck, TruckTransport))
        self.assertTrue(isinstance(truck, AbstractTransport))

        # assert additionally deliver method here
        self.assertEqual(truck.deliver(), 'Delivering by land in a truck.')

    def test_create_packaging(self) -> None:
        """Test if create_packaging return BoxPackaging"""
        package: AbstractPackaging = self.road_logistic.create_packaging()

        # assert if package is AbstractPackaging/BoxPackaging
        self.assertTrue(isinstance(package, BoxPackaging))
        self.assertTrue(isinstance(package, AbstractPackaging))

        # assert additionally package method here
        self.assertEqual(package.package(), 'Packing in a box.')


class TestSeaLogistics(unittest.TestCase):
    """Test Sea Logistics Class Methods"""

    sea_logistic: SeaLogisticsFactory

    @classmethod
    def setUpClass(cls) -> None:
        """setup instance for testing"""
        cls.sea_logistic = SeaLogisticsFactory()

    def test_sea_logistics_instance_created_properly(self) -> None:
        """Test if sea_logistic created properly and inherited from expected class"""

        # assert True if it is expected
        self.assertTrue(isinstance(self.sea_logistic, SeaLogisticsFactory))
        self.assertTrue(isinstance(self.sea_logistic, AbstractFactory))

    def test_create_transport(self) -> None:
        """ Test if create_transport returns TruckTransport(Transport)"""
        sea: AbstractTransport = self.sea_logistic.create_transport()

        # assert if truck is AbstractTransport and TruckTransport
        self.assertTrue(isinstance(sea, SeaTransport))
        self.assertTrue(isinstance(sea, AbstractTransport))

        # assert additionally deliver method here
        self.assertEqual(sea.deliver(), 'Delivering by sea in a ship.')

    def test_create_packaging(self) -> None:
        """Test if create_packaging return BoxPackaging"""
        container: AbstractPackaging = self.sea_logistic.create_packaging()

        # assert if package is AbstractPackaging/Container Packaging
        self.assertTrue(isinstance(container, ContainerPackaging))
        self.assertTrue(isinstance(container, AbstractPackaging))

        # assert additionally package method here
        self.assertEqual(container.package(), 'Packing in a container.')
