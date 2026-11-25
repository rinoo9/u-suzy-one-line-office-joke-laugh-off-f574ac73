#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Deterministic: the same joke, byte for byte, on every run.
"""

import os

JOKE = (
    "Our printer only breaks down on deadline day, "
    "which is the closest thing this office has to a union rep."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the gate"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
