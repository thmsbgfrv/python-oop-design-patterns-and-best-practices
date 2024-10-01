# singleton.py
"""
Creational Patterns 1: SingletonNaive, Metaclass
"""
from typing import Any, Dict, Type


class Singleton(type):
    """I am using metaclass implemenation for creating Singleton"""
    # pylint: disable=too-few-public-methods
    __instances: Dict[Type[Any], Any] = {}

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        """Create Class At first call then return needed class"""
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    @classmethod
    def reset(mcs) -> None:
        """Reset the instances to allow re-creation of singletons."""
        mcs.__instances.clear()


class SingletonNaive(metaclass=Singleton):
    """
    Singleton Class that ensures only one instance of itself is created.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self.name = name


class SingletonNaive2(metaclass=Singleton):
    """
    Singleton Class that ensures only one instance of itself is created.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self.name = name
