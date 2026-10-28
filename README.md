# Docs Assistant

This project builds two Claude Code skills, `release-notes` and `doc-review`, and evaluates them the way you would test production software.

**Method:** I wrote the correct answers for 20 real commits by hand before writing the skill. Each run is graded one row per case against a versioned 8-criterion rubric (`evals/rubric.md`). A script grades the 4 criteria it can, and I grade the rest. Each failure is traced to a cause, fixed in the spec, and the skill is run again.

**Start here:** [case-study.md](case-study.md) is the full write-up, with a file behind every claim. [evals/runs/README.md](evals/runs/README.md) lists every score in one line each.

## The two skills

**`release-notes`** turns raw git commit messages into user-facing release notes. The notes use the past tense, and they cover only changes a user of the product would notice. The skill also flags anything it couldn't verify. The test cases come from a real project of mine, a book-recommendation skill, so "would a user notice this?" has a real answer. It is written for that one project: its skip rule names the book-recommendation skill, so using it for another product would need a rewrite and new test cases.

**`doc-review`** checks a document against a short checklist, such as whether it states its purpose up front and uses active voice. It reports pass, fail, or unverifiable for each item and says plainly when an item doesn't apply.

Both skills share rules in `shared/house-style.md`. `shared/hard-surfaces.md` says what each should do when input is missing, unclear, or out of scope. `tools/read-commits.md` documents the input format `release-notes` expects.

## How to make a third skill
1. Make a folder named for the skill under `.claude/skills/`.
2. Write its `SKILL.md`.
3. Add test cases in `evals/cases/`.
4. Add hand-written correct answers in `evals/gold/`.
5. Add a rubric for the skill in `evals/rubric.md`.
6. Add results of running the skill to `evals/runs/`.

## Running it yourself

You need an Anthropic API key:

```
export ANTHROPIC_API_KEY="sk-..."
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic
```

Then run these from the repo root:

- `python3 scripts/run-eval.py --name run-13` runs the 20 release-notes cases once and saves each response to `evals/runs/run-13/`. The script never overwrites an existing response, so give each run a new name.
- `python3 scripts/run-eval.py --name run-13 --repeats 5` runs each case 5 times (100 calls) into `evals/runs/run-13/rep-01/` through `rep-05/`.
- `python3 scripts/check-mechanical.py` grades every saved release-notes run on the automatable criteria and writes `evals/runs/mechanical-results.csv`. It only handles release-notes, because doc-review has no rubric.
- `python3 scripts/check-pass-rate.py --minimum 0.75 --run run-13` reads that CSV, scores only the `run-13` run, and exits with an error if the pass rate is below the minimum.


A person still grades the judgment criteria, such as whether a skip was correct. Those grades go into `evals/runs/judgment-grades.csv`.


## How the repo is organized

- `.claude/skills/` holds each skill's instructions.
- `shared/` holds the rules both skills follow and the hard-input expectations.
- `tools/` describes the real input the skill receives.
- `evals/cases/` holds the test inputs.
- `evals/gold/` holds hand-written correct answers, written before the skills existed so the skills were built to match human judgment.
- `evals/rubric.md` holds the scoring criteria. It is versioned, so old runs stay graded against the rules that applied at the time.
- `evals/runs/` holds every run's output and score.
- `evals/findings.md`, `CHANGELOG.md`, and `decisions.md` record what went wrong, what changed, and why.
- `scripts/` holds the eval runner, the mechanical grader, and the pass-rate gate.
