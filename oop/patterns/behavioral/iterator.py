"""Module for demonstrating the Iterator Pattern."""

from abc import ABC, abstractmethod
from typing import List


class Book:
    """Represents a book with a title and author."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Iterator(ABC):
    """Iterator interface for traversing collections."""

    @abstractmethod
    def next(self) -> Book:
        """Return the next book in the collection."""

    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more books to iterate over."""


class BookIterator(Iterator):
    """Concrete iterator for iterating over a BookCollection."""

    def __init__(self, collection: 'MyBookCollection') -> None:
        self._collection = collection
        self._index = 0

    def next(self) -> Book:
        """Return the next book in the collection."""
        book = self._collection.get_book(self._index)
        self._index += 1
        return book

    def has_next(self) -> bool:
        """Check if there are more books to iterate over."""
        return self._index < len(self._collection)


class BookCollection(ABC):
    """Aggregate interface for the collection of books."""

    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Create an iterator for the book collection."""


class MyBookCollection(BookCollection):
    """Concrete aggregate that holds a collection of books."""

    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the collection."""
        self._books.append(book)

    def get_book(self, index: int) -> Book:
        """Return a book at a specific index."""
        return self._books[index]

    def __len__(self) -> int:
        """Return the number of books in the collection."""
        return len(self._books)

    def create_iterator(self) -> Iterator:
        """Create an iterator for the book collection."""
        return BookIterator(self)
