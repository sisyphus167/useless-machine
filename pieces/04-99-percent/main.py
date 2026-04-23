"""A progress bar that never reaches 100%."""
import random
import sys
import time

WIDTH = 40
ETA_TEXT = "about 3 seconds remaining"


def render(pct: float, suffix: str = "") -> None:
    filled = int(pct * WIDTH / 100)
    bar = "█" * filled + "·" * (WIDTH - filled)
    line = f"\r[{bar}] {pct:5.1f}%  {suffix}"
    # Pad with spaces to overwrite any previous longer suffix
    sys.stdout.write(line.ljust(WIDTH + 40))
    sys.stdout.flush()


def climb_to_99() -> None:
    pct = 0.0
    while pct < 99.0:
        pct = min(99.0, pct + random.uniform(0.5, 2.0))
        render(pct)
        time.sleep(random.uniform(0.02, 0.08))


def linger_at_99() -> None:
    while True:
        jitter = random.choice([0.0, 0.0, 0.0, 0.1, 0.2])
        render(99.0 - jitter, suffix=ETA_TEXT)
        time.sleep(random.uniform(0.8, 1.5))


def main() -> None:
    try:
        climb_to_99()
        linger_at_99()
    except KeyboardInterrupt:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
