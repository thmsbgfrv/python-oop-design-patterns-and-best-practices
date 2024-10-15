"""Packaging Test Module"""

import unittest

from src.oop.patterns.creational.abstract_factory.packagings import AbstractPackaging, BoxPackaging, ContainerPackaging


class TestBoxPackaging(unittest.TestCase):
    """Test Box Packaging Class"""

    box: BoxPackaging

    @classmethod
    def setUpClass(cls) -> None:
        """BoxPackaging initialize class"""
        cls.box = BoxPackaging()

    def test_object_creating_valid(self) -> None:
        """test if box object created properly"""

        # assert box is BoxPackaging/AbstractPackaging
        self.assertTrue(isinstance(self.box, BoxPackaging))
        self.assertTrue(isinstance(self.box, AbstractPackaging))

    def test_package_method(self) -> None:
        """Test if package method runs and return valid string"""

        self.assertEqual(self.box.package(), "Packing in a box.")


class TestContainerPackaging(unittest.TestCase):
    """Test Container Packaging Class"""

    container: ContainerPackaging

    @classmethod
    def setUpClass(cls) -> None:
        """ContainerPackaging initialize class"""
        cls.container = ContainerPackaging()

    def test_object_creating_valid(self) -> None:
        """test if container object created properly"""

        # assert box is BoxPackaging/AbstractPackaging
        self.assertTrue(self.container, ContainerPackaging)
        self.assertTrue(self.container, AbstractPackaging)

    def test_package_method(self) -> None:
        """Test if package method runs and return valid string"""

        self.assertEqual(self.container.package(), "Packing in a container.")
