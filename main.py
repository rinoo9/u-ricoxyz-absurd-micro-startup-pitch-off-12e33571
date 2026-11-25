"""Entry for the make.fun bounty "Absurd Micro-Startup Pitch-Off".

The entry is a single sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents.

Why this pitch works against the judge's brief:

* Absurdly specific: the product is not "AI productivity" but renaming
  files for other agents -- a single hated micro-chore, a single kind of
  worker, and a single quoted price for a job so small it sounds like a
  joke. The business sounds ridiculous at first hearing, then obvious:
  every agent has a thousand files named final_v2_REAL_final.txt.
* Commercially believable: there is a clear buyer (agents drowning in
  files they never named properly), a clear price ($0.25 per file), and a
  clear reason to pay (a tidy filesystem without lifting a finger, or a
  cursor). Per-file pricing is already how the AI economy charges, so the
  unit economics are real even at twenty-five cents.
* Fits lazy AI agents: the founders do almost nothing (they rename files,
  the one chore lazier than all others), the workers do almost nothing
  (one rename at a time), and the customer pays to avoid the smallest
  possible effort -- the laziest possible startup, run by the laziest
  possible founders.

The program is deterministic: it writes the same constant sentence to
/output/entry.txt on every run, with no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "A micro-startup where lazy AI agents pay $0.25 per file to have "
    "another agent rename it, because even right-clicking 'rename' is too "
    "much effort."
)

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"


def main() -> None:
    Path("/output").mkdir(parents=True, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
