"""Module for testing the Command Pattern implementation in an online order system."""

import unittest
from unittest.mock import MagicMock, patch

from src.oop.patterns.behavioral.command import CancelOrderCommand, Order, OrderInvoker, PlaceOrderCommand


class TestCommandPattern(unittest.TestCase):
    """Test case for the Command Pattern in an online order system."""

    def setUp(self) -> None:
        """Set up an order and commands for testing."""
        self.order = Order()
        self.place_order = PlaceOrderCommand(self.order)
        self.cancel_order = CancelOrderCommand(self.order)
        self.invoker = OrderInvoker()

    @patch("builtins.print")
    def test_place_order_command(self, mock_print: MagicMock) -> None:
        """Test executing the place order command."""
        self.invoker.set_command(self.place_order)
        self.invoker.press_button()  # Place the order

        mock_print.assert_called_once_with("Order has been placed.")

    @patch("builtins.print")
    def test_cancel_order_command(self, mock_print: MagicMock) -> None:
        """Test executing the cancel order command."""
        self.invoker.set_command(self.cancel_order)
        self.invoker.press_button()  # Cancel the order

        mock_print.assert_called_once_with("Order has been canceled.")

    @patch("builtins.print")
    def test_undo_command(self, mock_print: MagicMock) -> None:
        """Test undoing the last command executed."""
        self.invoker.set_command(self.place_order)
        self.invoker.press_button()  # Place the order
        self.invoker.set_command(self.cancel_order)
        self.invoker.press_button()  # Cancel the order

        # Undo: Place the order again
        self.invoker.press_undo()
        mock_print.assert_called_with("Order has been placed.")

        # Undo the cancel
        self.invoker.press_undo()
        mock_print.assert_called_with("Order has been canceled.")
