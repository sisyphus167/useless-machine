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
