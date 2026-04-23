# 05 — enterprise-hello

## 中文

> `hello`

两百行干净、解耦、SOLID 的 Python 产生恰好一行输出。每一个抽象都是真的——真的 Protocol、真的做基于反射的构造函数注入的 DI 容器、真的把真的 `GreetingEvent` 发布给真实（零个）订阅者的事件总线。没有一处是在做反讽动作。笑点就在这里：它极其认真地说了一声 hello。

你再往上加十二层，输出不会变。你拆掉十层，输出也不会变。架构不承重。架构本身就是作品。

类图见 [`architecture.md`](architecture.md)。

### 运行

```bash
python main.py
```

### 你会看到

```
hello
```

---

## English

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

### Run

```bash
python main.py
```

### What you'll see

```
hello
```
