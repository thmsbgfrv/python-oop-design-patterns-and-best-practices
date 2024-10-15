"""Module to implement prototype class"""

import copy
from abc import ABC, abstractmethod
from typing import Any, Optional


class Prototype(ABC):
    """Prototype interface for to implement this pattern"""

    @abstractmethod
    def clone(self) -> Any:
        """Deep Copy"""

    @abstractmethod
    def shallow_clone(self) -> Any:
        """Shallow Copy"""


class SelfReferencingEntity:
    """Self Referencing Entity will be used as test for our design Pattern"""

    def __init__(self) -> None:
        """Constructor which create object with parent=None as default"""
        self.parent: Optional["SomeComponent"] = None

    def set_parent(self, parent: "SomeComponent") -> None:
        """Setter for SelfReferencingEntity"""
        self.parent = parent


class SomeComponent(Prototype):
    """Component to implement prototype pattern"""

    def __init__(
        self,
        some_int: int,
        some_list_of_objects: list[int | set[int] | list[int]],
        some_circular_ref: SelfReferencingEntity,
    ) -> None:
        """Implementing contructor with default values"""
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def shallow_clone(self) -> "SomeComponent":
        """Clone method to creating shallow copy and return object"""
        return copy.copy(self)

    def clone(self) -> "SomeComponent":
        """Clone method to creating deep copy of SomeComponent"""
        return copy.deepcopy(self)

    def __copy__(self) -> "SomeComponent":
        """
        Create a shallow copy. This method will be called whenever someone calls
        `copy.copy` with this object and the returned value is returned as the
        new shallow copy.
        :return:
        """

        some_int: int = self.some_int
        # creating the shallow copy of nested object
        some_list_of_objects: list[int | set[int] | list[int]] = copy.copy(self.some_list_of_objects)
        some_circular_ref: SelfReferencingEntity = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new: "SomeComponent" = self.__class__(some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo: Optional[dict[Any, Any]] = None) -> "SomeComponent":
        """
        Create a deep copy. This method will be called whenever someone calls
        `copy.deepcopy` with this object and the returned value is returned as
        the new deep copy.

        What is the use of the argument `memo`? Memo is the dictionary that is
        used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all the `deepcopy` calls
        you make in the `__deepcopy__` implementation to prevent infinite
        recursions.

        :param memo:
        :return:
        """
        if memo is None:
            memo = {}

        some_int: int = self.some_int
        # creating the shallow copy of nested object
        some_list_of_objects: list[int | set[int] | list[int]] = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref: SelfReferencingEntity = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new: "SomeComponent" = self.__class__(some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new
