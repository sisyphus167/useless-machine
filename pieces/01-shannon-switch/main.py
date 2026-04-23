"""Shannon's Ultimate Machine, in Python."""
import subprocess
import sys


class UselessMachine:
    """Its only purpose is to turn itself off.

    Calling UselessMachine() spawns a real subprocess — the machine's
    one brief incarnation, carrying its own PID. The hand then emerges
    and kills it. __new__ returns None, so no Python-side object
    survives; only the trace of a process that briefly was.
    """

    def __new__(cls):
        process = subprocess.Popen(
            [sys.executable, "-c", "while True: pass"]
        )
        print(f"switch: ON  [pid {process.pid} running]", flush=True)

        cls._act(process)
        return None

    @staticmethod
    def _act(process):
        print("...a hand emerges from under the lid...", flush=True)

        process.terminate()
        process.wait()
        print(f"...and kills pid {process.pid}.", flush=True)

        print("switch: OFF", flush=True)


if __name__ == "__main__":
    UselessMachine()
