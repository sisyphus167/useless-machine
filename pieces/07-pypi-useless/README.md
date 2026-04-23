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
