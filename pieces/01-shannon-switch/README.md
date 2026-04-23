# 01 — shannon-switch

## 中文

> 开关拨到 ON。机器伸出手把它拨回 OFF。
> 全部。

1952 年，克劳德·香农造了一只盒子。盒面上只有一个开关。当你把开关拨到 ON，盒子里会伸出一只小手，把开关拨回 OFF，然后缩回去。这就是这台机器的全部功能。

`UselessMachine` 就是那只盒子在 Python 里的化身。调用它会拉起一个真实的子进程——那就是机器唯一一次的肉身显形，带着自己的 PID 短暂活过。紧接着那只手伸出来把它按掉。`__new__` 返回 `None`，Python 这一层不留下任何对象；只剩那个 PID 曾经活过的痕迹。

### 运行

```bash
python main.py
```

### 你会看到

```
switch: ON  [pid 12345 running]
...a hand emerges from under the lid...
...and kills pid 12345.
switch: OFF
```

（PID 每次运行都不同。`switch: ON` 时真有一个 Python 子进程被拉起来；中间那一拍就是 `process.terminate()`——那只手真的按到了开关。 / The PID changes each run. On `switch: ON` a real Python subprocess is spawned; the middle beat is `process.terminate()` — the hand really pushing the switch.）

---

## English

> The switch is flipped ON. The machine reaches out and flips it OFF.
> That is the whole of it.

In 1952, Claude Shannon built a box. On top of the box was a single switch. 
When you flipped the switch ON, a small hand would emerge from inside the 
box, flip the switch OFF, and retract. This was the whole function of the 
machine.

`UselessMachine` is that box, in Python. Calling it spawns a real 
subprocess — the machine's one brief incarnation, carrying its own 
PID. The hand then emerges and kills it. `__new__` returns `None`, 
so no Python-side object survives — only the trace of a process that 
briefly was.

### Run

```bash
python main.py
```

### What you'll see

```
switch: ON  [pid 12345 running]
...a hand emerges from under the lid...
...and kills pid 12345.
switch: OFF
```

（PID 每次运行都不同。`switch: ON` 时真有一个 Python 子进程被拉起来；中间那一拍就是 `process.terminate()`——那只手真的按到了开关。 / The PID changes each run. On `switch: ON` a real Python subprocess is spawned; the middle beat is `process.terminate()` — the hand really pushing the switch.）
