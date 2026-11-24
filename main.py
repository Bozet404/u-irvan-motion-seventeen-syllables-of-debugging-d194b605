"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, under 200 characters)
to /output/entry.txt.
"""

import os

HAIKU = (
    "One red breakpoint blinks\n"
    "the log line scrolls past midnight\n"
    "dawn finds the typo\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(HAIKU)


if __name__ == "__main__":
    main()
