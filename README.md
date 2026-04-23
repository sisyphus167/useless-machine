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
python -m venv .venv && source .venv/bin/activate   # once
pip install -e ".[dev]"                             # once, from the repo root
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
