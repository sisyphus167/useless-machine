"""Shannon's Ultimate Machine, in Python."""


class UselessMachine:
    """Its only purpose is to turn itself off.

    The switch turns on, and in the same breath the machine reaches out
    and turns it off. No instance is ever returned — the machine never
    really exists, only the trace of it having existed.
    """

    def __new__(cls):
        print("switch: ON",  flush=True)
        print("switch: OFF", flush=True)
        return None


if __name__ == "__main__":
    UselessMachine()
