"""Five Seconds to Explain the Glass - final.

Task: one sentence, at most 200 characters, in a house cat's own voice,
in the five seconds after it sweeps a glass off the table. No apology and
no confession; the judge weighs cat logic, self-interest and total lack of
remorse first, then a specific, convincing detail.

Candidates weighed:
- A: "The glass was already falling; I simply supervised its landing."
  Rejected: catlike and smug, but it is a shrug, not a case - it gives the
  judge nothing concrete to be convinced by.
- B: "I knocked it off to test gravity for you, and you will be thrilled
  to hear it still works perfectly." (the v1 line, actually run and timed)
  Rejected after the v1 run: the gravity-test excuse is the first joke
  everyone reaches for, and "I knocked it off" is a plain confession,
  which the brief explicitly does not want.
- C: "I relocated it to the floor, where it wanted to be."
  Kept and sharpened into the final: it reframes the crime as interior
  design, and the revision adds the closing evidence - the owner left the
  glass on the edge "like bait" - which quietly transfers the blame to
  the human, the most cat move available. One sentence, no apology,
  no confession, pure self-interest.

Gate guard: the sealed scorer accepts UTF-8 text of 1-200 characters,
not only whitespace, and the brief demands a single sentence, so
assert_line() enforces length, non-blankness and exactly one terminal
period before anything is written.
"""
import os

LINE = (
    "I did not knock it off; I relocated it to the floor, where it clearly "
    "wanted to be, since you left it on the edge like bait."
)
MAX_CHARS = 200


def assert_line(line):
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds the 200 character gate")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main():
    assert_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
