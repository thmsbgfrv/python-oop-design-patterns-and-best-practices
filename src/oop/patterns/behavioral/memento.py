"""Module implementing the Memento Pattern for a Text Editor."""


class Memento:
    """Memento class that stores the state of the text editor."""

    def __init__(self, state: str) -> None:
        """Initialize the Memento with a given state."""
        self._state = state

    def get_state(self) -> str:
        """Get the stored state of the Memento."""
        return self._state


class TextEditor:
    """TextEditor class that can create and restore mementos."""

    def __init__(self) -> None:
        """Initialize the TextEditor with empty text and an empty list of mementos."""
        self._text = ""
        self._mementos: list[Memento] = []

    def type(self, text: str) -> None:
        """Type text into the editor, modifying its current state.

        Args:
            text (str): The text to be added to the current state.
        """
        self._text += text

    def save(self) -> None:
        """Save the current state as a memento."""
        self._mementos.append(Memento(self._text))

    def undo(self) -> str | None:
        """Restore the last saved state, if available.

        Returns:
            Optional[str]: The restored state or None if no states are available to undo.
        """
        if not self._mementos:
            print("No states to undo.")
            return None

        self._mementos.pop()

        if self._mementos:
            self._text = self._mementos[-1].get_state()
        else:
            self._text = ""
        return self._text

    def get_text(self) -> str:
        """Get the current text in the editor.

        Returns:
            str: The current text in the editor.
        """
        return self._text
