# singleton.py
"""
Creational Patterns 1: Singleton
"""
from typing import Dict, Optional


class Singleton:
    """
    Singleton Class that ensures only one instance of itself is created.
    """

    __instance: Optional["Singleton"] = None  # Store the singleton instance
    config: Dict[str, str] = {"db": "test"}  # Example configuration dictionary

    def __new__(cls) -> "Singleton":
        """
        This method returns the instance if it has been created before.
        If not, it creates a new instance.
        """
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls) -> "Singleton":
        """Class Method to get singleton instance"""
        return cls()
