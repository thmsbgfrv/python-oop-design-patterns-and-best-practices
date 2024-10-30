"""
Advanced Python Decorators Examples

This module includes examples of:
1. A simple decorator without arguments.
2. A function-based decorator with an argument.
3. A class-based decorator with two arguments.
4. Applying decorators to class methods and using a class as a singleton.
"""

from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")


# 1. Simple Decorator
def log_start_end(func: Callable[..., T]) -> Callable[..., T]:
    """Decorator that logs when a function starts and ends.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending {func.__name__}")
        return result

    return wrapper


@log_start_end
def say_hello() -> None:
    """Function to demonstrate the log_start_end decorator."""
    print("Hello!")


# 2. Function-Based Decorator with an Argument
def repeat(times: int) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator that repeats a function call a specified number of times.

    Args:
        times: The number of times to repeat the function call.

    Returns:
        The decorated function that repeats its execution.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            result = None
            for i in range(times):
                print(f"Run {i + 1} of {times}")
                result = func(*args, **kwargs)
            return result  # type: ignore

        return wrapper

    return decorator


@repeat(3)
def greet() -> None:
    """Function to demonstrate the repeat decorator."""
    print("Hello!")


# 3. Class-Based Decorator with Two Arguments
class AddPrefixSuffix:
    """Decorator class that adds a prefix and suffix to the function output.

    Args:
        prefix: The string to add before the function output.
        suffix: The string to add after the function output.
    """

    def __init__(self, prefix: str, suffix: str) -> None:
        self.prefix = prefix
        self.suffix = suffix

    def __call__(self, func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            print(self.prefix, end="")
            result = func(*args, **kwargs)
            print(self.suffix)
            return result

        return wrapper


@AddPrefixSuffix(prefix=">>> ", suffix=" <<<")
def display_message() -> None:
    """Function to demonstrate the AddPrefixSuffix decorator."""
    print("Decorated Message", end="")


# 4. Using Decorators on Class Methods
class Greeter:
    """Class demonstrating usage of various decorators on methods."""

    @log_start_end
    def greet(self) -> None:
        """Method to demonstrate the log_start_end decorator on a method."""
        print("Hello from the Greeter class!")

    @repeat(2)
    def wave(self) -> None:
        """Method to demonstrate the repeat decorator on a method."""
        print("Waving!")

    @AddPrefixSuffix(prefix="** ", suffix=" **")
    def cheer(self) -> None:
        """Method to demonstrate the AddPrefixSuffix decorator on a method."""
        print("Go Team!", end="")


# 5. Class Decorator Example - Singleton
def singleton(cls: type) -> Callable[..., Any]:
    """Decorator that makes a class a singleton (only one instance).

    Args:
        cls: The class to be decorated as a singleton.

    Returns:
        A function that returns the singleton instance.
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Database:
    """Database class demonstrating a singleton pattern."""

    def __init__(self) -> None:
        print("Connecting to the database...")


# --- Example Usage --- #

if __name__ == "__main__":
    # Simple decorator example
    print("=== log_start_end decorator example ===")
    say_hello()

    # Function-based decorator with argument example
    print("\n=== repeat decorator example ===")
    greet()

    # Class-based decorator with arguments example
    print("\n=== AddPrefixSuffix decorator example ===")
    display_message()

    # Decorators on class methods
    print("\n=== Greeter class method decorators ===")
    greeter = Greeter()
    greeter.greet()
    greeter.wave()
    greeter.cheer()

    # Singleton class decorator example
    print("\n=== Singleton class decorator example ===")
    db1 = Database()
    db2 = Database()
    print("db1 is db2:", db1 is db2)  # Should print True, confirming singleton behavior
