"""Transport Module"""
from abc import ABC, abstractmethod


class AbstractTransport(ABC):
    """Abstract Transport Abstract Class"""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def deliver(self) -> str:
        """Deliver method for to implementing"""


class TruckTransport(AbstractTransport):
    """Truck Transport Class"""
    # pylint: disable=too-few-public-methods

    def deliver(self) -> str:
        """deliver method for truck"""
        return "Delivering by land in a truck."


class SeaTransport(AbstractTransport):
    """Sear Transport Class"""
    # pylint: disable=too-few-public-methods

    def deliver(self) -> str:
        """deliver method for SeaTransport"""
        return "Delivering by sea in a ship."
