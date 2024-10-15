"""Module to test prototype module classes and functions"""

import unittest

from src.oop.patterns.creational.prototype.prototype import SelfReferencingEntity, SomeComponent


class TestSelfReferencingEntity(unittest.TestCase):
    """Test Class for SelfReferencingEntity"""

    component: SomeComponent
    circular_ref: SelfReferencingEntity

    def setUp(self) -> None:
        """Setup for testing, calling before every test"""
        self.circular_ref = SelfReferencingEntity()
        self.component = SomeComponent(1, [], self.circular_ref)

    @classmethod
    def setUpClass(cls) -> None:
        """Setup class for testing, calling only when class initiate"""

    def test_circular_ref_component(self) -> None:
        """Test if child and parent are not he same"""

        # check if they are not equal
        self.assertNotEqual(self.component, self.circular_ref)

        # check if component.circular_ref assigned right
        self.assertEqual(self.circular_ref, self.component.some_circular_ref)

        # check if parent is null
        self.assertIsNone(self.circular_ref.parent)

        # assign parent to create circular ref
        self.circular_ref.parent = self.component

        # check if parent assigned properly
        self.assertEqual(self.circular_ref.parent, self.component)


class TestSomeComponent(unittest.TestCase):
    """Test Class for TestSomeComponent"""

    component: SomeComponent
    circular_ref: SelfReferencingEntity
    some_int: int
    some_list_of_objects: list[int | set[int] | list[int]]

    def setUp(self) -> None:
        """Setup for testing, calling before every test"""
        self.some_int = 23
        self.some_list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
        self.circular_ref = SelfReferencingEntity()
        self.component = SomeComponent(self.some_int, self.some_list_of_objects, self.circular_ref)
        self.circular_ref.parent = self.component

    @classmethod
    def setUpClass(cls) -> None:
        """Setup class for testing, calling only when class initiate"""

    def test_shallow_clone(self) -> None:
        """Test Shallow Copy to verify it works fine and as expected"""
        shallow_copy: SomeComponent = self.component.shallow_clone()

        # test copy and component not the same
        self.assertNotEqual(shallow_copy, self.component)
        self.assertNotEqual(id(shallow_copy), id(self.component))

        # test changing int value and not equal
        self.component.some_int = 24
        self.assertNotEqual(shallow_copy.some_int, self.component.some_int)

        # change index[0] in array and test
        self.component.some_list_of_objects[0] = 10
        self.assertEqual(shallow_copy.some_list_of_objects[0], 10)

        # change add to set and test
        self.component.some_list_of_objects[1].add(10)  # type: ignore
        self.assertTrue(10 in shallow_copy.some_list_of_objects[1])  # type: ignore

        # add to list and check
        self.component.some_list_of_objects[2].append(10)  # type: ignore
        self.assertEqual(shallow_copy.some_list_of_objects[2][-1], 10)  # type: ignore

        # test circular ref
        self.assertEqual(
            id(shallow_copy.some_circular_ref),
            id(shallow_copy.some_circular_ref.parent.some_circular_ref),  # type: ignore
        )
        self.assertEqual(
            id(shallow_copy.some_circular_ref.parent),
            id(shallow_copy.some_circular_ref.parent.some_circular_ref.parent),  # type: ignore
        )

    def test_clone(self) -> None:
        """Test  Clone to verify it works fine and as expected"""
        clone: SomeComponent = self.component.clone()

        # test copy and component not the same
        self.assertNotEqual(clone, self.component)
        self.assertNotEqual(id(clone), id(self.component))

        # test changing int value and not equal
        self.component.some_int = 24
        self.assertNotEqual(clone.some_int, self.component.some_int)

        # change index[0] in array and test
        self.component.some_list_of_objects[0] = 10
        self.assertNotEqual(clone.some_list_of_objects[0], 10)

        # change add to set and test
        self.component.some_list_of_objects[1].add(10)  # type: ignore
        self.assertFalse(10 in clone.some_list_of_objects[1])  # type: ignore

        # add to list and check
        self.component.some_list_of_objects[2].append(10)  # type: ignore
        self.assertNotEqual(clone.some_list_of_objects[2][-1], 10)  # type: ignore

        # check circular ref
        self.assertEqual(
            id(clone.some_circular_ref),
            id(clone.some_circular_ref.parent.some_circular_ref),  # type: ignore
        )
        self.assertEqual(
            id(clone.some_circular_ref.parent),
            id(clone.some_circular_ref.parent.some_circular_ref.parent),  # type: ignore
        )
