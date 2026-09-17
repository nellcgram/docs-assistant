# Doc Review Gold

## Case 1: README

**Issues:**
- Description should include doc review and that the eval harness tests skills
- Why was the agent built; are commits not strong enough?
- Should decisions.md be left out of project since this is for the case study?

**Missing:**
- Skills included — list each skill (doc-review, release-notes) with a one-liner on what it does.
- How to run evals — command(s) to run the eval harness, where cases/gold files live (evals/cases/, evals/gold/), and how grading works (you mentioned mechanical vs. judgment grading split).
- Adding a new eval case — the convention for naming/structuring case + gold files, since that's a repeatable task.
- Directory structure — brief map of key folders (skills/, evals/cases/, evals/gold/).
- Requirements/setup — any dependencies, API keys, or Claude Code version assumptions.

## Case 2: Skill
- Should there be any intro to the skill that says what it does?
- Can the Rules' wording be cut down at all?

## Case 3: Decisions.md
- This is engineering log and will need to be shortened for case study
- Why was it built?

**Main points so far:**
- Skip rule is about visible effect, not how technical the wording sounds (2026-09-14 2:28 PM)
- Vague-but-accurate notes still fail — need specific mechanism/outcome (2026-09-14 2:28 PM)
- Repo-check needs an explicit stop condition, not just permission to check (2026-09-14 8:49 PM)
- Portfolio/eval/meta commits skip regardless of visibility (2026-09-14 9:05 PM)
- Isolated single-commit calls induce hedging/asking that batched calls don't — a call-format artifact, not just a wording gap (Run 6 → Run 7 → Run 10, spanning three entries)
- Splitting mechanical vs. judgment grading to make scoring scale (2026-09-15)