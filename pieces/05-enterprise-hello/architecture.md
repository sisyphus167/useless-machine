# Architecture

```
                ┌──────────────────────────────────────┐
                │           main.py                    │
                │  builds container, resolves          │
                │  AbstractGreeter, calls .greet()     │
                └─────────────────┬────────────────────┘
                                  │
                                  ▼
                ┌──────────────────────────────────────┐
                │  DependencyInjectionContainer        │
                │  • register_singleton(iface, inst)   │
                │  • register_class(iface, impl)       │
                │  • resolve(iface) → auto-wires ctor  │
                └───┬───────────────┬────────────┬─────┘
                    │               │            │
                    ▼               ▼            ▼
         AbstractEventBus   AbstractGreeting   AbstractGreeter
                │           Strategy                │
                ▼               │                   ▼
           EventBus             ▼             ConcreteGreeter
           (pub/sub)     CasualGreetingStrategy      │
                                                    │ depends on
                                                    ▼
                                    (strategy, event_bus)
                                                    │
                                                    │ publishes
                                                    ▼
                                              GreetingEvent
                                          (subject, message)
```

Nine classes, four files of wiring, two Protocols, one ABC, one dataclass, 
one dependency-injection container, one pub/sub event bus.

Observable output: `hello`.
