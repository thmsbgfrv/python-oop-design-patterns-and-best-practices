"""Tests for Mediator Pattern in a Chat Application"""

import unittest
from unittest.mock import MagicMock, patch

from src.oop.patterns.behavioral.mediator import ChatRoom, User


class TestMediatorPattern(unittest.TestCase):
    """Unit tests for the Mediator Pattern."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.chat_room = ChatRoom()
        self.user1 = User("Alice", self.chat_room)
        self.user2 = User("Bob", self.chat_room)
        self.chat_room.add_colleague(self.user1)
        self.chat_room.add_colleague(self.user2)

    @patch("builtins.print")
    def test_user_send_message(self, mock_print: MagicMock) -> None:
        """Test if a user can send a message."""
        self.user1.send("Hello, Bob!")
        mock_print.assert_called_with("Bob: Received message: Hello, Bob!")

    @patch("builtins.print")
    def test_user_receive_message(self, mock_print: MagicMock) -> None:
        """Test if a user receives a message correctly."""
        self.user1.send("Hello, Bob!")
        self.user2.send("Hi Alice!")

        mock_print.assert_any_call("Alice: Received message: Hi Alice!")
        mock_print.assert_any_call("Bob: Received message: Hello, Bob!")

    @patch("builtins.print")
    def test_multiple_users_send_message(self, mock_print: MagicMock) -> None:
        """Test multiple users sending messages."""
        self.user1.send("Hello everyone!")
        self.user2.send("Hi there!")

        mock_print.assert_any_call("Alice: Received message: Hi there!")
        mock_print.assert_any_call("Bob: Received message: Hello everyone!")

    @patch("builtins.print")
    def test_no_message_sent_to_sender(self, mock_print: MagicMock) -> None:
        """Test that a user does not receive their own message."""
        self.user1.send("Hello everyone!")
        # Check that Alice did not receive her own message
        calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertNotIn("Alice: Received message: Hello everyone!", calls)
