"""Test Transport Module"""

import unittest

from src.oop.patterns.creational.abstract_factory.transports import AbstractTransport, SeaTransport, TruckTransport


class TestTruckTransport(unittest.TestCase):
    """Test Truck Transport Class"""

    truck: TruckTransport

    @classmethod
    def setUpClass(cls) -> None:
        """Test Case Init"""
        cls.truck = TruckTransport()

    def test_object_creation(self) -> None:
        """Test if object created properly"""

        # assert if object is TruckTransport/AbstractTransport
        self.assertTrue(isinstance(self.truck, AbstractTransport))
        self.assertTrue(isinstance(self.truck, TruckTransport))

    def test_deliver(self) -> None:
        """Test Deliver Method Works As Expected"""

        self.assertEqual(self.truck.deliver(), "Delivering by land in a truck.")


class TestSeaTransport(unittest.TestCase):
    """Test Sea Transport Class"""

    sea: SeaTransport

    @classmethod
    def setUpClass(cls) -> None:
        """Test Case Init"""
        cls.sea = SeaTransport()

    def test_object_creation(self) -> None:
        """Test if object created properly"""

        # assert if object is SeaTransport/AbstractTransport
        self.assertTrue(isinstance(self.sea, AbstractTransport))
        self.assertTrue(isinstance(self.sea, SeaTransport))

    def test_deliver(self) -> None:
        """Test Deliver Method Works As Expected"""

        self.assertEqual(self.sea.deliver(), "Delivering by sea in a ship.")
