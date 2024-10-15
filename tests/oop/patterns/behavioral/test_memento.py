"""Memento module tests"""

import unittest
from unittest.mock import MagicMock, patch

from src.oop.patterns.behavioral.memento import TextEditor


class TestTextEditor(unittest.TestCase):
    """Tests for the TextEditor class using the Memento Pattern."""

    def setUp(self) -> None:
        """Set up a TextEditor instance for testing."""
        self.editor = TextEditor()

    def test_initial_text(self) -> None:
        """Test the initial text in the editor is empty."""
        self.assertEqual(self.editor.get_text(), "")

    def test_type_and_save(self) -> None:
        """Test typing text and saving it as a memento."""
        self.editor.type("Hello, ")
        self.editor.save()
        self.assertEqual(self.editor.get_text(), "Hello, ")

    def test_undo_last_state(self) -> None:
        """Test undoing the last saved state."""
        self.editor.type("Hello, ")
        self.editor.save()
        self.editor.type("world!")
        self.editor.undo()
        self.assertEqual(self.editor.get_text(), "")

    @patch("builtins.print")
    def test_undo_without_states(self, mock_print: MagicMock) -> None:
        """Test undoing when there are no saved states."""
        self.editor.undo()
        mock_print.assert_called_once_with("No states to undo.")

    def test_multiple_undos(self) -> None:
        """Test multiple undos in sequence."""
        self.editor.type("Hello, ")
        self.editor.save()

        self.editor.type("world!")
        self.editor.save()

        self.assertEqual(self.editor.get_text(), "Hello, world!")

        self.editor.undo()  # Undo "world!"
        self.assertEqual(self.editor.get_text(), "Hello, ")
        self.editor.undo()  # Undo "Hello, "
        self.assertEqual(self.editor.get_text(), "")

    @patch("builtins.print")
    def test_undo_after_multiple_undos(self, mock_print: MagicMock) -> None:
        """Test undoing after multiple undos gives proper message."""
        self.editor.type("Hello, ")
        self.editor.save()
        self.editor.type("world!")
        self.editor.save()
        self.editor.undo()  # Undo "world!"
        self.editor.undo()  # Undo "Hello, "
        self.editor.undo()  # No states to undo
        mock_print.assert_called_once_with("No states to undo.")
