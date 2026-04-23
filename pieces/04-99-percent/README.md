# 04 — 99-percent

## 中文

> 马上就好。

一个进度条，它本身没有任何过错，但它完不成。它从零诚实地爬到九十九。然后停住。ETA 每秒左右刷新一次，给你一个稳定、令人安心的答复：*大约还剩三秒*。你想看多久，这个答复就会持续为真多久。

进度条会抖——回退零点几个百分点，然后恢复——因为软件里没有什么是真正静止的。想放弃，按 Ctrl-C；作品自己不会放弃。

### 运行

```bash
python main.py
```

（看够了就按 Ctrl-C。）

### 你会看到

进度条大约三秒钟爬到 99.0%，然后无限期停留在那里，偶尔抖一下、回退零点几个百分点再回来。ETA：大约还剩三秒。

建议配一份 `demo.gif`——那种"抖"感用看比用读更容易传达。

---

## English

> Any minute now.

A progress bar that, through no fault of its own, cannot complete. It 
climbs honestly from zero to ninety-nine. Then it stops. The ETA, which 
updates every second or so, gives you a consistent and reassuring answer: 
*about three seconds remaining.* This will remain true for as long as you 
care to watch.

The bar jitters — a fraction of a percent back, then recovering — because 
nothing in software is ever quite still. Press Ctrl-C to give up; the 
piece will not.

### Run

```bash
python main.py
```

(Press Ctrl-C when you've had enough.)

### What you'll see

A progress bar that climbs to 99.0% in roughly three seconds, then stays 
there indefinitely, occasionally shivering a fraction of a percent down 
and back. ETA: about three seconds remaining.

A `demo.gif` is recommended — the shiver is easier to feel than to describe.
