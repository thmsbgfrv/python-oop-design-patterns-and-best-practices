"""~Car Test Builder~"""
import unittest

from oop.patterns.creational.builder.builder import Car, CarBuilder


class TestCarBuilder(unittest.TestCase):
    """~Car Test Builder~"""
    def setUp(self) -> None:
        """Set up a new CarBuilder instance before each test."""
        self.builder: CarBuilder = CarBuilder()

    def test_set_model(self) -> None:
        """Test that the model of the car is set correctly."""
        self.builder.set_model("Model S")
        car: Car = self.builder.build()
        self.assertEqual(car.model, "Model S")
        self.assertEqual(car.year, None)  # Ensure year is not set

    def test_set_year(self) -> None:
        """Test that the year of the car is set correctly."""
        self.builder.set_year(2022)
        car: Car = self.builder.build()
        self.assertEqual(car.year, 2022)
        self.assertEqual(car.model, None)  # Ensure model is not set

    def test_build_car(self) -> None:
        """Test building a car with both model and year set."""
        self.builder.set_model("Model X").set_year(2021)
        car: Car = self.builder.build()
        self.assertEqual(car.model, "Model X")
        self.assertEqual(car.year, 2021)

    def test_reset_builder(self) -> None:
        """Test that the builder resets after building a car."""
        self.builder.set_model("Model Y").set_year(2020)
        car1: Car = self.builder.build()

        # Ensure the car1 object has the correct data
        self.assertEqual(car1.model, "Model Y")
        self.assertEqual(car1.year, 2020)

        # Create a new car after reset
        self.builder.set_model("Model Z")
        car2: Car = self.builder.build()

        # Ensure car1 and car2 have different values and the builder was reset
        self.assertEqual(car2.model, "Model Z")
        self.assertEqual(car2.year, None)
        self.assertNotEqual(car1.model, car2.model)
        self.assertNotEqual(car1.year, car2.year)

    def test_reset_after_build(self) -> None:
        """Test that the builder is automatically reset after calling build."""
        self.builder.set_model("Model S").set_year(2022)
        car1: Car = self.builder.build()

        # Builder should be reset, next car should be a fresh instance
        car2: Car = self.builder.build()

        # The second car should have no model or year set
        self.assertIsNone(car2.model)
        self.assertIsNone(car2.year)
        self.assertNotEqual(car1, car2)

    def test_str_method(self) -> None:
        """Test that the __str__ method of Car works as expected."""
        self.builder.set_model("Roadster").set_year(2023)
        car: Car = self.builder.build()
        self.assertEqual(str(car), "Car: Roadster 2023")
