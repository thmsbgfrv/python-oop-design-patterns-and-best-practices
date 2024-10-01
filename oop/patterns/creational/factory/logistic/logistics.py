""" Logistic Abstract Module for to use in Factory Design Pattern"""
from abc import ABC, abstractmethod

from oop.patterns.creational.factory.transport.transport import Transport


class Logistics(ABC):
    """Logistics Abstract Class"""

    @abstractmethod
    def create_transport(self) -> Transport:
        """Return Proper Transport Object When called, abstract method"""

    def plan_delivery(self) -> str:
        """Call the factory method to create a Transport Object."""
        transport: Transport = self.create_transport()
        return f"Logistics: {transport.deliver()}"
