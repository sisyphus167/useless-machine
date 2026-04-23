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
