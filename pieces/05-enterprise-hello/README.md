# 05 — enterprise-hello

> `hello`

Two hundred lines of clean, decoupled, SOLID Python produce exactly one 
line of output. Every abstraction is real — real Protocols, a real DI 
container that does real reflection-based constructor wiring, a real 
event bus that really publishes a real `GreetingEvent` to real (zero) 
subscribers. None of it is doing anything ironic. That is the joke: it 
is all extremely serious about saying hello.

You could add twelve more layers and the output would not change. You 
could remove ten and the output would not change. The architecture is 
not load-bearing. The architecture is the piece.

See [`architecture.md`](architecture.md) for the class diagram.

## Run

```bash
python main.py
```

## What you'll see

```
hello
```
