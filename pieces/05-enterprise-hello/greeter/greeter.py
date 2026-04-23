"""The concrete greeter, wiring strategy + event bus behind AbstractGreeter."""
from __future__ import annotations

from .abstract import AbstractEventBus, AbstractGreeter, AbstractGreetingStrategy
from .events import GreetingEvent


class ConcreteGreeter(AbstractGreeter):
    def __init__(
        self,
        strategy: AbstractGreetingStrategy,
        event_bus: AbstractEventBus,
    ) -> None:
        self._strategy = strategy
        self._event_bus = event_bus

    def greet(self, subject: str = "") -> None:
        message = self._strategy.build_greeting(subject)
        print(message)
        self._event_bus.publish(
            GreetingEvent(subject=subject, rendered_message=message)
        )
