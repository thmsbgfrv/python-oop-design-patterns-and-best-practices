# singleton.py
"""
Creational Patterns 1: SingletonNaiveThreadSafe Metaclass
"""
from threading import Lock
from typing import Any, Dict, Type


class Singleton(type):
    """I am using metaclass approach for creating Singleton Naive Thread Safe Class"""
    # pylint: disable=too-few-public-methods
    __instances: Dict[Type[Any], Any] = {}
    __lock: Lock = Lock()

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        """Create Class At first call then return needed class"""
        with cls.__lock:
            if cls not in cls.__instances:
                cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    @classmethod
    def reset(mcs) -> None:
        """Reset the instances to allow re-creation of singletons."""
        with mcs.__lock:
            mcs.__instances.clear()


class SingletonNaiveThreadSafe(metaclass=Singleton):
    """
    SingletonNaiveThreadSafe Class that ensures only one instance of itself is created.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self.name = name


class SingletonNaiveThreadSafe2(metaclass=Singleton):
    """
    SingletonNaiveThreadSafe2 Class that ensures only one instance of itself is created.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self.name = name
