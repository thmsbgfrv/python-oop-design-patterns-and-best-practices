"""
Test Module for Chain of Responsibility Pattern

This module contains unit tests for the Chain of Responsibility pattern, specifically testing the
LowLevelHandler, MidLevelHandler, and HighLevelHandler classes. The tests ensure that each handler
in the chain processes requests or passes them to the next handler appropriately.

Classes:
    TestChainOfResponsibility (unittest.TestCase):
        Unit tests for testing different handlers in the Chain of Responsibility.
"""

import unittest

from oop.patterns.behavioral.chain import HighLevelHandler, LowLevelHandler, MidLevelHandler


class TestChainOfResponsibility(unittest.TestCase):
    """
    TestChainOfResponsibility

    Unit tests for the Chain of Responsibility pattern. Tests the behavior of LowLevelHandler,
    MidLevelHandler, and HighLevelHandler in processing different types of requests.

    Methods:
        setUp() -> None:
            Sets up the chain of handlers before each test case.
        test_low_handler() -> None:
            Tests if the low-level handler processes the "low" request.
        test_mid_handler() -> None:
            Tests if the mid-level handler processes the "mid" request.
        test_high_handler() -> None:
            Tests if the high-level handler processes the "high" request.
        test_no_handler() -> None:
            Tests if none of the handlers can process an "unknown" request.
    """

    def setUp(self) -> None:
        """
        Sets up the chain of handlers before each test case.

        The chain is configured as low -> mid -> high, where requests
        are passed along this chain until one of the handlers can process them.
        """
        self.low: LowLevelHandler = LowLevelHandler()
        self.mid: MidLevelHandler = MidLevelHandler()
        self.high: HighLevelHandler = HighLevelHandler()

        # Setup chain: low -> mid -> high
        self.low.set_next(self.mid).set_next(self.high)

    def test_low_handler(self) -> None:
        """
        Tests if the LowLevelHandler processes the "low" request.

        The request "low" should be handled by the LowLevelHandler.
        """
        self.assertEqual(self.low.handle("low"), "LowLevelHandler: Handling low")

    def test_mid_handler(self) -> None:
        """
        Tests if the MidLevelHandler processes the "mid" request.

        The request "mid" should be handled by the MidLevelHandler,
        even when passed to the LowLevelHandler first.
        """
        self.assertEqual(self.low.handle("mid"), "MidLevelHandler: Handling mid")

    def test_high_handler(self) -> None:
        """
        Tests if the HighLevelHandler processes the "high" request.

        The request "high" should be handled by the HighLevelHandler,
        even when passed to the LowLevelHandler first.
        """
        self.assertEqual(self.low.handle("high"), "HighLevelHandler: Handling high")

    def test_no_handler(self) -> None:
        """
        Tests if no handler processes an "unknown" request.

        If none of the handlers can process the request, the response should be None.
        """
        self.assertIsNone(self.low.handle("unknown"))
