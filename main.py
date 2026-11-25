"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Deterministic: the same line on every run. No input, no network, no
environment reads -- the line is a constant in this file.

The joke: a standing desk bought for health ends up doing the opposite
of its job -- holding the chair. The turn is the punchline.
Line length: 65 characters (66 with the trailing newline).
"""

import os

LINE = "I bought a standing desk to get healthier. It now holds my chair."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
