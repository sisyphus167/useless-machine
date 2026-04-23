"""Shannon's Ultimate Machine, in Python."""
import time


class UselessMachine:
    """Its only purpose is to turn itself off.

    The switch turns on, and in the same breath the machine reaches out
    and turns it off. No instance is ever returned — the machine never
    really exists, only the trace of it having existed.
    """

    def __new__(cls):
        cls._wake()
        cls._act()
        cls._rest()
        return None

    @classmethod
    def _wake(cls):
        print("switch: ON", flush=True)
        time.sleep(0.4)

    @classmethod
    def _act(cls):
        print("...a hand emerges from under the lid...", flush=True)
        time.sleep(0.8)

    @classmethod
    def _rest(cls):
        print("switch: OFF", flush=True)


if __name__ == "__main__":
    UselessMachine()
