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

See the root README for setup (`python -m venv .venv && pip install -e ".[dev]"`) — you need `sandbox` on the import path.

## Run

```bash
python main.py
```

(Run it as many times as you like. The piece is safe.)

## What you'll see

The source of this file, printed to stdout. Then, on stderr, a single line 
naming the path of the shadow file that was just deleted.
