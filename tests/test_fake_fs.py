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
