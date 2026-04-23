# 02 — hello-antiworld

## 中文

> 它存在过。你也许看见了。现在它不曾存在。

经典的第一行程序，被撤销。`Hello, World!` 这几个字符被写入终端，只停留到勉强能被察觉那么一瞬（300 毫秒），然后被空格覆盖。光标回到第零列。屏幕之后的状态，跟从未打印过任何东西的屏幕毫无分别。

那个 sleep 是故意留的。太快，消息根本到不了你的眼睛——作品就变得不诚实（它真的什么都没做）。太慢，擦除就变成了刻意动作，而不是转瞬即逝的事件。300 毫秒大约是一次眨眼的时长。

### 运行

```bash
python main.py
```

### 你会看到

在你运行命令那一行，`Hello, World!` 闪一下，然后留下一个干净的 shell 提示符。这个效果在纯文本 transcript 里复现不出来——以后更新时建议补一份 `demo.gif`。

---

## English

> It existed. You might have seen it. Now it didn't.

The canonical first program, undone. The characters `Hello, World!` are 
written to the terminal, linger just long enough to be almost-perceived 
(300 ms), and are then overwritten with spaces. The cursor returns to 
column zero. The screen, afterwards, is indistinguishable from a screen 
where nothing was printed.

The sleep is deliberate. Too fast, and the message never reaches your 
eyes at all — then the piece is dishonest (it really did nothing). Too 
slow, and the erasure feels intentional rather than fugitive. 300 ms is 
about the blink of an eye.

### Run

```bash
python main.py
```

### What you'll see

A brief flash of `Hello, World!` on the line you ran it from, then a clean 
prompt. A `demo.gif` is recommended for the README on a future pass — the 
effect does not translate to a plain-text transcript.
