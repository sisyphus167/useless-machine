# 06 — quine-and-vanish

## 中文

> *这件作品使用 `sandbox.fake_fs` —— 没有真实文件会受到伤害。*

一份文件把自己大声读出来，然后离开。读的部分是诚实的：你在标准输出里看到的源码，跟给你读的这份文件的源码逐字节相同。离开的部分也是诚实的——`os.remove` 真的被调用，真的作用在一个真实存在过的文件上；那个文件的路径会被打印到 stderr，调用完成之后那个文件确实不在了。

被删掉的是一份影子副本，由 `sandbox.fake_fs.ShadowFile` 产生。这不是 dry run。没有任何东西被 mock 掉。影子是 temp 目录里真实的文件，只活到被删除那一刻。原始的 `main.py`——你正在读的这份——从未被触碰；否则这件作品就不能被反复运行了。

### 前置条件

见根目录 README 的设置部分（`python -m venv .venv && pip install -e ".[dev]"`）—— 需要 `sandbox` 在 import 路径上。

### 运行

```bash
python main.py
```

（想跑几遍跑几遍。作品是安全的。）

### 你会看到

这份文件的源码被打印到 stdout。然后 stderr 上出现一行，写着刚被删除的那份影子文件的路径。

---

## English

> *This piece uses `sandbox.fake_fs` — no real files are harmed.*

A file reads itself out loud, and then leaves. The reading is honest: the 
source you see on standard output is byte-for-byte the source of the file 
that read it to you. The leaving is also honest — `os.remove` is really 
called on a real file that really existed at the path printed to stderr, 
and that file is really no longer there afterward.

The file that is deleted is a shadow copy, produced by `sandbox.fake_fs.ShadowFile`. 
This is not a dry run. Nothing is mocked. The shadow is a real file in a 
real temp directory, living exactly long enough to be deleted. The 
original `main.py` — the one you are reading — is never touched; the 
piece would not be safe to re-run otherwise.

### Prerequisites

See the root README for setup (`python -m venv .venv && pip install -e ".[dev]"`) — you need `sandbox` on the import path.

### Run

```bash
python main.py
```

(Run it as many times as you like. The piece is safe.)

### What you'll see

The source of this file, printed to stdout. Then, on stderr, a single line 
naming the path of the shadow file that was just deleted.
