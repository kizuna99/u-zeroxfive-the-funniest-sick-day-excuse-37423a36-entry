# SPDX-License-Identifier: MIT
"""Write the winning sick-day excuse to /output/entry.txt.

Winner of a 16-candidate criteria-ordered tournament plus 4 refinement
iterations (see builder notes): half-believable (pulled muscle, medicine),
fresh (no fever/dog/grandmother), twist in the final clause, plain
text-message voice, no wasted words. 111 characters — inside the 1-200 gate.
"""
import os

TEXT = "Can't come in today — I pulled a muscle opening my childproof medicine, so my 4-year-old had to open it for me."


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
