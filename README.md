# Docs Assistant

This project is two Claude Code skills — `release-notes` and `doc-review` — built and evaluated the same way real production skills should be: write a first version, test it against real cases, diagnose exactly why it fails, fix it, and keep testing until the failures stop and stay stopped.

**Start here:** [`case-study.md`](case-study.md) is the full write-up — every number this project produced, why it is what it is, and a specific file backing up each claim. [`evals/runs/README.md`](evals/runs/README.md) is a quick one-line-per-run scoreboard if you just want the numbers without the narrative.

## What's here

**`release-notes`** takes a batch of raw git commit messages and turns them into user-facing release notes: past tense, only the commits a user of the thing being changed would actually notice, and honest about anything it couldn't verify. Its test cases are modeled on a real feature — the book-recommendation feature on [nellcgram.github.io](../nellcgram.github.io) — so "would a user notice this" is a real question with a real answer, not a hypothetical. It went through ten rounds of testing and fixing before it held up consistently — that whole process, including the fresh mistakes it caught along the way, is in `CHANGELOG.md` and `decisions.md`.

**`doc-review`** checks a document against a short checklist (states its purpose up front, active voice, consistent formatting, and so on) and reports pass, fail, or not applicable per item. It was grounded the same way as the first skill: by hand-reviewing three real documents from this repo before writing a single rule. It doesn't have scripted grading yet — everything for this skill is still graded by hand.

Both skills are meant to be evaluated with the same kind of harness: hand-picked test cases, a rubric with plain pass/fail/unverifiable criteria, and a script that automates the parts of grading that can be automated (tense, formatting, whether it asked for clarification instead of deciding) while leaving judgment calls (is this skip decision actually correct, is this note specific enough) to a human. Right now that's only fully built out for release-notes. `tools/` (descriptions of tools a skill can use) exists but is still empty, and a shared rules file for both skills was planned but never actually written.

## Running it yourself

You'll need an Anthropic API key:

```
export ANTHROPIC_API_KEY="sk-..."
pip install anthropic --break-system-packages
```

Then, from the repo root (both scripts are currently hardcoded to the release-notes skill, its 20-case file, and `evals/runs/v3/` — not yet general-purpose):

- `python3 scripts/run-eval.py` runs all 20 release-notes test cases once and saves each response to `evals/runs/v3/`.
- `python3 scripts/run-eval.py --repeats 5` runs them 5 times each (100 calls total) to check consistency, saving into `evals/runs/v3/rep-01/` through `rep-05/`.
- `python3 scripts/check-mechanical.py` grades every saved run against the automatable rubric criteria and writes `evals/runs/mechanical-results.csv`, one row per case per run.

Judgment criteria (does this note say what actually happened, was this the right commit to skip) still need a human reading the output next to the actual commit — that grading goes into `evals/runs/judgment-grades.csv` by hand.

## How it's organized

- `.claude/skills/release-notes/` and `.claude/skills/doc-review/` hold each skill's actual instructions.
- `evals/cases/` has the test inputs — commit descriptions for release-notes, real documents for doc-review.
- `evals/gold/` has hand-written "what a correct answer looks like" for a few cases, written before either skill existed, so the skill was built to match human judgment rather than the other way around.
- `evals/rubric.md` is the scoring criteria, versioned (rules changed partway through, so old runs are still graded against what was actually true when they ran).
- `evals/runs/` holds every test run's raw output and score, oldest to newest.
- `evals/findings.md`, `CHANGELOG.md`, and `decisions.md` are the running record of what went wrong, what changed in response, and why — the actual evidence trail behind every number in `case-study.md`.
- `scripts/` has the two automation tools described above.
