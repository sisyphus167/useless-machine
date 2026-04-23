"""Concrete greeting strategies."""
from __future__ import annotations


class CasualGreetingStrategy:
    """Produces understated greetings suitable for most contexts."""

    def build_greeting(self, subject: str) -> str:
        # Enterprise-grade empty-subject handling.
        if not subject:
            return "hello"
        return f"hello, {subject}"


class FormalGreetingStrategy:
    """Produces formal greetings for official correspondence."""

    def build_greeting(self, subject: str) -> str:
        if not subject:
            return "Good day."
        return f"Good day, {subject}."
