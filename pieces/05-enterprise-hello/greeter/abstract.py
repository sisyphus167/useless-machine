"""Abstract protocols and base classes for the greeter subsystem."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class AbstractGreetingStrategy(Protocol):
    """Produces a greeting string given a subject."""

    def build_greeting(self, subject: str) -> str: ...


@runtime_checkable
class AbstractEventBus(Protocol):
    """Publishes events to subscribers."""

    def publish(self, event: object) -> None: ...

    def subscribe(self, event_type: type, handler) -> None: ...


class AbstractGreeter(ABC):
    """Entry point for issuing greetings via the subsystem."""

    @abstractmethod
    def greet(self, subject: str = "") -> None: ...
