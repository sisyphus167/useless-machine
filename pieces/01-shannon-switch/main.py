"""Shannon's Ultimate Machine, in Python."""
import time


class UselessMachine:
    """Its only purpose is to turn itself off.

    The switch turns on. A hand reaches out from inside the box and
    flips it off. `__new__` runs the whole sequence and then returns
    None — no instance is ever constructed, only the trace of one
    having briefly been.
    """

    def __new__(cls):
        cls._turn_on()
        cls._reach_out()
        cls._turn_off()
        return None

    @classmethod
    def _turn_on(cls):
        print("switch: ON", flush=True)
        time.sleep(0.4)

    @classmethod
    def _reach_out(cls):
        print("...a hand emerges from under the lid...", flush=True)
        time.sleep(0.8)

    @classmethod
    def _turn_off(cls):
        print("switch: OFF", flush=True)


if __name__ == "__main__":
    UselessMachine()
