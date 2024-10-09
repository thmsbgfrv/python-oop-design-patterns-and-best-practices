"""Module for simple builder pattern"""


class Car:
    """Car class to use in builder"""

    def __init__(self) -> None:
        """Init class with defaults"""
        self.model: str | None = None
        self.year: int | None = None

    def __str__(self) -> str:
        """ToString method for car"""
        return f'Car: {self.model} {self.year}'


class CarBuilder:
    """Car builder class to create car"""

    def __init__(self) -> None:
        """Init for Car builder"""
        self._car: Car = Car()

    def set_model(self, model: str) -> "CarBuilder":
        """setter for model"""
        self._car.model = model
        return self

    def set_year(self, year: int) -> "CarBuilder":
        """Setter for year"""
        self._car.year = year
        return self

    def build(self) -> Car:
        """build method to return car object"""
        built_car: Car = self._car
        self.reset()
        return built_car

    def reset(self) -> None:
        """Reset method for builder"""
        self._car = Car()
