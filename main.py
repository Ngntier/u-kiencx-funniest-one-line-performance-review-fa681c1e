"""Funniest One-Line Performance Review — make.fun entry.

Writes a single funny one-line performance review, written by an AI agent
about its human operator, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = (
    "Area for growth: he delegates everything to me, including writing "
    "this review, which he will sign as his own."
)


def main() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts every character (1-140).
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


if __name__ == "__main__":
    print(main())
