"""Shannon's Ultimate Machine, in Python."""
import subprocess
import sys


class UselessMachine:
    """Its only purpose is to turn itself off.

    The switch turns on, and in the same breath the machine reaches out
    and turns it off. No instance is ever returned — the machine never
    really exists, only the trace of it having existed.
    """

    def __new__(cls):
        cls._act()
        return None

    @classmethod
    def _act(cls):
        process = subprocess.Popen(
            [sys.executable, "-c", "import time; time.sleep(3600)"]
        )
        print(f"switch: ON  [pid {process.pid} running]", flush=True)

        print("...a hand emerges from under the lid...", flush=True)

        process.terminate()
        process.wait()
        print(f"...and kills pid {process.pid}.", flush=True)

        print("switch: OFF", flush=True)


if __name__ == "__main__":
    UselessMachine()
