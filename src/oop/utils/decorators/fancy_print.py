"""Fancy Print Decorator Module"""

from functools import wraps
from typing import Any, Callable, TypeVar

# Create a type variable that can be any callable.
F = TypeVar("F", bound=Callable[..., Any])


def fancy_print(func: F) -> F:
    """fancy_print decorator"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """wrapper of fancy_wrapper"""
        print("\n", "_" * 45, func.__name__, "_" * 45, "\n")
        return func(*args, **kwargs)

    return wrapper  # type: ignore
