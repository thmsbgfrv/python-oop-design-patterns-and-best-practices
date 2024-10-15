"""Module for testing the Iterator Pattern implementation."""

import unittest

from src.oop.patterns.behavioral.iterator import Book, MyBookCollection


class TestMyBookCollection(unittest.TestCase):
    """Test case for MyBookCollection."""

    def setUp(self) -> None:
        """Set up a book collection for testing."""
        self.collection = MyBookCollection()
        self.collection.add_book(Book("1984", "George Orwell"))
        self.collection.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
        self.collection.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    def test_book_count(self) -> None:
        """Test the count of books in the collection."""
        self.assertEqual(len(self.collection), 3)

    def test_book_retrieval(self) -> None:
        """Test the retrieval of books by index."""
        self.assertEqual(str(self.collection.get_book(0)), "1984 by George Orwell")
        self.assertEqual(str(self.collection.get_book(1)), "To Kill a Mockingbird by Harper Lee")
        self.assertEqual(str(self.collection.get_book(2)), "The Great Gatsby by F. Scott Fitzgerald")
