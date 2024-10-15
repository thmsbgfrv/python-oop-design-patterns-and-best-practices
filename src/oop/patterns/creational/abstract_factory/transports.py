"""Transport Module"""

from abc import ABC, abstractmethod


class AbstractTransport(ABC):
    """Abstract Transport Abstract Class"""

    @abstractmethod
    def deliver(self) -> str:
        """Deliver method for to implementing"""


class TruckTransport(AbstractTransport):
    """Truck Transport Class"""

    def deliver(self) -> str:
        """deliver method for truck"""
        return "Delivering by land in a truck."


class SeaTransport(AbstractTransport):
    """Sear Transport Class"""

    def deliver(self) -> str:
        """deliver method for SeaTransport"""
        return "Delivering by sea in a ship."
