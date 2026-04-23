# 01 — shannon-switch

## 中文

> 开关拨到 ON。机器伸出手把它拨回 OFF。
> 全部。

1952 年，克劳德·香农造了一只盒子。盒面上只有一个开关。当你把开关拨到 ON，盒子里会伸出一只小手，把开关拨回 OFF，然后缩回去。这就是这台机器的全部功能。

`UselessMachine` 就是那只盒子在 Python 里的化身。`__new__` 返回 `None`——实例从未被真正构造出来。机器开了一瞬，刚好够把自己关掉。你抓不住它。你只能见证它曾经短暂存在过。

### 运行

```bash
python main.py
```

### 你会看到

```
switch: ON
switch: OFF
```

---

## English

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

### Run

```bash
python main.py
```

### What you'll see

```
switch: ON
switch: OFF
```
