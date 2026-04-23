# Useless Machine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the initial public-ready state of the `useless-machine` repo: the 7-piece starter lineup (01–07), the shared `sandbox/` library, root README/CONTRIBUTING, and a `pyproject.toml` that makes `import sandbox` work after `pip install -e .`.

**Architecture:** Each piece is an independent directory under `pieces/`. The `sandbox/` package is the only shared code. Pieces don't share abstractions with each other and never import from each other. Only piece 06 depends on `sandbox/`. Tests exist only for `sandbox/` (it's safety-critical infrastructure); pieces themselves are verified manually because they're concept art, not functions.

**Tech Stack:** Python 3.11+, pytest (for sandbox tests only), Jupyter + matplotlib (for piece 03), setuptools (build backend).

---

## File Structure

```
useless-machine/
├── README.md                                  # Task 10
├── CONTRIBUTING.md                            # Task 10
├── pyproject.toml                             # Task 1
├── .gitignore                                 # Task 1
├── docs/superpowers/                          # already exists (spec, this plan)
├── sandbox/                                   # Task 2
│   ├── __init__.py
│   └── fake_fs.py
├── tests/                                     # Task 2
│   └── test_fake_fs.py
└── pieces/
    ├── 01-shannon-switch/{README,main.py}     # Task 3
    ├── 02-hello-antiworld/{README,main.py}    # Task 4
    ├── 03-sisyphus-sort/{README,*.ipynb}      # Task 5
    ├── 04-99-percent/{README,main.py}         # Task 6
    ├── 05-enterprise-hello/                   # Task 7
    │   ├── README.md
    │   ├── architecture.md
    │   ├── main.py
    │   └── greeter/
    │       ├── __init__.py
    │       ├── abstract.py
    │       ├── strategies.py
    │       ├── events.py
    │       ├── container.py
    │       └── greeter.py
    ├── 06-quine-and-vanish/{README,main.py}   # Task 8
    └── 07-pypi-useless/                       # Task 9
        ├── README.md
        ├── pyproject.toml                     # inner package manifest
        └── src/useless/__init__.py
```

**Responsibility notes:**
- `sandbox/fake_fs.py` is the only file whose correctness matters for physical safety; it gets real tests.
- Each piece's `main.py` or `*.ipynb` is self-contained. No cross-piece imports.
- Root `pyproject.toml` exists so `pip install -e .` makes `from sandbox.fake_fs import ShadowFile` work from anywhere (piece 06 needs this).
- `pieces/07-pypi-useless/pyproject.toml` is a **separate** build manifest for the inner `useless` PyPI package. Distinct from the repo-root one.

---

## Task 1: Repository skeleton

**Files:**
- Create: `pyproject.toml`
- Create: `.gitignore`
- Create: `sandbox/` (empty dir placeholder; task 2 fills it)
- Create: `pieces/` (empty dir placeholder)
- Create: `tests/` (empty dir placeholder)

- [ ] **Step 1: Create `pyproject.toml` at repo root**

```toml
[project]
name = "useless-machine"
version = "0.0.1"
description = "A collection of useless Python code in the spirit of Shannon's Ultimate Machine."
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "matplotlib>=3.7",
    "jupyter>=1.0",
    "ipykernel>=6.0",
    "build>=1.0",
]

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["."]
include = ["sandbox*"]
exclude = ["pieces*", "tests*", "docs*"]
```

- [ ] **Step 2: Create `.gitignore`**

```
__pycache__/
*.pyc
*.pyo
.venv/
venv/
.ipynb_checkpoints/
*.egg-info/
dist/
build/
.pytest_cache/
.DS_Store
```

- [ ] **Step 3: Create the empty directories with `.gitkeep`**

Create three empty files so the directories exist in git:

```bash
mkdir -p sandbox pieces tests
touch sandbox/.gitkeep pieces/.gitkeep tests/.gitkeep
```

(We'll delete `sandbox/.gitkeep` and `tests/.gitkeep` in Task 2 once they have real files. `pieces/.gitkeep` will be removed in Task 3 when the first piece arrives.)

- [ ] **Step 4: Create a fresh Python venv and install in editable mode**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Expected: `pip install` succeeds. `sandbox` is empty so importing it will fail — that's fine for now; Task 2 populates it.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml .gitignore sandbox/.gitkeep pieces/.gitkeep tests/.gitkeep
git commit -m "chore: initial repo skeleton (pyproject, dirs, gitignore)"
```

---

## Task 2: `sandbox.fake_fs` with TDD

**Files:**
- Create: `sandbox/__init__.py`
- Create: `sandbox/fake_fs.py`
- Create: `tests/test_fake_fs.py`
- Delete: `sandbox/.gitkeep`, `tests/.gitkeep`

**Design:** `ShadowFile(path)` creates a real temp-directory copy of a file. Operations like `.delete()`, `.read_text()`, `.write_text()`, `.exists()` operate on the shadow — they call real `os.remove` etc. — but the original file at `path` is untouched. The shadow lives under `tempfile.gettempdir()/useless-machine-shadows/<hash>/`.

**Key invariants to test:**
1. Constructing a `ShadowFile` for an existing file produces a separate file with the same content.
2. `.delete()` actually removes the shadow (real `os.remove`) and leaves the original alone.
3. `.read_text()` and `.write_text()` work on the shadow.
4. `.exists()` reflects real FS state of the shadow.
5. `.path` returns the shadow path (so pieces printing `"deleted {me.path}"` feel authentic).
6. Constructing a `ShadowFile` for a path that doesn't exist raises `FileNotFoundError`.

- [ ] **Step 1: Write the test file with all six tests (they will all fail)**

`tests/test_fake_fs.py`:

```python
import os
from pathlib import Path

import pytest

from sandbox.fake_fs import ShadowFile


def test_shadow_copies_content_from_original(tmp_path):
    original = tmp_path / "real.txt"
    original.write_text("hello")

    shadow = ShadowFile(original)

    assert shadow.read_text() == "hello"
    assert Path(shadow.path) != original


def test_delete_removes_shadow_but_not_original(tmp_path):
    original = tmp_path / "real.txt"
    original.write_text("hello")

    shadow = ShadowFile(original)
    shadow_path = Path(shadow.path)
    assert shadow_path.exists()

    shadow.delete()

    assert not shadow_path.exists()  # shadow is really gone
    assert original.exists()         # original is untouched
    assert original.read_text() == "hello"


def test_write_text_writes_to_shadow_only(tmp_path):
    original = tmp_path / "real.txt"
    original.write_text("original content")

    shadow = ShadowFile(original)
    shadow.write_text("shadow content")

    assert shadow.read_text() == "shadow content"
    assert original.read_text() == "original content"


def test_exists_reflects_shadow_state(tmp_path):
    original = tmp_path / "real.txt"
    original.write_text("hi")

    shadow = ShadowFile(original)
    assert shadow.exists() is True

    shadow.delete()
    assert shadow.exists() is False


def test_path_returns_shadow_path_not_original(tmp_path):
    original = tmp_path / "real.txt"
    original.write_text("x")

    shadow = ShadowFile(original)
    assert Path(shadow.path).exists()
    assert str(shadow.path) != str(original)


def test_missing_original_raises(tmp_path):
    missing = tmp_path / "does-not-exist.txt"
    with pytest.raises(FileNotFoundError):
        ShadowFile(missing)
```

- [ ] **Step 2: Create `sandbox/__init__.py` (empty is fine)**

```python
"""Safe imitations of destructive operations.

Pieces in this repo that would otherwise touch real files, remotes, or mailboxes
use this package instead. The imitations are real (they really call os.remove,
really push to a real git repo, really send through a real SMTP server) — they
just target sandboxed resources.
"""
```

- [ ] **Step 3: Run tests — expect all to fail with ImportError**

```bash
pytest tests/test_fake_fs.py -v
```

Expected: 6 errors, all complaining about `No module named 'sandbox.fake_fs'` or similar.

- [ ] **Step 4: Implement `sandbox/fake_fs.py`**

```python
"""Shadow-file utilities: real file operations on real (but sandboxed) files."""
from __future__ import annotations

import hashlib
import os
import shutil
import tempfile
from pathlib import Path

_SHADOW_ROOT = Path(tempfile.gettempdir()) / "useless-machine-shadows"


class ShadowFile:
    """A real file copy of `source`, living in a temp directory.

    Operations on the ShadowFile really execute (os.remove, Path.write_text,
    etc.) — they just target the shadow copy. The original is never touched.
    """

    def __init__(self, source: str | os.PathLike) -> None:
        source_path = Path(source)
        if not source_path.exists():
            raise FileNotFoundError(source_path)

        _SHADOW_ROOT.mkdir(parents=True, exist_ok=True)
        # Use a content+path hash so repeated shadowing of the same file
        # produces a fresh copy each time (important for `delete()` in tests).
        digest = hashlib.sha256(
            f"{source_path.resolve()}:{os.urandom(8).hex()}".encode()
        ).hexdigest()[:16]
        shadow_dir = _SHADOW_ROOT / digest
        shadow_dir.mkdir(parents=True, exist_ok=True)

        self._path = shadow_dir / source_path.name
        shutil.copy2(source_path, self._path)

    @property
    def path(self) -> Path:
        return self._path

    def exists(self) -> bool:
        return self._path.exists()

    def read_text(self) -> str:
        return self._path.read_text()

    def write_text(self, content: str) -> None:
        self._path.write_text(content)

    def delete(self) -> None:
        os.remove(self._path)
```

- [ ] **Step 5: Re-run tests — expect all to pass**

```bash
pytest tests/test_fake_fs.py -v
```

Expected: 6 passed.

- [ ] **Step 6: Clean up the `.gitkeep` placeholders**

```bash
rm sandbox/.gitkeep tests/.gitkeep
```

- [ ] **Step 7: Commit**

```bash
git add sandbox/__init__.py sandbox/fake_fs.py tests/test_fake_fs.py
git rm sandbox/.gitkeep tests/.gitkeep
git commit -m "feat(sandbox): add fake_fs.ShadowFile with tests"
```

---

## Task 3: Piece 01 — `shannon-switch`

**Files:**
- Create: `pieces/01-shannon-switch/README.md`
- Create: `pieces/01-shannon-switch/main.py`
- Delete: `pieces/.gitkeep`

**Design:** The purest Python homage: a class that, upon construction, prints "switch: ON" and immediately prints "switch: OFF" — and never actually produces an instance. `UselessMachine()` returns `None`.

- [ ] **Step 1: Write `pieces/01-shannon-switch/main.py`**

```python
"""Shannon's Ultimate Machine, in Python."""


class UselessMachine:
    """Its only purpose is to turn itself off.

    The switch turns on, and in the same breath the machine reaches out
    and turns it off. No instance is ever returned — the machine never
    really exists, only the trace of it having existed.
    """

    def __new__(cls):
        print("switch: ON",  flush=True)
        print("switch: OFF", flush=True)
        return None


if __name__ == "__main__":
    UselessMachine()
```

- [ ] **Step 2: Write `pieces/01-shannon-switch/README.md`**

```markdown
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
```

- [ ] **Step 3: Run it**

```bash
cd pieces/01-shannon-switch
python main.py
```

Expected output (exactly):
```
switch: ON
switch: OFF
```

- [ ] **Step 4: Commit**

```bash
cd ../..  # back to repo root
git rm pieces/.gitkeep
git add pieces/01-shannon-switch/
git commit -m "feat(01): shannon-switch"
```

---

## Task 4: Piece 02 — `hello-antiworld`

**Files:**
- Create: `pieces/02-hello-antiworld/README.md`
- Create: `pieces/02-hello-antiworld/main.py`

**Design:** Print "Hello, World!", pause long enough for the terminal to render it (~300ms), then emit `\r` + spaces + `\r` to erase the line. Screen ends clean.

- [ ] **Step 1: Write `pieces/02-hello-antiworld/main.py`**

```python
"""Hello, World! — and then nothing."""
import sys
import time

MESSAGE = "Hello, World!"
LINGER_SECONDS = 0.3


def main() -> None:
    sys.stdout.write(MESSAGE)
    sys.stdout.flush()
    time.sleep(LINGER_SECONDS)
    sys.stdout.write("\r" + " " * len(MESSAGE) + "\r")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Write `pieces/02-hello-antiworld/README.md`**

```markdown
# 02 — hello-antiworld

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

## Run

```bash
python main.py
```

## What you'll see

A brief flash of `Hello, World!` on the line you ran it from, then a clean 
prompt. A `demo.gif` is recommended for the README on a future pass — the 
effect does not translate to a plain-text transcript.
```

- [ ] **Step 3: Run it and verify visually**

```bash
cd pieces/02-hello-antiworld
python main.py
```

Expected: you briefly see "Hello, World!" and then the line is blank when the command returns. If run in CI or captured output (e.g. `python main.py | cat`), the erase sequence won't render visibly — that's fine; the piece is about terminal display, not log output.

- [ ] **Step 4: Commit**

```bash
cd ../..
git add pieces/02-hello-antiworld/
git commit -m "feat(02): hello-antiworld"
```

---

## Task 5: Piece 03 — `sisyphus-sort` (notebook)

**Files:**
- Create: `pieces/03-sisyphus-sort/README.md`
- Create: `pieces/03-sisyphus-sort/sisyphus_sort.ipynb`

**Design:** One Jupyter notebook that alternates sorting and shuffling a small array forever, visualized as an animated bar chart via `matplotlib.animation.FuncAnimation`. The animation renders inline (HTML) so GitHub preview / nbviewer shows it.

The notebook has exactly 4 cells:
1. Markdown — manifesto
2. Code — imports + constants
3. Code — the generator + animation logic
4. Code — render call returning the animation HTML

- [ ] **Step 1: Create `pieces/03-sisyphus-sort/sisyphus_sort.ipynb`**

The easiest way to author this is to write the JSON directly. Use this exact content:

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 03 — sisyphus-sort\n",
    "\n",
    "> He sorts the array. It is good. He turns his back. It is not good.\n",
    "\n",
    "A bar chart. Thirty integers. They get sorted, from shortest to tallest, by a bubble sort that takes its time so you can watch. When the sort completes, an unseen hand reaches into the array and shuffles it back to chaos. Then the sort begins again.\n",
    "\n",
    "The loop never terminates. The animation below will run for as many frames as you let it. Each cycle takes about fifteen seconds. Nothing about the array is ever different on the other side of a cycle — the initial distribution is the same, the terminal distribution is the same. Only Sisyphus's legs are tired.\n",
    "\n",
    "*Reference: Camus, 1942; Knuth, 1968.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.animation import FuncAnimation\n",
    "from IPython.display import HTML\n",
    "\n",
    "N = 30\n",
    "CYCLES = 4  # how many sort-then-shuffle cycles to render"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bubble_sort_frames(arr):\n",
    "    n = len(arr)\n",
    "    for i in range(n):\n",
    "        for j in range(n - i - 1):\n",
    "            if arr[j] > arr[j + 1]:\n",
    "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n",
    "            yield list(arr)\n",
    "\n",
    "\n",
    "def shuffle_frames(arr):\n",
    "    # one swap per frame so the reversal is visible, not instant\n",
    "    for _ in range(len(arr) * 2):\n",
    "        i = random.randrange(len(arr))\n",
    "        j = random.randrange(len(arr))\n",
    "        arr[i], arr[j] = arr[j], arr[i]\n",
    "        yield list(arr)\n",
    "\n",
    "\n",
    "def sisyphus(cycles):\n",
    "    arr = list(range(1, N + 1))\n",
    "    random.shuffle(arr)\n",
    "    yield list(arr)\n",
    "    for _ in range(cycles):\n",
    "        yield from bubble_sort_frames(arr)\n",
    "        yield from shuffle_frames(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "random.seed(0)\n",
    "frames = list(sisyphus(CYCLES))\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(8, 3))\n",
    "bars = ax.bar(range(N), frames[0], color=\"#444\")\n",
    "ax.set_ylim(0, N + 1)\n",
    "ax.set_xticks([])\n",
    "ax.set_yticks([])\n",
    "for spine in ax.spines.values():\n",
    "    spine.set_visible(False)\n",
    "\n",
    "\n",
    "def draw(heights):\n",
    "    for bar, h in zip(bars, heights):\n",
    "        bar.set_height(h)\n",
    "    return bars\n",
    "\n",
    "\n",
    "anim = FuncAnimation(fig, draw, frames=frames, interval=40, blit=False)\n",
    "plt.close(fig)\n",
    "HTML(anim.to_jshtml())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

- [ ] **Step 2: Write `pieces/03-sisyphus-sort/README.md`**

```markdown
# 03 — sisyphus-sort

> The boulder. The hill. The sort.

See [`sisyphus_sort.ipynb`](sisyphus_sort.ipynb).

A bar chart of thirty integers, bubble-sorted to order, then shuffled back 
to chaos, forever. Each cycle takes about fifteen seconds. The animation 
renders inline; on GitHub, the notebook preview will display it.

## Run

```bash
jupyter lab sisyphus_sort.ipynb
# then: Restart & Run All
```

Or view on GitHub / nbviewer — the embedded JSHTML animation plays without 
a Python kernel.
```

- [ ] **Step 3: Verify the notebook runs end-to-end**

```bash
cd pieces/03-sisyphus-sort
jupyter nbconvert --to notebook --execute sisyphus_sort.ipynb --output sisyphus_sort.ipynb
```

Expected: command completes without error; the notebook now has populated `outputs` with an HTML animation in the last cell. If you want to verify visually, open it in Jupyter Lab and run all cells.

- [ ] **Step 4: Commit**

```bash
cd ../..
git add pieces/03-sisyphus-sort/
git commit -m "feat(03): sisyphus-sort notebook"
```

---

## Task 6: Piece 04 — `99-percent`

**Files:**
- Create: `pieces/04-99-percent/README.md`
- Create: `pieces/04-99-percent/main.py`

**Design:** Progress bar renders at 40 chars wide, climbs 0→99 with random small increments and small random sleeps (so it feels like a real download). Once it hits 99.0, it stays there and jitters — each "tick" it sleeps 0.8–1.5s, then re-renders with a tiny subtraction (0, 0, 0, 0.1, or 0.2 off 99) so the bar occasionally shivers back a fraction before recovering. ETA suffix is always "about 3 seconds remaining". Ctrl-C exits cleanly.

- [ ] **Step 1: Write `pieces/04-99-percent/main.py`**

```python
"""A progress bar that never reaches 100%."""
import random
import sys
import time

WIDTH = 40
ETA_TEXT = "about 3 seconds remaining"


def render(pct: float, suffix: str = "") -> None:
    filled = int(pct * WIDTH / 100)
    bar = "█" * filled + "·" * (WIDTH - filled)
    line = f"\r[{bar}] {pct:5.1f}%  {suffix}"
    # Pad with spaces to overwrite any previous longer suffix
    sys.stdout.write(line.ljust(WIDTH + 30))
    sys.stdout.flush()


def climb_to_99() -> None:
    pct = 0.0
    while pct < 99.0:
        pct = min(99.0, pct + random.uniform(0.5, 2.0))
        render(pct)
        time.sleep(random.uniform(0.02, 0.08))


def linger_at_99() -> None:
    while True:
        jitter = random.choice([0.0, 0.0, 0.0, 0.1, 0.2])
        render(99.0 - jitter, suffix=ETA_TEXT)
        time.sleep(random.uniform(0.8, 1.5))


def main() -> None:
    try:
        climb_to_99()
        linger_at_99()
    except KeyboardInterrupt:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Write `pieces/04-99-percent/README.md`**

```markdown
# 04 — 99-percent

> Any minute now.

A progress bar that, through no fault of its own, cannot complete. It 
climbs honestly from zero to ninety-nine. Then it stops. The ETA, which 
updates every second or so, gives you a consistent and reassuring answer: 
*about three seconds remaining.* This will remain true for as long as you 
care to watch.

The bar jitters — a fraction of a percent back, then recovering — because 
nothing in software is ever quite still. Press Ctrl-C to give up; the 
piece will not.

## Run

```bash
python main.py
```

(Press Ctrl-C when you've had enough.)

## What you'll see

A progress bar that climbs to 99.0% in roughly three seconds, then stays 
there indefinitely, occasionally shivering a fraction of a percent down 
and back. ETA: about three seconds remaining.

A `demo.gif` is recommended — the shiver is easier to feel than to describe.
```

- [ ] **Step 3: Run it and verify**

```bash
cd pieces/04-99-percent
timeout 10 python main.py || true
echo ""  # clean up line
```

Expected: progress bar climbs to 99.0% within ~3 seconds and continues shivering until `timeout` kills it at 10 seconds. No crash, no traceback (timeout's SIGTERM may or may not print — that's fine).

- [ ] **Step 4: Commit**

```bash
cd ../..
git add pieces/04-99-percent/
git commit -m "feat(04): 99-percent"
```

---

## Task 7: Piece 05 — `enterprise-hello`

**Files:**
- Create: `pieces/05-enterprise-hello/README.md`
- Create: `pieces/05-enterprise-hello/architecture.md`
- Create: `pieces/05-enterprise-hello/main.py`
- Create: `pieces/05-enterprise-hello/greeter/__init__.py`
- Create: `pieces/05-enterprise-hello/greeter/abstract.py`
- Create: `pieces/05-enterprise-hello/greeter/strategies.py`
- Create: `pieces/05-enterprise-hello/greeter/events.py`
- Create: `pieces/05-enterprise-hello/greeter/container.py`
- Create: `pieces/05-enterprise-hello/greeter/greeter.py`

**Design:** The only observable behavior is `python main.py` printing exactly `hello`. Underneath: ~200 LOC across 6 files implementing abstract protocols, a dependency-injection container, strategy pattern, and an event bus. The point is the ratio.

Structure:
- `abstract.py`: `AbstractGreetingStrategy` (Protocol), `AbstractGreeter` (ABC), `AbstractEventBus` (Protocol)
- `strategies.py`: `CasualGreetingStrategy`, `FormalGreetingStrategy` (we'll use casual)
- `events.py`: `GreetingEvent` dataclass, `EventBus` publisher/subscriber
- `container.py`: `DependencyInjectionContainer` with registration + resolution
- `greeter.py`: `ConcreteGreeter` — depends on strategy + event bus, calls strategy to build a message, publishes an event, prints the message
- `main.py`: wires the container, resolves the greeter, invokes `.greet()`

- [ ] **Step 1: Create `pieces/05-enterprise-hello/greeter/__init__.py`**

```python
"""Enterprise-grade greeter subsystem."""

from .abstract import AbstractEventBus, AbstractGreeter, AbstractGreetingStrategy
from .container import DependencyInjectionContainer
from .events import EventBus, GreetingEvent
from .greeter import ConcreteGreeter
from .strategies import CasualGreetingStrategy, FormalGreetingStrategy

__all__ = [
    "AbstractEventBus",
    "AbstractGreeter",
    "AbstractGreetingStrategy",
    "CasualGreetingStrategy",
    "ConcreteGreeter",
    "DependencyInjectionContainer",
    "EventBus",
    "FormalGreetingStrategy",
    "GreetingEvent",
]
```

- [ ] **Step 2: Create `pieces/05-enterprise-hello/greeter/abstract.py`**

```python
"""Abstract protocols and base classes for the greeter subsystem."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class AbstractGreetingStrategy(Protocol):
    """Produces a greeting string given a subject."""

    def build_greeting(self, subject: str) -> str: ...


@runtime_checkable
class AbstractEventBus(Protocol):
    """Publishes events to subscribers."""

    def publish(self, event: object) -> None: ...

    def subscribe(self, event_type: type, handler) -> None: ...


class AbstractGreeter(ABC):
    """Entry point for issuing greetings via the subsystem."""

    @abstractmethod
    def greet(self, subject: str = "") -> None: ...
```

- [ ] **Step 3: Create `pieces/05-enterprise-hello/greeter/strategies.py`**

```python
"""Concrete greeting strategies."""
from __future__ import annotations


class CasualGreetingStrategy:
    """Produces understated greetings suitable for most contexts."""

    def build_greeting(self, subject: str) -> str:
        # Enterprise-grade empty-subject handling.
        if not subject:
            return "hello"
        return f"hello, {subject}"


class FormalGreetingStrategy:
    """Produces formal greetings for official correspondence."""

    def build_greeting(self, subject: str) -> str:
        if not subject:
            return "Good day."
        return f"Good day, {subject}."
```

- [ ] **Step 4: Create `pieces/05-enterprise-hello/greeter/events.py`**

```python
"""Event bus and greeting event definitions."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class GreetingEvent:
    """Emitted when a greeting has been successfully delivered."""

    subject: str
    rendered_message: str


class EventBus:
    """A simple synchronous in-process publisher/subscriber."""

    def __init__(self) -> None:
        self._subscribers: dict[type, list[Callable[[object], None]]] = defaultdict(list)

    def publish(self, event: object) -> None:
        for handler in self._subscribers.get(type(event), []):
            handler(event)

    def subscribe(self, event_type: type, handler: Callable[[object], None]) -> None:
        self._subscribers[event_type].append(handler)
```

- [ ] **Step 5: Create `pieces/05-enterprise-hello/greeter/container.py`**

```python
"""A lightweight dependency-injection container.

Supports:
    - singleton registration by type
    - factory registration by type
    - resolution by type with automatic constructor wiring
"""
from __future__ import annotations

import inspect
from typing import Any, Callable


class DependencyInjectionContainer:
    def __init__(self) -> None:
        self._singletons: dict[type, Any] = {}
        self._factories: dict[type, Callable[[], Any]] = {}

    def register_singleton(self, interface: type, instance: Any) -> None:
        self._singletons[interface] = instance

    def register_factory(self, interface: type, factory: Callable[[], Any]) -> None:
        self._factories[interface] = factory

    def register_class(self, interface: type, implementation: type) -> None:
        """Resolve a concrete class with auto-wired constructor args."""
        self._factories[interface] = lambda: self._build(implementation)

    def resolve(self, interface: type) -> Any:
        if interface in self._singletons:
            return self._singletons[interface]
        if interface in self._factories:
            return self._factories[interface]()
        raise KeyError(f"No registration for {interface!r}")

    def _build(self, cls: type) -> Any:
        sig = inspect.signature(cls.__init__)
        kwargs: dict[str, Any] = {}
        for name, param in sig.parameters.items():
            if name == "self" or param.annotation is inspect.Parameter.empty:
                continue
            kwargs[name] = self.resolve(param.annotation)
        return cls(**kwargs)
```

- [ ] **Step 6: Create `pieces/05-enterprise-hello/greeter/greeter.py`**

```python
"""The concrete greeter, wiring strategy + event bus behind AbstractGreeter."""
from __future__ import annotations

from .abstract import AbstractEventBus, AbstractGreeter, AbstractGreetingStrategy
from .events import GreetingEvent


class ConcreteGreeter(AbstractGreeter):
    def __init__(
        self,
        strategy: AbstractGreetingStrategy,
        event_bus: AbstractEventBus,
    ) -> None:
        self._strategy = strategy
        self._event_bus = event_bus

    def greet(self, subject: str = "") -> None:
        message = self._strategy.build_greeting(subject)
        print(message)
        self._event_bus.publish(
            GreetingEvent(subject=subject, rendered_message=message)
        )
```

- [ ] **Step 7: Create `pieces/05-enterprise-hello/main.py`**

```python
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
```

- [ ] **Step 8: Create `pieces/05-enterprise-hello/architecture.md`**

```markdown
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
```

- [ ] **Step 9: Create `pieces/05-enterprise-hello/README.md`**

```markdown
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
```

- [ ] **Step 10: Run it**

```bash
cd pieces/05-enterprise-hello
python main.py
```

Expected output (exactly one line):
```
hello
```

- [ ] **Step 11: Commit**

```bash
cd ../..
git add pieces/05-enterprise-hello/
git commit -m "feat(05): enterprise-hello"
```

---

## Task 8: Piece 06 — `quine-and-vanish`

**Files:**
- Create: `pieces/06-quine-and-vanish/README.md`
- Create: `pieces/06-quine-and-vanish/main.py`

**Design:** A pseudo-quine that reads its own source via `__file__`, prints it, then uses `sandbox.fake_fs.ShadowFile` to really delete a shadow copy of itself. The real `main.py` is untouched — but the deletion is a real `os.remove` on a real file. The piece uses the repo's installed `sandbox` package (requires `pip install -e .` from Task 1).

Note: this is explicitly *not* a classical quine (one that reproduces its own source via string manipulation). Reading `__file__` is cheating at quine but faithful to the aesthetic — the piece is about the vanishing, not the mirror.

- [ ] **Step 1: Write `pieces/06-quine-and-vanish/main.py`**

```python
"""A file that shows its face and then leaves."""
import sys

from sandbox.fake_fs import ShadowFile


def main() -> None:
    me = ShadowFile(__file__)
    print(me.read_text())
    me.delete()
    assert not me.exists(), "the shadow lingers"
    print(f"(the file at {me.path} has been removed)", file=sys.stderr)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Write `pieces/06-quine-and-vanish/README.md`**

```markdown
# 06 — quine-and-vanish

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

## Prerequisites

From the repo root: `pip install -e .` so `import sandbox` resolves.

## Run

```bash
python main.py
```

(Run it as many times as you like. The piece is safe.)

## What you'll see

The source of this file, printed to stdout. Then, on stderr, a single line 
naming the path of the shadow file that was just deleted.
```

- [ ] **Step 3: Run and verify**

```bash
cd pieces/06-quine-and-vanish
python main.py
```

Expected: stdout contains the contents of `main.py`; stderr contains one line starting with `(the file at ` and ending with ` has been removed)`. No traceback. Re-running the file works identically (the original `main.py` is untouched).

Verify the original was not deleted:

```bash
ls main.py  # should still exist
```

- [ ] **Step 4: Commit**

```bash
cd ../..
git add pieces/06-quine-and-vanish/
git commit -m "feat(06): quine-and-vanish (uses sandbox.fake_fs)"
```

---

## Task 9: Piece 07 — `pypi-useless`

**Files:**
- Create: `pieces/07-pypi-useless/README.md`
- Create: `pieces/07-pypi-useless/pyproject.toml`
- Create: `pieces/07-pypi-useless/src/useless/__init__.py`

**Design:** The inner directory is a real, buildable PyPI-ready package whose sole export is a module docstring. `pip install useless` (were we to publish) succeeds; `import useless` succeeds; nothing observable happens. The *actual* upload to PyPI is a one-time manual action outside this plan — we only produce a package that *could* be uploaded.

- [ ] **Step 1: Create `pieces/07-pypi-useless/src/useless/__init__.py`**

```python
"""The most dependable package on PyPI.

It has a 100% uptime SLA because it has no functions to fail at.
It has zero known bugs because it has zero known behaviors.
It has no dependencies, no API surface, no deprecation policy, and
no roadmap. It is feature-complete.
"""
```

- [ ] **Step 2: Create `pieces/07-pypi-useless/pyproject.toml`**

```toml
[project]
name = "useless"
version = "0.1.0"
description = "The most dependable package on PyPI."
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }
authors = [{ name = "sisyphus167" }]
keywords = ["useless", "nothing", "concept-art"]
classifiers = [
    "Development Status :: 6 - Mature",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Topic :: Artistic Software",
]

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

- [ ] **Step 3: Create `pieces/07-pypi-useless/README.md`**

```markdown
# 07 — pypi-useless

> `pip install useless`
> `import useless`
> *(nothing happens)*

This directory is a buildable PyPI package. Its public API is a module 
docstring. Everything that is not a docstring has been extensively 
removed.

It is the collection's closing piece because it's the only one that 
leaves the repository. The file above your terminal prompt is useless; 
the package at `pip install useless` is useless at a distance. It is 
useless in your site-packages, useless in your `requirements.txt`, 
useless in production.

Nothing that is wrong with your software is its fault.

## Build

From this directory:

```bash
python -m build
```

This produces `dist/useless-0.1.0.tar.gz` and `dist/useless-0.1.0-py3-none-any.whl`.

## Publish (out of scope for the repo)

`twine upload dist/*` — a one-time action not part of normal repo 
operation. If the package has been uploaded, a link here would eventually 
point at it.

## What you'll see

After `pip install useless && python -c "import useless"`: nothing, and 
correctly.
```

- [ ] **Step 4: Verify the inner package builds**

```bash
cd pieces/07-pypi-useless
python -m build
ls dist/
```

(The `build` package was installed via the root `.[dev]` extra in Task 1.)

Expected: `dist/useless-0.1.0.tar.gz` and `dist/useless-0.1.0-py3-none-any.whl` exist, both non-empty.

- [ ] **Step 5: Verify the package installs and imports silently**

```bash
pip install --force-reinstall dist/useless-0.1.0-py3-none-any.whl
python -c "import useless; print('ok' if useless.__doc__ else 'no docstring')"
pip uninstall -y useless
```

Expected: `import useless` succeeds, prints `ok`. Uninstall succeeds.

- [ ] **Step 6: Clean up build artifacts and commit**

```bash
rm -rf dist/ build/ src/useless.egg-info/
cd ../..
git add pieces/07-pypi-useless/
git commit -m "feat(07): pypi-useless (buildable inner package)"
```

Note: `dist/`, `build/`, and `*.egg-info/` are already in `.gitignore` from Task 1, so they wouldn't get committed anyway — the explicit `rm -rf` is tidiness, not safety.

---

## Task 10: Root `README.md` + `CONTRIBUTING.md`

**Files:**
- Create: `README.md` (repo root)
- Create: `CONTRIBUTING.md` (repo root)

- [ ] **Step 1: Create `README.md`**

```markdown
# useless-machine

*A collection of Python code in the spirit of Claude Shannon's Ultimate 
Machine — pieces whose sole purpose is to undo themselves, spin in place, 
over-engineer nothing, or refer only to themselves.*

In 1952, Shannon built a box with a switch on it. Flip the switch; a 
small hand emerges from the box, flips the switch back, and retracts. 
This repository collects the software version of that impulse.

Each piece is a small work of concept art: some Python code, a short 
manifesto. Run it, look at it, move on.

## Index

| # | Piece | Faction | One-line |
|---|---|---|---|
| 01 | [shannon-switch](pieces/01-shannon-switch/) | Shannon | A class whose `__new__` turns the switch on and off in the same breath. |
| 02 | [hello-antiworld](pieces/02-hello-antiworld/) | Shannon | "Hello, World!" — printed, then erased. |
| 03 | [sisyphus-sort](pieces/03-sisyphus-sort/) | Sisyphus | Bar chart sorted, shuffled, sorted, shuffled. Forever. |
| 04 | [99-percent](pieces/04-99-percent/) | Sisyphus | A progress bar that never reaches 100%. |
| 05 | [enterprise-hello](pieces/05-enterprise-hello/) | Over-engineering | 200 lines of SOLID Python produce exactly `hello`. |
| 06 | [quine-and-vanish](pieces/06-quine-and-vanish/) | Self-reference | A file reads itself out loud and then leaves. |
| 07 | [pypi-useless](pieces/07-pypi-useless/) | Philosophical | A buildable PyPI package whose API is a docstring. |

## Running a piece

```bash
pip install -e ".[dev]"           # once, from the repo root
cd pieces/01-shannon-switch
python main.py
```

Piece 03 is a Jupyter notebook: `jupyter lab pieces/03-sisyphus-sort/sisyphus_sort.ipynb`.

## Safety

Pieces that would produce destructive side effects (self-deletion, 
pushing to remotes, sending mail) use the `sandbox/` library, which 
provides real-but-harmless shadow objects — real files in temp 
directories, real local-bare-repo pushes, real localhost SMTP. No 
actual files, remotes, or mailboxes are touched.

Currently, only piece 06 uses `sandbox/`.

## License / purpose

Not for utility. For looking at.
```

- [ ] **Step 2: Create `CONTRIBUTING.md`**

```markdown
# A letter to future me

*This file is written for the one person who is likely to add another 
piece to this repo — me, later.*

## A good useless piece has

1. **A clear thesis.** You can say in one sentence what the piece *is*. 
   "A class whose constructor turns it off" is a thesis. "Some over-engineered 
   code" is not.
2. **Faithfulness to the thesis.** No extra features, no escape hatches. 
   If the thesis is "it always fails", it always fails. Don't add a 
   `--succeed` flag.
3. **Autonomy.** It doesn't import from other pieces. `sandbox/` is the 
   only permitted shared code.
4. **Self-reliance.** The README explains the piece to a reader who has 
   not been told anything else.

## A bad useless piece

- **Tries to be useful secretly.** A progress bar that's secretly 
  informative is a real progress bar in a costume. Delete it.
- **Explains its own joke.** No `# lol because it's like Shannon's thing` 
  comments. Let the piece be what it is.
- **Uses mocks or dry-run flags to fake destructiveness.** Use `sandbox/`. 
  The piece should read as if it is really doing the thing.
- **Faction-hops.** Pick one; the piece gets the clarity of its faction 
  in return.

## House rules

- **Number by arrival order.** Never renumber. 03 is the third piece you 
  made, and it stays 03, even if later you think it's weak.
- **Pick one language per piece.** Whichever (中/en) makes the manifesto 
  land. Don't translate — the piece loses voice.
- **Commit each piece on its own.** One piece per commit. The history 
  is the exhibition catalog.
- **If a piece needs >1 file, split by what a reader wants to read 
  separately.** Not by technical layer.

## The two temptations

1. **"This is a really clever trick, I should add it."** If it's useful, 
   it probably doesn't belong. Clever ≠ useless.
2. **"This piece is weak, let me delete it."** No. A mixed-quality 
   portfolio is honest. A curated-to-perfection one is a product pitch. 
   Leave it. Write a better one next to it.

## When to expand `sandbox/`

Only when a new piece genuinely needs it. The spec lists `fake_git` and 
`fake_net` as placeholders — add them when the piece that requires them 
is actually being written. Not before.

## External contributions

Not currently accepted. This is a closed exhibition. If someone opens a 
PR: thank them kindly and close it. Nothing personal — the coherence of 
the portfolio depends on one hand.
```

- [ ] **Step 3: Verify the README renders on GitHub preview**

If pushed to a remote, check that the table renders. No command-line verification required — markdown is markdown.

- [ ] **Step 4: Commit**

```bash
git add README.md CONTRIBUTING.md
git commit -m "docs: root README with piece index and CONTRIBUTING letter"
```

---

## Deferred items (explicitly out of scope for this plan)

The spec calls for three artifacts that can't reasonably be authored by code-authoring tasks; they require running the finished pieces with a human-controlled recorder/editor. The plan produces the code that makes them possible, but leaves the artifact itself for manual follow-up:

- **`pieces/02-hello-antiworld/demo.gif`** — record `python main.py` in a real terminal with asciinema + asciicast2gif (or similar). Spec flags this as required.
- **`pieces/04-99-percent/demo.gif`** — record ~15 seconds showing the climb to 99% and the linger/shiver. Spec flags this as required.
- **`pieces/05-enterprise-hello/architecture.svg`** — the spec calls for SVG; this plan delivers an ASCII diagram in `architecture.md` as the source material. Rendering to SVG (e.g., via a diagram tool like Mermaid / draw.io / graphviz) is a follow-up pass.
- **PyPI publication of piece 07** — the package builds; uploading is a one-time manual `twine upload` outside normal repo operation. Spec already marks this out of scope.

None of these block the first public-ready state of the repo; all pieces run correctly without them, and the READMEs name the gaps.

## Post-implementation sanity check

After Task 10, from the repo root, these should all succeed cleanly:

```bash
pytest tests/ -v                                            # sandbox tests pass
python pieces/01-shannon-switch/main.py                     # prints "switch: ON\nswitch: OFF"
python pieces/02-hello-antiworld/main.py                    # (brief flash, line ends clean)
timeout 8 python pieces/04-99-percent/main.py || true       # climbs to 99% and lingers
python pieces/05-enterprise-hello/main.py                   # prints "hello"
python pieces/06-quine-and-vanish/main.py                   # prints source + stderr note
(cd pieces/07-pypi-useless && python -m build)              # inner package builds
```

The notebook (piece 03) can be verified by opening `pieces/03-sisyphus-sort/sisyphus_sort.ipynb` in Jupyter and running all cells; the animation should render inline. Alternatively, from repo root:

```bash
jupyter nbconvert --to notebook --execute pieces/03-sisyphus-sort/sisyphus_sort.ipynb --output /tmp/sisyphus-check.ipynb
```

which executes the notebook without UI and errors if any cell fails.

No additional commit needed — this is just a smoke test.
