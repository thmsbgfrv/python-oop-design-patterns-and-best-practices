"""Flyweight modules tests"""

import unittest
from io import StringIO
from unittest.mock import patch

from oop.patterns.structural.flyweight import CharacterFactory


class TestFlyweight(unittest.TestCase):
    """Test cases for the Flyweight pattern in a text editor."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_character_creation(self, mock_stdout: StringIO) -> None:
        """Test creating and displaying a character."""
        factory = CharacterFactory()
        char = factory.get_character('A', 'Arial', 'Red')
        char.display()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Character: A, Font: Arial, Color: Red")

    def test_character_sharing(self) -> None:
        """Test that the same character with the same attributes is shared."""
        factory = CharacterFactory()
        char1 = factory.get_character('A', 'Arial', 'Red')
        char2 = factory.get_character('A', 'Arial', 'Red')
        char3 = factory.get_character('B', 'Arial', 'Red')

        self.assertIs(char1, char2)  # char1 and char2 should be the same instance
        self.assertIsNot(char1, char3)  # char1 and char3 should be different instances
