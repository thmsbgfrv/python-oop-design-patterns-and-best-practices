"""Module for Visitor Pattern in E-commerce Product Management"""

from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class for products."""

    @abstractmethod
    def accept(self, visitor: 'ProductVisitor') -> None:
        """Accept a visitor to perform an operation."""


class Electronics(Product):
    """Concrete class for Electronics product."""

    def __init__(self, name: str, price: float) -> None:
        """Initialize the Electronics product."""
        self.name: str = name
        self.price: float = price

    def accept(self, visitor: 'ProductVisitor') -> None:
        """Accept a visitor for Electronics."""
        visitor.visit_electronics(self)


class Clothing(Product):
    """Concrete class for Clothing product."""

    def __init__(self, name: str, price: float) -> None:
        """Initialize the Clothing product."""
        self.name: str = name
        self.price: float = price

    def accept(self, visitor: 'ProductVisitor') -> None:
        """Accept a visitor for Clothing."""
        visitor.visit_clothing(self)


class ProductVisitor(ABC):
    """Abstract base class for product visitors."""

    @abstractmethod
    def visit_electronics(self, electronics: Electronics) -> None:
        """Visit an Electronics product."""

    @abstractmethod
    def visit_clothing(self, clothing: Clothing) -> None:
        """Visit a Clothing product."""


class DisplayVisitor(ProductVisitor):
    """Concrete visitor for displaying product details."""

    def visit_electronics(self, electronics: Electronics) -> None:
        """Display details of an Electronics product."""
        print(f"Electronics - Name: {electronics.name}, Price: {electronics.price:.2f}")

    def visit_clothing(self, clothing: Clothing) -> None:
        """Display details of a Clothing product."""
        print(f"Clothing - Name: {clothing.name}, Price: {clothing.price:.2f}")


class DiscountVisitor(ProductVisitor):
    """Concrete visitor for calculating product discounts."""

    def visit_electronics(self, electronics: Electronics) -> None:
        """Calculate discount for an Electronics product."""
        discount = electronics.price * 0.1  # 10% discount
        print(f"Discount for Electronics - {electronics.name}: {discount:.2f}")

    def visit_clothing(self, clothing: Clothing) -> None:
        """Calculate discount for a Clothing product."""
        discount = clothing.price * 0.15  # 15% discount
        print(f"Discount for Clothing - {clothing.name}: {discount:.2f}")
