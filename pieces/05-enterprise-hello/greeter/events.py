"""Event bus and greeting event definitions."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class GreetingEvent:
    """Emitted when a greeting has been successfully delivered."""

    subject: str
    rendered_message: str


class EventBus:
    """A simple synchronous in-process publisher/subscriber."""

    def __init__(self) -> None:
        self._subscribers: dict[type, list[Callable[[object], None]]] = defaultdict(list)

    def publish(self, event: object) -> None:
        for handler in self._subscribers.get(type(event), []):
            handler(event)

    def subscribe(self, event_type: type, handler: Callable[[object], None]) -> None:
        self._subscribers[event_type].append(handler)
