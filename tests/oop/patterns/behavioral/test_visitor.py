"""Unit tests for Visitor Pattern in E-commerce Product Management"""

import unittest
from unittest.mock import MagicMock, patch

from src.oop.patterns.behavioral.visitor import Clothing, DiscountVisitor, DisplayVisitor, Electronics


class TestVisitorPattern(unittest.TestCase):
    """Tests for the Visitor Pattern implementations."""

    @patch("builtins.print")
    def test_display_visitor(self, mock_print: MagicMock) -> None:
        """Test the DisplayVisitor's output for products."""
        electronics = Electronics(name="Smartphone", price=699.99)
        clothing = Clothing(name="T-shirt", price=19.99)

        display_visitor = DisplayVisitor()
        electronics.accept(display_visitor)
        clothing.accept(display_visitor)

        # Verify printed output
        mock_print.assert_any_call("Electronics - Name: Smartphone, Price: 699.99")
        mock_print.assert_any_call("Clothing - Name: T-shirt, Price: 19.99")

    @patch("builtins.print")
    def test_discount_visitor(self, mock_print: MagicMock) -> None:
        """Test the DiscountVisitor's output for products."""
        electronics = Electronics(name="Smartphone", price=100.00)
        clothing = Clothing(name="T-shirt", price=100.00)

        discount_visitor = DiscountVisitor()

        # # Verify printed output
        electronics.accept(discount_visitor)

        mock_print.assert_any_call("Discount for Electronics - Smartphone: 10.00")

        clothing.accept(discount_visitor)
        mock_print.assert_any_call("Discount for Clothing - T-shirt: 15.00")
