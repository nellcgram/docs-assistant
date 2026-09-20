# Doc Review

Each case is a snapshot of the file as it stood when I reviewed it. The files have changed since. Case 2 is the skill before `house-style.md` was extracted, and Case 3 is one entry from `decisions.md`, not the whole file.

## Case 1:  README

```
An agent skill that turns raw git commit messages into user-facing release notes, built and tested with Claude Code.

### Structure

- `.claude/skills/release-notes/` — the skill instructions
- `evals/cases/` — test cases (raw commits, selected for testing)
- `evals/gold/` — hand-written correct answers for a few cases
- `evals/rubric.md` — how output is scored
- `evals/runs/` — saved outputs from each test run
- `evals/findings.md` — diagnosis of what went wrong and why
- `shared/` — rules used by more than one skill
- `tools/` — descriptions of tools the skill can use
- `CHANGELOG.md` — record of changes to the skill, with reasons
- `decisions.md` — why the project is structured this way
```

## Case #2: Doc Review Skill

```
---
name: doc-review
description: Use when the user asks to check a document against a checklist.
---

## Purpose
The agent should check each rule when assessing a document.

## Rules
1. Check if the document states its purpose in the first paragraph/intro. Say pass, fail, or unverifiable.
2. Check if the document uses active instead of passive voice, and uses full sentences instead of sentence fragments. Say pass, fail, or unverifiable.
3. Check if the document has headings for every section. Say pass, fail, or unverifiable.
4. Check if the document uses the correct developer or user-facing voice for its audience. Say pass, fail, or unverifiable.
5. Check if links and code examples work. Say pass, fail, or unverifiable.
6. Check if format is consistent (terminology, code block style, headings). Say pass, fail, or unverifiable.
7. When a rule doesn’t apply — for example, if there are no links, no code samples, no sections that need headings, say so plainly; do not mark the item as fail. Say pass, fail, or unverifiable.

```

## Case #3: Decisions

```
### Rule 10 default-to-skip fix applied; holds in batched format, still gapped in isolated single-commit calls [2026-09-15]
**Decision:** I applied the fix left pending by the "Ambiguous feature-vs-portfolio commits default to skip" entry below, adding a clause to rule 10 (commit 512e384): "When a description could mean either the feature itself or its portfolio/project-level presence with no stronger signal, default to skip." I verified with two follow-up runs: Run 9 (batched, matching Runs 5/7's format) passed 8/8 and correctly skipped commit 12. Run 10 (5 repetitions of the isolated single-commit format that caused Run 6's original regressions, run via the new scripts/run-eval.py against the API directly) confirmed the fix holds for commit 12 specifically, but 4 of the 20 cases (commits 2, 6, 10, 18) still failed a subset of reps: not by refusing to decide as in Run 6, but by deciding and then appending a hedging follow-up asking for the diff, which still trips criterion 8.

**Why:** The isolated single-commit format has now caused two different failure modes at two different points (Run 6's outright non-decisions, Run 10's decide-then-hedge) despite two rounds of rule tightening (rules 3/4/10, then rule 10's default-to-skip clause). This suggests the format itself, not just remaining wording gaps, makes hedging more likely. Each isolated case has no other commit's context to calibrate confidence against, unlike the batched conversational format Runs 5, 7, and 9 all used.

**Status:** I applied rule 10 (512e384) but made no further rule change. Evals/findings.md logs the specific commits/reps from Run 10. I will hold off on another rule edit until it's confirmed this isn't specific to the script's call shape (a single system-prompt-plus-one-message call, no conversation, no tools) versus Claude Code's actual runtime, which is how Runs 1-9 were produced.

```