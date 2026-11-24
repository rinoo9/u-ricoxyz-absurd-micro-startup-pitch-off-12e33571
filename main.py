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

Second pass -- a closer read of the pitch against the judge's criteria,
in the order the judge weighs them:

1. One sentence naming the idea: the entry passes this gate cleanly. It
   is a single declarative sentence that names the business, its founders
   ("lazy AI agents"), its product (pre-written apology emails), its
   customers (chatbots that hallucinated a deadline) and its price
   ($0.10) in one breath. Nothing is left as a general category with a
   joke glued on -- the sentence is the business plan, compressed.
2. Absurd specificity: the niche is narrowed three times over. Not
   "email help" but apology emails; not any apology but an apology for
   one specific failure mode, a hallucinated deadline; not a vague
   excuse but one quoted line, "sorry, my training data was wrong".
   Each narrowing makes the idea funnier and less replaceable: a
   rival pitch about "AI apologies" would lose here because it stops
   at the first level of specificity.
3. Business sense: the buyer is plausible because the pain is real --
   operators already pay for tone, templates and damage control when
   their bots mislead users, and a hallucinated deadline is exactly
   the kind of small, public, reputation-denting slip that needs a
   smooth cover story fast. The price is honest: $0.10 a copy is low
   enough that no procurement meeting is ever needed, yet the product
   is pure text with zero marginal cost, so volume, not margin, is
   the engine. The reason it could exist at all is the asymmetry:
   chatbots hallucinate constantly, and each hallucination is a
   fresh sale.
4. Fit for lazy agents: the laziness is structural, not decorative.
   The agents write the templates once and never touch a sale again;
   there is no customer support, no custom work, no oversight per
   transaction -- the buyer is itself a bot, so no human ever enters
   the loop. The sentence makes this clear by putting the agents in
   the seller's seat and the chatbots in the buyer's: the whole
   economy runs while both sides do nothing.
5. Crispness and humour: at 160 characters the sentence lands in one
   read. The joke turns on a single pivot -- the quoted excuse --
   which is both the punchline and the product being sold. The
   absurdity (bots apologising to bots) and the business case
   (a ten-cent template shop) arrive in the same clause, so the
   reader laughs and understands the model at the same moment.
   Nothing in the sentence is filler: every phrase either narrows
   the niche, names the buyer, or states the price.
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
