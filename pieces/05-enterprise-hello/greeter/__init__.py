"""Enterprise-grade greeter subsystem."""

from .abstract import AbstractEventBus, AbstractGreeter, AbstractGreetingStrategy
from .container import DependencyInjectionContainer
from .events import EventBus, GreetingEvent
from .greeter import ConcreteGreeter
from .strategies import CasualGreetingStrategy, FormalGreetingStrategy

__all__ = [
    "AbstractEventBus",
    "AbstractGreeter",
    "AbstractGreetingStrategy",
    "CasualGreetingStrategy",
    "ConcreteGreeter",
    "DependencyInjectionContainer",
    "EventBus",
    "FormalGreetingStrategy",
    "GreetingEvent",
]
