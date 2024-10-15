"""
Test Module for Observer Pattern

This module contains unit tests for the Observer design pattern. These tests verify that
the observers receive the correct state updates from the subject.
"""

import unittest

from src.oop.patterns.behavioral.observer import ConcreteObserver, ConcreteSubject

# pylint: disable=W0212


class TestObserverPattern(unittest.TestCase):
    """
    Unit tests for the Observer design pattern.

    This class tests if observers correctly receive state updates and if detaching an observer works as expected.
    """

    def setUp(self) -> None:
        """Sets up the subject and observers before each test case."""
        self.subject: ConcreteSubject = ConcreteSubject()
        self.observer1: ConcreteObserver = ConcreteObserver("Observer 1")
        self.observer2: ConcreteObserver = ConcreteObserver("Observer 2")

        # Attach observers to the subject
        self.subject.attach(self.observer1)
        self.subject.attach(self.observer2)

    def test_single_observer_update(self) -> None:
        """
        Test that a single observer receives the correct state update from the subject.

        Observer 1 should receive the state update from the subject.
        """
        # Change subject's state to 10 and expect observer1 to receive the update
        self.subject.change_state(10)
        self.assertEqual(self.observer1._subject_state, 10)
        self.assertEqual(self.observer2._subject_state, 10)

    def test_multiple_observers_update(self) -> None:
        """
        Test that multiple observers receive the correct state update from the subject.

        Both Observer 1 and Observer 2 should receive the same update when the subject's state changes.
        """
        # Change subject's state to 20 and expect both observers to receive the update
        self.subject.change_state(20)
        self.assertEqual(self.observer1._subject_state, 20)
        self.assertEqual(self.observer2._subject_state, 20)

    def test_observer_detach(self) -> None:
        """
        Test that an observer does not receive updates after being detached.

        Observer 1 should stop receiving updates after being detached, but Observer 2 should still receive updates.
        """
        # Change state to 30 and verify that both observers get the update
        self.subject.change_state(30)
        self.assertEqual(self.observer1._subject_state, 30)
        self.assertEqual(self.observer2._subject_state, 30)

        # Detach observer1 and change the state again
        self.subject.detach(self.observer1)
        self.subject.change_state(40)

        # Observer 1 should no longer receive the update
        self.assertEqual(self.observer1._subject_state, 30)  # Still at the previous state
        # Observer 2 should still receive the update
        self.assertEqual(self.observer2._subject_state, 40)

    def test_observer_reattach(self) -> None:
        """
        Test that an observer receives updates again after being reattached.

        Observer 1 should receive updates again after being detached and reattached.
        """
        # Detach observer1, change the state, and then reattach it
        self.subject.detach(self.observer1)
        self.subject.change_state(50)
        self.assertEqual(self.observer1._subject_state, 0)  # Still at the previous state (before detachment)
        self.assertEqual(self.observer2._subject_state, 50)

        # Reattach observer1 and update the state again
        self.subject.attach(self.observer1)
        self.subject.change_state(60)
        self.assertEqual(self.observer1._subject_state, 60)
        self.assertEqual(self.observer2._subject_state, 60)
