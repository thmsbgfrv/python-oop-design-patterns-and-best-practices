"""
Module Of Chain DP

This module implements the Chain of Responsibility design pattern, which allows handling requests by passing them
through a chain of handlers. Each handler processes the request or passes it to the next handler in the chain.

Classes:
    Handler (abstract class): Defines the interface for setting the next handler and handling the request.
    AbstractHandler (concrete class): Implements default chaining behavior and passes requests along the chain.
    LowLevelHandler (concrete class): Handles low-level requests.
    MidLevelHandler (concrete class): Handles mid-level requests.
    HighLevelHandler (concrete class): Handles high-level requests.
"""

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    Abstract Handler

    The base interface for all concrete handlers. Each handler should define how to set the next handler
    in the chain and how to process the request.

    Methods:
        set_next(handler: 'Handler') -> 'Handler':
            Set the next handler in the chain.
        handle(request: str) -> Optional[str]:
            Process the request or pass it to the next handler.
    """

    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        """Set the next handler in the chain."""

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        """Handle the request or pass it to the next handler in the chain."""


class AbstractHandler(Handler):
    """
    Abstract Handler Implementation

    Provides default chaining behavior. Can pass requests to the next handler in the chain if the current handler
    cannot process the request.

    Attributes:
        _next_handler (Optional[Handler]): The next handler in the chain, or None if there is no next handler.

    Methods:
        set_next(handler: 'Handler') -> 'Handler':
            Set the next handler in the chain and return the handler.
        handle(request: str) -> Optional[str]:
            Process the request or pass it to the next handler.
    """

    _next_handler: Optional[Handler] = None

    def set_next(self, handler: "Handler") -> "Handler":
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> Optional[str]:
        """Process the request or pass it to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class LowLevelHandler(AbstractHandler):
    """
    Low Level Handler

    Concrete handler that processes "low" level requests. If it cannot handle the request,
    it passes it to the next handler.

    Methods:
        handle(request: str) -> Optional[str]:
            Handle "low" level requests or pass the request to the next handler.
    """

    def handle(self, request: str) -> Optional[str]:
        """Handle 'low' level requests, or pass it to the next handler."""
        if request == "low":
            return f"LowLevelHandler: Handling {request}"

        return super().handle(request)


class MidLevelHandler(AbstractHandler):
    """
    Mid Level Handler

    Concrete handler that processes "mid" level requests. If it cannot handle the request,
    it passes it to the next handler.

    Methods:
        handle(request: str) -> Optional[str]:
            Handle "mid" level requests or pass the request to the next handler.
    """

    def handle(self, request: str) -> Optional[str]:
        """Handle 'mid' level requests, or pass it to the next handler."""
        if request == "mid":
            return f"MidLevelHandler: Handling {request}"
        return super().handle(request)


class HighLevelHandler(AbstractHandler):
    """
    High Level Handler

    Concrete handler that processes "high" level requests. If it cannot handle the request,
    it passes it to the next handler.

    Methods:
        handle(request: str) -> Optional[str]:
            Handle "high" level requests or pass the request to the next handler.
    """

    def handle(self, request: str) -> Optional[str]:
        """Handle 'high' level requests, or pass it to the next handler."""
        if request == "high":
            return f"HighLevelHandler: Handling {request}"
        return super().handle(request)
