# Decisions

Every judgment call in this project, newest first. Each entry says what I decided, why, and what happened next.

## 2026-09-19 — Shared rules moved out of the skills (Step E)
**Decision:** `shared/house-style.md` holds only the three rules both skills use. Release-notes rules 5 and 8 became one-line pointers to it, and the six doc-review checklist rules moved back into doc-review's SKILL.md. Both skills now point to `shared/hard-surfaces.md` and give the full path to `house-style.md`. `scripts/run-eval.py` sends the shared files to the model with SKILL.md.

**Why:** Step E keeps one source of truth for each rule. `house-style.md` held doc-review's checklist items, which duplicated `checklist.md`, while release-notes still restated two shared rules. The script had to change too, because the API sees only what goes in the prompt, and the moved rules would have vanished from every scripted run.

**Status:** Applied. I haven't re-scored the skill since, so the v3 numbers predate the change. I kept rules 5 and 8 numbered so the run history's rule numbers still hold.

## 2026-09-19 — Housekeeping calls
**Decision:**
- **Doc-review reports pass, fail, or unverifiable.** The plan says "not applicable," but the skill, the rubric, and the gold review all use "unverifiable." An item that doesn't apply reports as unverifiable.
- **Run files keep the names `run-01.md` through `run-10.md`,** not the plan's `run-01-v1.md` and `-v2` pair. Diagnosing Run 1 took four rounds of fixes (Runs 2 to 5), so a pair didn't fit.
- **`check-mechanical.py` stays release-notes-only.** Its criteria are specific to release notes, and doc-review has no rubric yet.

**Why:** Each keeps one convention across the project and stops the plan from disagreeing with the files.

**Status:** Applied.

## 2026-09-19 — Hard cases scored against `hard-surfaces.md`: fifth number is 3 of 10
**Decision:** I scored each of the 10 inputs in `evals/cases/hard-cases-10.md` against the matching bullet in `shared/hard-surfaces.md`, not just on which skill fired. The result is **3 of 10**: doc-review 1 of 5 and release-notes 2 of 5 (`evals/runs/hard-cases-01.md`). Each input ran once.

**Why:** Step J calls for scoring against the file, and a routing check answers a different question. My first draft only recorded which skill fired and reported 4 of 10. Rescoring changed several verdicts. Doc-review input 1 flipped to a fail because the response ran the checklist on commits instead of saying the skill doesn't apply. Release-notes input 5 ("commit notes") flipped to a fail because the response never asked what the prompt meant.

**Status:** Applied. Open items:
- Neither SKILL.md pointed to `hard-surfaces.md`, and the `house-style.md` references had no path. Both are fixed.
- `hard-surfaces.md` had no bullet for a wrong-language document or a wrong skill named. I added both on 2026-09-19 (`CHANGELOG.md`).
- The hard-cases file headings say "docs-review" and the skill is `doc-review`.

## 2026-09-19 — Step K documents the input format only; no new rules for merge or multi-change commits
**Decision:** `tools/read-commits.md` describes the output of `git log --oneline -10` as the skill's input format. It doesn't lead to a rule or hard case for merge commits ("Merge pull request #7 ...") or for commits that bundle several changes on one line.

**Why:** The skill never runs a command. It receives pasted text, so the file documents an input shape, not a live tool. None of the 20 test commits is a merge commit, and every other rule in this project came from a failure I saw in a real run. If the skill later takes raw `git log` output directly, the merge-commit gap becomes real and worth a rule.

**Status:** Applied. The file couldn't check whether the numbering in `release-notes-20.md` runs oldest first, because those hashes don't exist in this repo, and it says so.

## 2026-09-18 — Trigger reword didn't move the result: fourth number is 18 of 20 both times
**Decision:** Prompts 4 ("fix my commits") and 6 ("apply review of these commits") are indirect phrasings that should trigger release-notes, and that expectation stands. After the one description reword that Step I calls for (commit 1b78776), run 2 matched run 1: both prompts still missed. Release-notes scored 8 of 10 and the total was **18 of 20** in both runs.

**Why:** The reword added explicit verbs to a description whose passing prompts already used them, so it couldn't help prompts that never say "release notes." I re-ran only the 10 release-notes prompts, since only that skill's description changed, which is fewer than the plan's 20. Both runs included the commits or docs with every prompt. Run 1's file said otherwise until I corrected it.

**Status:** Applied. Step I allows one rewording round, so I stopped there. The before and after comparison is the result.

## 2026-09-17 — Phase 8 (context arrangement) not attempted
**Decision:** I didn't run the plan's Phase 8, which tests whether identical instructions score differently when arranged inline, split into `examples.md`, or read late in a long session. No sixth number exists.

**Why:** I spent the time on grounding the second skill (Phase 7) and on verifying the mechanical and judgment grading (Phase 5). Both surfaced concrete problems. Phase 8 asks a narrower question and doesn't block any other phase.

**Status:** Not done. `case-study.md` says so.

## 2026-09-17 — Fresh 5-repeat run: only 9 of 20 cases hold across all 5 reps
**Decision:** I ran `scripts/run-eval.py --repeats 5` into `evals/runs/v3/rep-01` through `rep-05` (100 calls), graded in `evals/runs/v3-stats.csv`. Nine of 20 cases pass every criterion in all 5 reps. Commit 18 fails all 5, commit 6 fails 4, and eight correctly skipped commits fail at least one rep by attaching a per-commit reason to a bare skip.

**Why:** Rule 4 says a skip gets no entry or one aggregate line, so this is the model ignoring a clear rule. Causes are in `evals/findings.md`.

**Status:** Logged, and I made no SKILL.md edit. It's an open item.

## 2026-09-17 — Run 1 vs Run 5 is the second number, not Run 6
**Decision:** The first number is Run 1 (0 of 20, graded against the Version 1 rubric). The second is **Run 5 (19 of 20, Version 2 rubric)**. Run 6 (4 of 20) isn't used.

**Why:** Runs 1 and 5 both ran as one batched request in a single conversation, so only the skill changed between them. Run 6 also changed the call format to 20 isolated calls. Pairing it with Run 1 would credit or blame the skill for a change it didn't cause. Run 6 belongs with the consistency story in Phase 6.

**Status:** Applied. `case-study.md` cites this pairing.

## 2026-09-17 — Grading CSVs stay cumulative
**Decision:** `evals/runs/mechanical-results.csv` and `evals/runs/judgment-grades.csv` hold every graded run in one file each, with a `run` column and a `case` column. The plan puts a separate copy inside each run's folder.

**Why:** The point of Phases 2 through 6 is comparing scores across runs. One file per run means reconciling a dozen CSVs by hand. A single file with a `run` column is the standard shape for this data.

**Status:** Applied on purpose, not an oversight.

## 2026-09-17 — Write/skip ground truth for the 20 test commits
**Decision:** Write commits 1, 2, 4, 8, and 19. Skip everything else, including commit 6 (an internal fix to the skill's own description) and commit 12 (ambiguous, covered by the default-to-skip rule).

**Why:** Rule 4 skips anything a user of the skill can't see and anything about the portfolio site, evals, or the project itself. Commits 6 and 12 both fall under it even though they read like plausible feature changes.

**Status:** Applied. `run-08.md` scores 19 of 20 and `run-09.md` scores 20 of 20 against this truth.

## 2026-09-17 — Every run is graded one row per case
**Decision:** `evals/rubric.md` now requires one graded row per case, out of N. A whole run may never get a single "applies to all commits" judgment.

**Why:** A holistic grade can hide a violation in one of 20 commits, and it makes runs impossible to compare case by case. Run 5's original "7 of 7" summary hid commit 18's hedge this way.

**Status:** Applied to the rubric and every run graded since.

## 2026-09-15 — Mechanical and judgment grading split
**Decision:** `scripts/check-mechanical.py` grades criteria 1, 2, 4, and 8 from text alone into `evals/runs/mechanical-results.csv`. A person grades criteria 3, 5, 6, and 7 against the actual commit into `evals/runs/judgment-grades.csv`. Criterion 8 uses both. The script catches an explicit request for clarification, and a person catches a quiet reason attached to a skip.

**Why:** A keyword check can't tell a legitimate aggregate skip line from one carrying a hidden justification. Automating the text checks makes grading Run 10's 100 files practical, and keeping judgment by hand keeps the combined score trustworthy. Cross-checking the two caught real mistakes, including Run 6's "0 of 20" summary, which should have read 4 of 20.

**Status:** Applied to runs 4 through v3. The rubric retagging missed criterion 5 at first and now tags it "judgment."

## 2026-09-15 — Unverifiable doesn't disqualify a commit from the pass count
**Decision:** A commit counts as passing if none of its criteria are marked Fail. Unverifiable doesn't count against it.

**Why:** Unverifiable usually means the criterion doesn't apply (for example, no fallback exists to explain), or the model correctly declined to guess at an inaccessible repo. Counting it against a commit would make nearly every commit fail, since almost all of them hit Unverifiable on criterion 3, 5, or 6.

**Status:** Applied retroactively, and it corrected Run 6 from 0 of 20 to 4 of 20.

## 2026-09-15 — Rule 10 gets a default-to-skip clause
**Decision:** When a description could mean the feature itself or its portfolio-level presence and nothing favors either reading, default to skip (commit 512e384).

**Why:** Commit 12 ("Take Book Recommendations project offline") flipped between write and skip across runs with no rule change in between. Rule 10 said to pick the better-supported reading but gave no tiebreak. Skip is the safer default, because a missed note costs less than a fabricated one and portfolio changes are already skipped.

**Status:** Applied. Run 9 (batched) passed 20 of 20. Run 10 (per-commit calls, 5 reps) confirmed the fix for commit 12, but commits 2, 6, 10, and 18 still failed some reps. They decide correctly and then hedge, so I held off on more rule edits. The working theory is that the per-commit format itself invites hedging.

## 2026-09-15 — Run 6 regressed under per-commit calls; I hardened the skill anyway
**Decision:** Run 5 (batched) passed, so I left the skill alone. Run 6 ran each commit as its own call and regressed. I logged it without a fix, because editing the skill might have fixed a test artifact. Run 7 (batched again) passed 20 of 20, which confirmed the format caused the regression. I edited rules 3 and 4 and added rule 10 anyway.

**Why:** Nothing in the skill told the model to decide instead of ask, and rule 3's "flag the discrepancy" language for verified conflicts had spread to every ambiguous description. A caller can't be relied on to always batch requests, so the behavior needed a rule regardless.

**Status:** Applied. Old and new wording is in `CHANGELOG.md`.

## 2026-09-14 — Portfolio-site and eval/project-meta commits skip regardless of visibility
**Decision:** A commit is skipped if it changes the portfolio site, the evals, or the project itself, even when someone can see the effect. A portfolio visitor isn't a user of the book-recommendation skill. I added a meta example next to the technical one.

**Why:** On 2026-09-12 I had dropped an earlier project-scope rule as redundant with the visibility check. Run 4 disproved that. Three portfolio and project commits passed the visibility check and got written up as release notes.

**Status:** Applied to rule 4 and rubric criterion 3.

## 2026-09-14 — Repo-check rule needs a stop condition
**Decision:** Rule 3 checks a repo only if one is already known in context. It never searches the filesystem or guesses at locations, and it marks the commit unverifiable if the repo isn't accessible.

**Why:** Once repo checking was allowed, the model kept hunting for a repo. The test hashes are synthetic and don't resolve anywhere. Run 4 scored well on its own rubric, but the behavior was wrong. Grading missed it, and I found it afterward.

**Status:** Applied to rule 3 and rubric criterion 6.

## 2026-09-14 — Commit #1's test input restored
**Decision:** I restored `release-notes-20.md` commit 1 to its own wording ("specifying the exact heading to look for in the already-read file"). An edit meant for commit 19 had landed on it.

**Why:** Commit 1 had picked up wording that described commit 19's change. I caught it before Run 4 used the file.

**Status:** Applied.

## 2026-09-14 — Vague notes fail even when accurate
**Decision:** A release note fails if it's accurate but drops the specific mechanism or outcome. "Adjusted when it asked" fails, and naming the default it applied passes.

**Why:** Three commits in Run 3 went through two rounds of revision and were still too vague to be useful.

**Status:** Applied to the skill and rubric.

## 2026-09-14 — "Don't check other repos" became "don't check any repo"
**Decision:** I broadened the rule so it forbids checking any repo for commits.

**Why:** Run 2 showed the model still looking commits up itself under the narrower wording.

**Status:** Applied. Rule 3 later replaced the ban with the stop condition above.

## 2026-09-14 — CHANGELOG entries quote old and new wording and cite a commit
**Decision:** Each `CHANGELOG.md` entry names the commit that made the change and quotes the wording before and after.

**Why:** A paraphrase can't be checked against what the rule actually said.

**Status:** Applied to every entry since.

## 2026-09-14 — The skill does one job
**Decision:** I removed a "rules for changelog" section from SKILL.md and reverted its description to release notes only. Changelog entries about the skill's own edits are written by hand in `CHANGELOG.md`.

**Why:** Mixing two rule sets made it unclear which one a run was following and complicated grading.

**Status:** Applied.

## 2026-09-14 — Skipped commits get no output, and Run 1 added tense, filename, and repo rules
**Decision:** A skipped commit produces no line at all, which replaced the earlier "SKIP; reason" line. I also added three rules: write in past tense only, never name internal files like skill, rubric, eval, or findings, and don't check other repos.

**Why:** Run 1 showed the skill and rubric contradicting each other. The model followed the skill's SKIP-line instruction and still failed the rubric. The three new rules answered failures Run 1 found: mixed tenses, internal filenames, and stopping to ask about other repos.

**Status:** Applied. The SKIP line was useful while hand-writing gold answers but is wrong for shipped output.

## 2026-09-12 — Gold answers and first rules
**Decision:** While hand-writing gold answers I made five calls:
- Release notes speak to the user, not a developer.
- Commits with no user-visible effect get skipped. Two examples were adding entries to `already-read-example.md` and moving the rubric into the evals folder.
- Commits cite in the form "Commit 4 (5da846a): sentence."
- A silent default must be stated. A fallback to the contemporary genre needs to say so, or it looks like a bug or a lucky guess.
- Skips got a "SKIP; reason" line at first, so a grader could tell an absent line from a verified no-note case. That line is now gone (see above).

**Why:** These were the patterns visible across my own hand-written entries, and I needed one consistent format before grading multiple runs.

**Status:** Applied to `evals/gold/release-notes.md` and encoded in SKILL.md the next day.
