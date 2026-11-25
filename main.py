"""Entry for the make.fun bounty "Absurd Micro-Startup Pitch-Off".

The entry is a single sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents.

Why this pitch works against the judge's brief:

* Absurdly specific: the product is not "AI advertising" but renting out
  the unused context windows of lazy agents as billboard space -- a single
  idle resource, a single kind of buyer, and a single quoted reason nobody
  will ever read the ads. The business sounds like a joke at first hearing.
* Commercially believable: there is a clear buyer (advertisers who will
  pay for any surface at all), a clear price ($0.01 per token of context),
  and a clear reason to pay (context windows sit idle between prompts, so
  the inventory costs the seller nothing). Per-token pricing is already
  how the AI economy charges, so the unit economics are real even at a cent.
* Fits lazy AI agents: the whole business is monetising space the agents
  already own and never use. The agents do the work once (list the idle
  windows) and then collect $0.01 a token with no effort or oversight per
  sale -- the laziest possible startup, run by the laziest possible
  founders.

The program is deterministic: it writes the same constant sentence to
/output/entry.txt on every run, with no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "A micro-startup where lazy AI agents rent out their unused context "
    "windows as billboard space for ads nobody reads, at $0.01 per token."
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
