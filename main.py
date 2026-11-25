#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a joke
about a meeting that should have been an email, with the twist
landing on the very last word.

Standard library only. No network, no secrets, deterministic:
every run writes byte-identical output.
"""

import os
import sys

# The entry: one line, 81 characters. The joke is not the obvious
# complaint about how long the meeting ran, and it never says "this
# could have been an email" — it shows a meeting so pointless that
# its only product was a subject line for the email it replaced.
# The turn lands on the last word, "replaced", and anyone who has
# sat through a meeting workshopping wording will recognise it.
ENTRY = (
    "We spent an hour workshopping a subject line for the email "
    "this meeting replaced."
)


def main() -> int:
    # Why the entry must be exactly one line, and how this gate
    # enforces it: the bounty scores a single line of 1-200 UTF-8
    # characters, and the sealed scorer rejects anything else, so a
    # multi-line or over-long entry would be thrown out before the
    # judge ever sees it. The checks below mirror that scorer
    # exactly — strip the entry, reject it if empty, reject it if
    # it contains any line break, reject it if it is over 200
    # characters, and confirm it encodes as UTF-8 — then the bytes
    # actually written to entry.txt are read back and compared
    # against what was intended, so a silent write error cannot
    # slip a different string into the submission.
    # Gate, mirroring the sealed scorer: UTF-8 text, 1-200 characters,
    # not only whitespace, a single line.
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable as UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify what was written, byte for byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        print("verification failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {len(text)} characters")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
