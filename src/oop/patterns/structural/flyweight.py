"""Flyweight DP module"""


class Character:
    """Flyweight class representing a character in a text editor."""

    def __init__(self, char: str, font: str, color: str) -> None:
        self.char = char
        self.font = font
        self.color = color

    def display(self) -> None:
        """Display the character with its attributes."""
        print(f"Character: {self.char}, Font: {self.font}, Color: {self.color}")


class CharacterFactory:
    """Factory class to manage Flyweight objects."""

    def __init__(self) -> None:
        self.characters: dict[tuple[str, str, str], Character] = {}

    def get_character(self, char: str, font: str, color: str) -> Character:
        """Get a character instance, creating it if it doesn't exist."""
        key = (char, font, color)
        if key not in self.characters:
            self.characters[key] = Character(char, font, color)
        return self.characters[key]
