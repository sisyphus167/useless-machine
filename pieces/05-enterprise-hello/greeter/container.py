"""A lightweight dependency-injection container.

Supports:
    - singleton registration by type
    - factory registration by type
    - resolution by type with automatic constructor wiring
"""
from __future__ import annotations

import inspect
from typing import Any, Callable


class DependencyInjectionContainer:
    def __init__(self) -> None:
        self._singletons: dict[type, Any] = {}
        self._factories: dict[type, Callable[[], Any]] = {}

    def register_singleton(self, interface: type, instance: Any) -> None:
        self._singletons[interface] = instance

    def register_factory(self, interface: type, factory: Callable[[], Any]) -> None:
        self._factories[interface] = factory

    def register_class(self, interface: type, implementation: type) -> None:
        """Resolve a concrete class with auto-wired constructor args."""
        self._factories[interface] = lambda: self._build(implementation)

    def resolve(self, interface: type) -> Any:
        if interface in self._singletons:
            return self._singletons[interface]
        if interface in self._factories:
            return self._factories[interface]()
        raise KeyError(f"No registration for {interface!r}")

    def _build(self, cls: type) -> Any:
        import typing
        hints = typing.get_type_hints(cls.__init__)
        sig = inspect.signature(cls.__init__)
        kwargs: dict[str, Any] = {}
        for name, param in sig.parameters.items():
            if name == "self" or param.annotation is inspect.Parameter.empty:
                continue
            annotation = hints.get(name, param.annotation)
            kwargs[name] = self.resolve(annotation)
        return cls(**kwargs)
