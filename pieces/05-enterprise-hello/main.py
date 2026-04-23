"""Entry point. Wires the container and dispatches a single greeting."""
from greeter import (
    AbstractEventBus,
    AbstractGreeter,
    AbstractGreetingStrategy,
    CasualGreetingStrategy,
    ConcreteGreeter,
    DependencyInjectionContainer,
    EventBus,
)


def build_container() -> DependencyInjectionContainer:
    container = DependencyInjectionContainer()
    container.register_singleton(AbstractEventBus, EventBus())
    container.register_singleton(AbstractGreetingStrategy, CasualGreetingStrategy())
    container.register_class(AbstractGreeter, ConcreteGreeter)
    return container


def main() -> None:
    container = build_container()
    greeter = container.resolve(AbstractGreeter)
    greeter.greet()


if __name__ == "__main__":
    main()
