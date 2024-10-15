"""Composite Design Pattern"""

from typing import Any


class FileSystemComponent:
    """Abstract class for files and directories."""

    def display(self, depth: int = 0) -> None:
        """Display the component. To be implemented by subclasses."""
        raise NotImplementedError("You should implement this method.")


class File(FileSystemComponent):
    """Represents a file in the file system."""

    def __init__(self, name: str) -> None:
        self.name = name

    def display(self, depth: int = 0) -> None:
        """Display the file's name."""
        print("  " * depth + f"File: {self.name}")


class Directory(FileSystemComponent):
    """Represents a directory in the file system."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[Any] = []

    def add(self, component: FileSystemComponent) -> None:
        """Add a component (file or directory) to the directory."""
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component (file or directory) from the directory."""
        self.children.remove(component)

    def display(self, depth: int = 0) -> None:
        """Display the directory and its contents."""
        print("  " * depth + f"Directory: {self.name}")
        for child in self.children:
            child.display(depth + 1)
