# Docs Assistant

This project builds two Claude Code skills, `release-notes` and `doc-review`, and evaluates them the way you would test production software. I wrote a first version of each skill, ran it against real cases, diagnosed why it failed, fixed the spec, and re-ran it.

**Start here:** [case-study.md](case-study.md) is the full write-up, with a file behind every claim. [evals/runs/README.md](evals/runs/README.md) lists every score in one line each.

## Results

| # | What it measures | Result |
|---|---|---|
| 1 | First version of `release-notes` | 0 of 20 cases |
| 2 | After diagnosing and fixing the spec | 19 of 20 |
| 3 | First scripted run | 15 of 20 |
| 4 | Whether the right skill fires (before and after rewording) | 18 of 20, then 18 of 20 |
| 5 | Handling of missing, unclear, and out-of-scope input | 3 of 10 |

A 5-repeat run found that only 9 of 20 cases pass every time, so the skill is correct more often than it is consistent. That run predates moving the shared rules into `shared/house-style.md`.

A GitHub Action now re-runs the 20 cases whenever a skill or shared file changes, and fails the check below a 0.75 pass rate. A deliberately broken skill scored 0.10 and failed it, and the fixed skill scored 0.85 and passed. The check grades only the four mechanical criteria, so it catches large regressions, not subtle ones: four of my five test breaks scored 0.80 to 0.85 and passed. The judgment criteria are still hand-graded. See `evals/findings.md` for the full test, with screenshots of the failing and passing runs.

## The two skills

**`release-notes`** turns raw git commit messages into user-facing release notes. The notes use the past tense, and they cover only changes a user of the product would notice. The skill also flags anything it couldn't verify. The test cases come from a real feature, the book-recommendation feature on [nellcgram.github.io](https://nellcgram.github.io), so "would a user notice this?" has a real answer. It took ten rounds of testing to hold up. `CHANGELOG.md` and `decisions.md` record each mistake it made along the way.

**`doc-review`** checks a document against a short checklist, such as whether it states its purpose up front and uses active voice. It reports pass, fail, or unverifiable for each item and says plainly when an item doesn't apply. I grounded it by hand-reviewing three real documents from this repo before writing any rule. Everything for this skill is still graded by hand.

Both skills share rules in `shared/house-style.md`. `shared/hard-surfaces.md` says what each should do when input is missing, unclear, or out of scope. `tools/read-commits.md` documents the input format `release-notes` expects.

## Running it yourself

You need an Anthropic API key:

```
export ANTHROPIC_API_KEY="sk-..."
pip install anthropic --break-system-packages
```

Then run these from the repo root:

- `python3 scripts/run-eval.py --name run-12` runs the 20 release-notes cases once and saves each response to `evals/runs/run-12/`. The script never overwrites an existing response, so give each run a new name.
- `python3 scripts/run-eval.py --name run-12 --repeats 5` runs each case 5 times (100 calls) into `evals/runs/run-12/rep-01/` through `rep-05/`.
- `python3 scripts/check-mechanical.py` grades every saved release-notes run on the automatable criteria and writes `evals/runs/mechanical-results.csv`. It only handles release-notes, because doc-review has no rubric yet.
- `python3 scripts/check-pass-rate.py --minimum 0.75 --run run-12` reads that CSV, scores only the `run-12` run, and exits with an error if the pass rate is below the minimum. The CI check runs this last.

A person still grades the judgment criteria, such as whether a skip was correct. Those grades go into `evals/runs/judgment-grades.csv`.

To run the check on GitHub, add your key as a repository secret named `ANTHROPIC_API_KEY` (Settings, then Secrets and variables, then Actions). Never put the key in the workflow file. Each CI run makes about 20 API calls.

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
- `.github/workflows/eval.yml` runs all three on every push that touches `.claude/skills/` or `shared/`.
