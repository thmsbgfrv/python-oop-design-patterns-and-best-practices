"""Module of Transport Abstract Method of Factory Design Pattern"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """Transport AbstractClass for using in factory design pattern"""

    @abstractmethod
    def deliver(self) -> str:
        """Abstract Deliver Method must override in transports"""
