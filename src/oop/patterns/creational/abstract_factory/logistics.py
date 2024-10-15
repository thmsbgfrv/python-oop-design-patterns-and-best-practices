"""Logistics Module"""

from abc import ABC, abstractmethod

from src.oop.patterns.creational.abstract_factory.packagings import AbstractPackaging, BoxPackaging, ContainerPackaging
from src.oop.patterns.creational.abstract_factory.transports import AbstractTransport, SeaTransport, TruckTransport


class AbstractFactory(ABC):
    """AbstractFactory to create proper logistics"""

    @abstractmethod
    def create_transport(self) -> AbstractTransport:
        """Create Transport Abstract Method"""

    @abstractmethod
    def create_packaging(self) -> AbstractPackaging:
        """Create Packaging Abstract Method"""


class RoadLogisticsFactory(AbstractFactory):
    """Road Logistics Factory Class"""

    def create_transport(self) -> AbstractTransport:
        """Create Truck Transport and Return"""
        return TruckTransport()

    def create_packaging(self) -> AbstractPackaging:
        """Create Box Packaging and Return"""
        return BoxPackaging()


class SeaLogisticsFactory(AbstractFactory):
    """Sea Logistics Factory Class"""

    def create_transport(self) -> AbstractTransport:
        """Create Sea Transport and Return"""
        return SeaTransport()

    def create_packaging(self) -> AbstractPackaging:
        """Create Container Transport and Return"""
        return ContainerPackaging()
