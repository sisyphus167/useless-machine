# 07 — pypi-useless

## 中文

> `pip install useless`
> `import useless`
> *（什么都不发生）*

这个目录是一个可构建的 PyPI 包。它的公共 API 是一个模块 docstring。所有不是 docstring 的东西都被彻底删除了。

它是整个合集的收尾之作，因为它是唯一一件会离开仓库的作品。你终端提示符上方的文件是无用的；经由 `pip install useless` 进来的包，则是在远处无用。它在你的 site-packages 里无用，在你的 `requirements.txt` 里无用，在生产环境里也无用。

你软件里任何出错的地方，都不是它的错。

### 构建

在本目录下：

```bash
python -m build
```

这会产生 `dist/useless-0.1.0.tar.gz` 和 `dist/useless-0.1.0-py3-none-any.whl`。

### 发布（不属于本仓库的日常范围）

`twine upload dist/*` —— 一次性动作，不属于仓库的正常操作。如果这个包已经被上传，这里之后会有一个指向它的链接。

### 你会看到

`pip install useless && python -c "import useless"` 之后：什么都没有，而且是正确地什么都没有。

---

## English

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

### Build

From this directory:

```bash
python -m build
```

This produces `dist/useless-0.1.0.tar.gz` and `dist/useless-0.1.0-py3-none-any.whl`.

### Publish (out of scope for the repo)

`twine upload dist/*` — a one-time action not part of normal repo 
operation. If the package has been uploaded, a link here would eventually 
point at it.

### What you'll see

After `pip install useless && python -c "import useless"`: nothing, and 
correctly.
