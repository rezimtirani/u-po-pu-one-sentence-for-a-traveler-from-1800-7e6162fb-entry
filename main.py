#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800. The sentence builds only from things a
person of 1800 already knows -- a road, a post office, a library --
and holds one picture: a letter that arrives before its ink dries,
and books lying open on the reader's table.

Run:  python3 main.py
Writes: $MAKEFUN_OUTPUT_DIR/entry.txt (default: ./output/entry.txt)
"""

import os
import sys

SENTENCE = (
    "Think of one road joining every library and post office on earth, "
    "so a letter you write arrives before the ink dries and the books "
    "of a thousand libraries lie open on your table."
)


def gate_ok(text):
    """Check the competition gate: UTF-8, 1-200 characters, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 200:
        return False
    text.encode("utf-8")
    return True


# Words coined after 1800 that a traveler of that year could not know.
# The sentence must be built only from what 1800 already had.
MODERN_WORDS = {
    "internet", "computer", "website", "email", "online", "digital",
    "screen", "phone", "telegraph", "radio", "television", "software",
    "download", "upload", "browser", "server", "network", "wifi",
    "smartphone", "app", "data", "cloud", "pixel", "video",
}


def check_vocabulary(text):
    """Fail if the sentence uses any word coined after the year 1800."""
    words = set(
        piece.strip(".,;:!?\"'").lower() for piece in text.split()
    )
    intruders = sorted(words & MODERN_WORDS)
    if intruders:
        raise SystemExit("modern words in sentence: %s" % ", ".join(intruders))
    return True


def verify_written(path, expected):
    """Re-read the written file and confirm it matches byte for byte."""
    with open(path, "rb") as handle:
        data = handle.read()
    if data.decode("utf-8") != expected:
        raise SystemExit("verify failed: file differs from the sentence")
    print("Verified %s: %d bytes, %d characters" % (path, len(data), len(expected)))


def main():
    if not gate_ok(SENTENCE):
        raise SystemExit("gate failed: sentence is not 1-200 characters")
    check_vocabulary(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    verify_written(target, SENTENCE)
    print("Wrote entry.txt (%d characters)" % len(SENTENCE))


if __name__ == "__main__":
    main()
