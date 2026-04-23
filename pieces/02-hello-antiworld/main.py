"""Hello, World! — and then nothing."""
import sys
import time

MESSAGE = "Hello, World!"
LINGER_SECONDS = 0.3


def main() -> None:
    sys.stdout.write(MESSAGE)
    sys.stdout.flush()
    time.sleep(LINGER_SECONDS)
    sys.stdout.write("\r" + " " * len(MESSAGE) + "\r")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
