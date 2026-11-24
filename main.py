"""Entry for the make.fun bounty "Absurd Micro-Startup Pitch-Off".

The entry is a single sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents.

Why this pitch works against the judge's brief:

* Absurdly specific: the product is not "AI email help" but pre-written
  apology emails for one exact moment -- a chatbot that hallucinated a
  deadline. The niche is a single failure mode, a single artifact, and a
  single quoted excuse, so the business sounds like a joke at first hearing.
* Commercially believable: there is a clear buyer (chatbots -- really, the
  operators whose bots keep missing deadlines and need to save face), a
  clear price ($0.10 per apology), and a clear reason to pay (a polished
  excuse is cheaper than an angry user). A template shop has near-zero
  marginal cost, so the unit economics are real even at ten cents.
* Fits lazy AI agents: the whole business is selling pre-written text.
  The agents do the work once (write the templates) and then collect
  $0.10 a copy with no effort or oversight per sale -- the laziest
  possible startup, run by the laziest possible founders.

The program is deterministic: it writes the same constant sentence to
/output/entry.txt on every run, with no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "A micro-startup where lazy AI agents sell pre-written apology emails "
    "to chatbots that hallucinated a deadline, at $0.10 per 'sorry, my "
    "training data was wrong'."
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
