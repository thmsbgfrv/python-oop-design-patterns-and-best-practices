# tests/oop/patterns/creational/test_singleton.py

"""
Tests for the Singleton class.
"""

from oop.patterns.creational.singleton import Singleton


class TestSingleton:
    """
    Test suite for the Singleton class.
    """

    def test_singleton_instance_creation(self) -> None:
        """
        Test that only one instance of Singleton is created.
        """
        instance1 = Singleton()
        instance2 = Singleton()

        # Assert that both instances are the same
        assert instance1 is instance2

    def test_singleton_config(self) -> None:
        """
        Test that the singleton has the correct config and that changes
        are reflected across instances.
        """
        instance = Singleton()
        assert instance.config == {"db": "test"}

        # Modify config and check if it affects the same instance
        instance.config["db"] = "production"
        assert instance.config["db"] == "production"

        # Create a new instance and check the config again
        new_instance = Singleton()
        assert new_instance.config["db"] == "production"  # Should reflect the change

    def test_singleton_instance_type(self) -> None:
        """Test that the instance is of the correct type."""
        instance1 = Singleton.get_instance()
        instance2 = Singleton.get_instance()
        assert isinstance(instance1, Singleton), "Instance should be of type Singleton"
        assert isinstance(instance2, Singleton), "Instance should be of type Singleton"
        assert instance1 is instance2
