# tests/oop/patterns/creational/test_singleton_naive.py

"""
Tests for the SingletonNaive class. With Naive Solution
"""

from oop.patterns.creational.singleton_naive import Singleton, SingletonNaive, SingletonNaive2


class TestSingletonNaive:
    """
    Test suite for the SingletonNaive class.
    """

    @classmethod
    def setup_method(cls) -> None:
        """Reset the Singleton instance before each test."""
        Singleton.reset()

    def test_singleton_naive_instance_creation(self) -> None:
        """
        Test that only one instance of SingletonNaive is created.
        """
        instance1: SingletonNaive = SingletonNaive("First")
        instance2: SingletonNaive = SingletonNaive("Second")
        instance3: SingletonNaive2 = SingletonNaive2("First")
        instance4: SingletonNaive2 = SingletonNaive2("Second")

        # Assert that both instances are the same
        assert instance1 is instance2
        assert instance3 is instance4
        assert not isinstance(instance1, SingletonNaive2)
        assert not isinstance(instance2, SingletonNaive2)
        assert not isinstance(instance3, SingletonNaive)
        assert not isinstance(instance4, SingletonNaive)

    def test_singleton_naive_instance_name_variable(self) -> None:
        """
        Test that only one instance of SingletonNaive is created.
        """
        instance1: SingletonNaive = SingletonNaive("First 1")
        instance2: SingletonNaive = SingletonNaive("Second 1")
        instance3: SingletonNaive2 = SingletonNaive2("First 2")
        instance4: SingletonNaive2 = SingletonNaive2("Second 2")

        # Assert that both instances are the same
        assert instance1.name == "First 1"
        assert instance2.name == "First 1"
        assert instance3.name == "First 2"
        assert instance4.name == "First 2"

    def test_singleton_naive_instance_reset(self) -> None:
        """Test Reset Method Of Metaclass"""
        instance1: SingletonNaive = SingletonNaive("First 1")
        Singleton.reset()
        instance2: SingletonNaive = SingletonNaive("First 2")

        assert instance1 is not instance2
        assert instance2.name == "First 2"
