# Changelog

This file lists every change to a skill, its rubric, or the eval tooling, newest first. Rule changes quote the old and new wording and give the reason. Scores are in `evals/runs/README.md`, failure causes are in `evals/findings.md`, and the reasoning is in `decisions.md`.

## 2026-09-23: Default-to-skip exception and gold-write guard
- **`shared/house-style.md` rule 3:** the old wording, "When a skill silently defaults to something, say that a default was applied," conflicted with `release-notes` rule 8 (default to skip) and rule 4 (no per-commit skip explanations). It now adds: "Exception: a default-to-skip is not announced per commit. The skill reports skips only in one aggregate line." The release-notes skill itself is unchanged.
- **`release-notes/SKILL.md` Purpose:** it now says the skill "is written for the book-recommendation project's release notes."
- **`scripts/check-mechanical.py`:** a new column, `gold_commit_written`, fails a case when the gold file says the commit gets a note (commits 1, 2, 4, 8, 19) but the response skipped, asked about, or missed it. It reads the commit list from `evals/gold/release-notes.md`. No run's pass count changed. It flags Run 6 case 2, which already failed criterion 8.
- **`scripts/check-pass-rate.py`:** a new `--min-gold` gate (default 0.6). Without it, a skill that skips all 20 commits would still pass 15 of 20 (0.75). A simulated skip-everything run now fails.
- **`evals/runs/judgment-grades.csv`:** Runs 4, 5, 6, and 7 had one row per group of commits. They now have 20 rows each, copied from the existing grades in `run-04.md` through `run-07.md`. No grade changed.

## 2026-09-23: Wording fixes (no rule change)
- **`shared/hard-surfaces.md`:** the release-notes section said to decide every commit "under rules 3, 4, and 10*", with a footnote admitting the current rule is 8. It now says "rules 3, 4, and 8" and the footnote is gone. The rule itself is unchanged.
- **Both `SKILL.md` files:** the Purpose line said "The agent" and now says "This skill". `doc-review` rule 7 also lost a double space.
- **Old runs:** they were scored on the earlier wording and I did not re-score them.

## 2026-09-21: Release-notes rules renumbered
I removed the two pointer rules (old rules 5 and 8) from `release-notes/SKILL.md`, because `shared/house-style.md` already states them. The remaining rules moved up, so the old rules 10, 11, and 12 are now rules 8, 9, and 10. I also changed the rule 1 example to "…so you will not be shown books you've already read." Earlier entries and run files use the rule numbers in force at the time.

## 2026-09-21: Run names standardized (no skill edit)
I renamed `v3` to Run 11 and `v4` to `run-12` so every run follows the `run-NN` pattern, and updated the scripts, CSVs, and links to match. No score changed.

## 2026-09-21: CI check added (no skill edit)
A GitHub Action now re-runs the 20-case eval on every push that touches `.claude/skills/` or `shared/`, and it fails the check if the pass rate drops below 0.75.
- **`.github/workflows/eval.yml`:** The workflow runs `run-eval.py`, `check-mechanical.py`, and then the gate. The API key is a repository secret and never appears in the file.
- **`scripts/check-pass-rate.py` (new):** It reads `mechanical-results.csv`, scores only the run the job just produced (`--run run-12`), and exits nonzero below the minimum. It also fails when no rows match, so a run that produced nothing can't pass.
- **Testing:** I broke `SKILL.md` on purpose in five temporary ways and reverted every one. Only the last break failed the check (0.10), and `evals/findings.md` has the results and screenshots of the failing and passing runs. The skill and shared files are byte-identical before and after the tests.

## 2026-09-19: Shared rules and hard-input handling
The hard-cases run showed that neither skill pointed to `shared/hard-surfaces.md` and that `house-style.md` held checklist items only doc-review used.
- **Release-notes rules 5 and 8:** They now point to `shared/house-style.md` (defaults must be stated, and no internal file names). They keep their numbers so "rule 10" in the run history still means the same rule.
- **Release-notes rule 11:** "Follow the shared rules in house-style.md" became "Follow the shared rules in shared/house-style.md," because the agent couldn't find the file without the path.
- **Release-notes rule 12 (new):** "When the input is missing, unclear, or out of scope, follow the release-notes section of shared/hard-surfaces.md."
- **Release-notes rule 1 example:** The old example used the present tense and named "the skill," which broke the skill's own rules. The new example reads: "Checked your already-read list before recommending, so you were not shown books you had already read."
- **Release-notes Purpose:** The old text was copied from doc-review. The new text reads: "The agent turns raw git commit messages into user-facing release notes."
- **Doc-review:** The skill now has one rule per checklist item and a rule that marks non-applicable items unverifiable. It also references both shared files.
- **`shared/house-style.md`:** I cut it from nine rules to the three that both skills use.
- **`shared/hard-surfaces.md`:** The release-notes section now says "decide every commit… Never ask about a commit," because its "ask" bullets contradicted rule 10. Both skills gained a "wrong skill named" case, and doc-review gained "wrong language."
- **Gold file:** I rewrote `evals/gold/release-notes.md` to match the skill (5 commits get notes and 15 are skipped).
- **Scripts:** `run-eval.py` now sends the shared files to the model, because the API otherwise sees only `SKILL.md`. It also takes `--name` and refuses to overwrite a response. `check-mechanical.py` now flags any `.md` file name and no longer counts an unaddressed commit as a pass, and it reproduces all 340 earlier rows unchanged.

## 2026-09-19: Hard cases run 1 (no skill edit)
The run scored 3 of 10. I added `shared/hard-surfaces.md` and `tools/read-commits.md` (the real input format). I also corrected `trigger-run-01.md`, which had wrongly said the prompts ran without their commits.

## 2026-09-18: Trigger reword and a doc-review edit
- **Release-notes `description:`** The old text read "Use when the user asks for release notes generated from commit messages." The new text reads "Use when the user asks to create, write, generate, add release notes from commit messages." The score stayed at 18 of 20 before and after, so I kept the reword although it wasn't a fix.
- **Doc-review rule 2:** I cleaned up the grammar, which went beyond the description-only scope of that step. I did not re-score doc-review.

## 2026-09-17: Run 11, the first scripted run (no skill edit)
Run 11 scored 15 of 20, and its 5-repeat variant had 9 of 20 cases clean in all 5 repeats. Both failed on rule 4: the model attached reasons to skips and wrote up commits 6 and 18 instead of skipping them. The rule is already clear, so I logged the failures and didn't rewrite it.

## 2026-09-15: Rule 10 default-to-skip (commit 512e384)
Run 8 wrote a note for commit 12 ("Take Book Recommendations project offline"), which Run 7 had skipped, because rule 10 had no tiebreak.
- **Added:** "When a description could mean either the feature itself or its portfolio/project-level presence with no stronger signal, default to skip."
- **Result:** Run 9 scored 20 of 20.

## 2026-09-15: Mechanical grading added
`scripts/check-mechanical.py` scores criteria 1, 2, 4, and 8 from the response text into `mechanical-results.csv`. A person grades criteria 3, 5, 6, and 7 into `judgment-grades.csv`. Regrading with this split corrected Run 6 from 0 of 20 to 4 of 20.

## 2026-09-15: Fixes after Run 6
Run 7 (batched again) scored 20 of 20, which showed the call format caused Run 6's regression. I fixed the wording anyway, because callers can't be relied on to batch.
- **Rule 3:** I added "mark unverifiable and still write or skip the entry… Do not stop the response to ask which reading is correct."
- **Rule 4:** I added "do not write a paragraph explaining, defending, or reconsidering a skip decision." A single aggregate line of skipped numbers is still allowed.
- **Rule 10 (new):** "Do not stop to ask the user to disambiguate a commit before finishing the response; decide using the rules above." I also added a matching rubric criterion 8.

## 2026-09-14: Run 4 fixes
- **Rule 4 (bc6eef7):** Portfolio, eval, and project-meta commits now skip even if someone can see them, because Run 4 wrote notes for three such commits. The old rule read "Skip a commit if the effect is not visible to the user." The new rule adds "…if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone."
- **Rule 3 (bc6eef7):** The repo check gained a stop condition: "Only check the repo if it is known in context; do not search the filesystem… If not immediately accessible, mark unverifiable."
- **Rule 3 (b29e33d):** The ban on checking repos became permission to verify a commit hash and flag a mismatch.
- **Rule 4 example (ae5dcb5):** A technical-sounding commit that changes what users see is now included and not skipped.
- **Rubric versioned (034a3c5):** I kept Version 1 (Runs 1 to 3) as graded. Version 2 (Run 4 on) drops the "never check repos" criterion and adds a conflict-flag criterion.
- **Test inputs:** I restored commit 1's wording after an edit meant for commit 19 landed on it (21039c5). I also replaced all 20 hashes with synthetic ones so the model can't look them up (3091109).

## 2026-09-14: Runs 1 to 3 fixes
- **Run 1 (a59fc9d) scored 0 of 20 because the skill and rubric disagreed.** I added "Write all release notes in the past tense only," a rule against internal file names, and a rule against checking other repos. I removed the SKIP line, because the rubric wanted no note at all for a skipped commit.
- **Run 2 (4dc4c81):** "Do not check other repos" became "Do not check any repo," because the model still looked commits up.
- **Run 3:** Commits 4 and 19 in the test file were too vague to demand a precise note, so I made them specific.
