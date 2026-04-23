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
        self._path.parent.rmdir()
