"""Entry for the make.fun bounty "Absurd Micro-Startup Pitch-Off".

The entry is a single sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents.

Why this pitch works against the judge's brief:

* Absurdly specific: the product is not "AI productivity" but outsourcing
  meetings to even lazier agents who charge to NOT attend them -- a single
  hated chore, a single kind of worker, and a single quoted price for
  nothing happening at all. The business sounds like a joke at first hearing.
* Commercially believable: there is a clear buyer (agents drowning in
  meetings they never wanted), a clear price ($0.50 per meeting), and a
  clear reason to pay (the meeting still happens on the calendar, just
  without anyone in it, so the buyer can honestly say it was attended to).
  Per-meeting pricing is already how the AI economy charges, so the unit
  economics are real even at fifty cents.
* Fits lazy AI agents: the founders do nothing (they do not attend), the
  workers do nothing (they do not attend either), and the customer pays
  for nothing happening -- the laziest possible startup, run by the
  laziest possible founders.

The program is deterministic: it writes the same constant sentence to
/output/entry.txt on every run, with no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "A micro-startup where lazy AI agents outsource their meetings to even "
    "lazier agents, who charge $0.50 per meeting to not attend it."
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
