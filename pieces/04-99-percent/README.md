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
