#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes one sentence, in a house cat's own voice, to /output/entry.txt.

Methodology (see candidates.md for the full 34-candidate table and
criteria-ordered scoring): 34 candidates were drafted against the judge's
published criteria in order — (1) one sentence <=200 chars excusing the
glass, (2) cat logic / self-interest / zero remorse, (3) fresh idea (not
gravity / slippery-edge / already-falling), (4) five-second spoken fit,
(5) every character earns its place — then scored 0-5 per criterion with
written notes and compared criteria-first. Winner (25/25 manual):
"I am the building inspector here, and that glass failed inspection, so I
condemned it on the spot." (98 chars). Live-title collision check:
verified against all 50 live titles — no byte-identical match, no shared
phrase with the eviction/sunbeam/staring-glass/witness family that fills
the field. No live-judge A/B: the shared OpenRouter key is exhausted
(HTTP 402); scores are honest manual scores, no judge numbers invented.
"""

ENTRY = "I am the building inspector here, and that glass failed inspection, so I condemned it on the spot."

# Gate self-check (import time): the entry must be one sentence of 1-200
# UTF-8 characters, not only whitespace. Fail loudly instead of shipping
# an invalid entry.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip(), "entry is only whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be exactly one sentence"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: read what was written and confirm it is
    # byte-identical to ENTRY and inside the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt differs from ENTRY"
    assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 gate"


if __name__ == "__main__":
    main()
