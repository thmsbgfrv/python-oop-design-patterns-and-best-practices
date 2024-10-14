"""
Module of Observer Pattern

This module implements the Observer design pattern, allowing objects (observers) to subscribe to and receive updates
from a subject (observable). It decouples the subject from the observers, allowing them to react independently
to changes.

Classes:
    Subject (abstract class): Defines the methods for managing observers.
    ConcreteSubject (concrete class): The subject that notifies observers when its state changes.
    Observer (abstract class): Defines the interface for objects that want to observe the subject.
    ConcreteObserver (concrete class): Observers that receive updates from the subject.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer (Abstract)

    Defines the interface for all observers that need to be notified when the subject's state changes.

    Methods:
        update(subject: 'ConcreteSubject') -> None:
            Update the observer with the subject's new state.
    """

    @abstractmethod
    def update(self, subject: 'ConcreteSubject') -> None:
        """Receive update from the subject with the current state."""


class Subject(ABC):
    """
    Subject (Abstract)

    Defines the interface for managing observers. Subjects can register, unregister, and notify observers.

    Methods:
        attach(observer: Observer) -> None:
            Add an observer to the subject.
        detach(observer: Observer) -> None:
            Remove an observer from the subject.
        notify() -> None:
            Notify all observers of a state change.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach Abstractmethod Method"""

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """detach Abstractmethod Method"""

    @abstractmethod
    def notify(self) -> None:
        """notify Abstractmethod Method"""


class ConcreteSubject(Subject):
    """
    ConcreteSubject

    Maintains a list of observers and notifies them of any changes in its state.

    Attributes:
        _observers (List[Observer]): A list of observers that are attached to this subject.
        _state (int): The state of the subject that observers are interested in.

    Methods:
        attach(observer: Observer) -> None:
            Add an observer to the subject.
        detach(observer: Observer) -> None:
            Remove an observer from the subject.
        notify() -> None:
            Notify all attached observers of a state change.
        change_state(new_state: int) -> None:
            Change the state of the subject and notify observers.
        get_state() -> int:
            Get the current state of the subject.
    """

    _observers: list[Observer] = []
    _state: int = 0

    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)
            # Notify the newly attached observer of the current state immediately
            if self._state is not None:
                observer.update(self)

    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers of a state change."""
        for observer in self._observers:
            observer.update(self)

    def change_state(self, new_state: int) -> None:
        """Change the state of the subject and notify observers."""
        self._state = new_state
        self.notify()

    def get_state(self) -> int:
        """Return the current state of the subject."""
        return self._state


class ConcreteObserver(Observer):
    """
    ConcreteObserver

    Concrete implementation of an observer. It receives updates from the subject and reacts accordingly.

    Attributes:
        _name (str): The name of the observer.
        _subject_state (int): The state received from the subject.

    Methods:
        update(subject: ConcreteSubject) -> None:
            Update the observer's state based on the subject's state.
        display_state() -> None:
            Display the current state of the observer.
    """

    _subject_state: int = 0

    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, subject: ConcreteSubject) -> None:
        """Update the observer with the current state of the subject."""
        self._subject_state = subject.get_state()
        self.display_state()

    def display_state(self) -> None:
        """Display the current state of the observer."""
        print(f"{self._name} received update: State is now {self._subject_state}")
