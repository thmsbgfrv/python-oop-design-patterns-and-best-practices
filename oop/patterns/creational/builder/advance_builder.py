"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Book:
        pass

    @abstractmethod
    def set_title(self, title: str) -> None:
        pass

    @abstractmethod
    def set_description(self, description: str) -> None:
        pass


class BookBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._book = Book()

    @property
    def product(self) -> Book:
        book = self._book
        self.reset()
        return book

    def set_title(self, title: str) -> None:
        self._book.title = title

    def set_description(self, description: str) -> None:
        self._book.description = description


class Book:
    def __init__(self) -> None:
        self.title = ""
        self.description = ""

    def show_details(self) -> None:
        print(f"Title: {self.title}, Description: {self.description}")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_simple_book(self) -> None:
        self.builder.set_title("Simple Book")

    def build_detailed_book(self) -> None:
        self.builder.set_title("Detailed Book")
        self.builder.set_description("This is a detailed description of the book.")


if __name__ == "__main__":
    director = Director()
    builder = BookBuilder()
    director.builder = builder

    print("Simple book:")
    director.build_simple_book()
    builder.product.show_details()

    print("\nDetailed book:")
    director.build_detailed_book()
    builder.product.show_details()

    print("\nCustom book:")
    builder.set_title("Custom Title")
    builder.set_description("Custom description for the book.")
    builder.product.show_details()

"""
