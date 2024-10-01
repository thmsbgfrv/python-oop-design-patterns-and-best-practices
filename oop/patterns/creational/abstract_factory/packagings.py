"""Packaging Module"""
from abc import ABC, abstractmethod


class AbstractPackaging(ABC):
    """Abstract Packaging Class"""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def package(self) -> str:
        """Abstract Package Method"""


class BoxPackaging(AbstractPackaging):
    """Box Packaging Class"""
    # pylint: disable=too-few-public-methods

    def package(self) -> str:
        """Implementing Package Method for Box Packaging"""
        return "Packing in a box."


class ContainerPackaging(AbstractPackaging):
    """Container Packaging Class"""
    # pylint: disable=too-few-public-methods

    def package(self) -> str:
        """Implementing Package Method for Container Packaging"""
        return "Packing in a container."
