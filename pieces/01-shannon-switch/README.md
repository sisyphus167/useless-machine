# 01 — shannon-switch

> The switch is flipped ON. The machine reaches out and flips it OFF.
> That is the whole of it.

In 1952, Claude Shannon built a box. On top of the box was a single switch. 
When you flipped the switch ON, a small hand would emerge from inside the 
box, flip the switch OFF, and retract. This was the whole function of the 
machine.

`UselessMachine` is that box, in Python. `__new__` returns `None` — no 
instance is ever constructed. The machine turns on just long enough to 
turn itself off. You cannot hold it. You can only witness its having 
briefly been.

## Run

```bash
python main.py
```

## What you'll see

```
switch: ON
switch: OFF
```
