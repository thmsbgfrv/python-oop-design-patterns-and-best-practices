# tests/oop/patterns/creational/singleton/test_singleton_naive_thread_safe.py

"""
Tests for the Singleton with naive and Thread Safe Solution
"""

from threading import Thread
from typing import List

from src.oop.patterns.creational.singleton.singleton_naive_thread_safe import (
    Singleton,
    SingletonNaiveThreadSafe,
    SingletonNaiveThreadSafe2,
)


class TestSingletonNaiveThreadSafeThreadSafe:
    """
    Test suite for the SingletonNaiveThreadSafeThreadSafe based (Singleton).
    """

    @classmethod
    def setup_method(cls) -> None:
        """Reset Singletons before each test"""
        Singleton.reset()

    def test_singleton_naive_instance_creation(self) -> None:
        """Test that only one instance of Singleton is created"""
        instance1: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("First")
        instance2: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("Second")

        # assert that both instances are the same
        assert instance1 is instance2

    def test_singleton_naive_instance_name_variable(self) -> None:
        """Test the name variable remains consistent across instances."""
        instance1: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("First")
        instance2: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("Second")

        assert instance1.name == instance2.name == "First"

    def test_different_singleton_classes(self) -> None:
        """Test that different singleton classes do not interfere with each other."""
        instance1: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("First")
        instance2: SingletonNaiveThreadSafe2 = SingletonNaiveThreadSafe2("Second")

        # assert that instances of different singletons are not the same
        assert id(instance1) != id(instance2)

        # Assert that they have their own names
        assert instance1.name != instance2.name
        assert instance1.name == "First"
        assert instance2.name == "Second"

    def test_reset_singleton(self) -> None:
        """Test that resetting the singleton instances."""
        instance1: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("First")
        Singleton.reset()
        instance2: SingletonNaiveThreadSafe = SingletonNaiveThreadSafe("Second")

        # assert that after reset, a new instance is created
        assert instance1 is not instance2
        assert instance2.name == "Second"

    def test_thread_safe(self) -> None:
        """Test that SingletonNaiveThreadSafe is thread-safe."""
        instance_list: List[SingletonNaiveThreadSafe] = []

        def create_instance(name: str) -> None:
            instance = SingletonNaiveThreadSafe(name)
            instance_list.append(instance)

        threads: List[Thread] = []

        for i in range(10):  # create 10 threads
            thread = Thread(target=create_instance, args=(f"Instance {i}",))
            threads.append(thread)
            thread.start()

        # assert that all instances in the list are the same
        assert all(instance is instance_list[0] for instance in instance_list)

        # assert that the name of the instance is that of the first thread
        assert all(instance.name == instance_list[0].name == "Instance 0" for instance in instance_list)
