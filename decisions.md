# Decisions

This file records every judgment call in the project, newest first. Each entry says what I decided, why, and what happened next.

Short on time? Start with these three: [The CI test used an override, because four simpler breaks passed](#2026-09-21-the-ci-test-used-an-override-because-four-simpler-breaks-passed), [Run 1 vs Run 5 is the second number, not Run 6](#2026-09-17-run-1-vs-run-5-is-the-second-number-not-run-6), and [Unverifiable doesn't count against a commit](#2026-09-15-unverifiable-doesnt-count-against-a-commit).

## 2026-09-21: Every run uses one naming scheme
**Decision:** I renamed the scripted run `v3` to Run 11 and made the CI run name `run-12`, so every run follows the `run-NN` pattern. I also moved `run-06/grading.md` to `run-06.md`, so Run 6 keeps its grading file beside its folder like the other runs. I renamed `hard-cases-01.md` to `hard-cases-run-01.md` to match `trigger-run-01.md`.

**Why:** Two naming schemes made the run history harder to scan.

**Result:** Links, CSV row labels, and scripts all use the new names, and the scripts no longer recognize `vN` names. No score changed.

## 2026-09-21: The CI gate scores only the fresh run
**Decision:** `scripts/check-pass-rate.py` takes `--run run-12` and scores only the run the job just produced. It fails if it finds no matching rows.

**Why:** `mechanical-results.csv` holds every run in the project's history (340 rows before CI), so averaging all of them would let old good runs hide a new bad one. An eval that produced nothing must not pass.

## 2026-09-21: The threshold stays at 0.75
**Decision:** The check fails below 0.75. I considered 0.90 and rejected it.

**Why:** The first CI run of the correct skill scored 0.95, and the identical skill scored 0.85 after I reverted my test edits. A 0.90 threshold would have failed a good skill. Each case is worth 0.05, and one run varies by two or three cases. The trade-off is that mild regressions, like four of my five test breaks (0.80 to 0.85), pass the check. The check catches large regressions, and a person still reviews small ones. Details are in `evals/findings.md`.

## 2026-09-21: CI also watches `shared/`
**Decision:** The workflow runs on changes to `.claude/skills/` and `shared/`.

**Why:** `run-eval.py` sends the shared files to the model along with `SKILL.md`, so an edit to `shared/hard-surfaces.md` changes the skill's behavior. The first version watched only the skills folder, which would have let such an edit ship unchecked.

## 2026-09-21: The CI test used an override, because four simpler breaks passed
**Decision:** To prove the check can fail, I added a rule to `SKILL.md` that overrides the shared files ("write no note, only ask"). That scored 0.10 and failed the check. I then reverted it.

**Why:** Four earlier breaks passed: deleting rules, reversing the tense rule, and adding an "ask first" rule with and without rule 8. The shared files repeat the skill's key rules, so removing or contradicting one copy did nothing. I kept the four passing results in `evals/findings.md` because they show the gate's real sensitivity.

**Result:** The skill and shared files match the pre-test version exactly.

## 2026-09-19: Shared rules moved out of the skills
**Decision:** `shared/house-style.md` now holds only the three rules both skills use. Release-notes rules 5 and 8 became one-line pointers, and the six doc-review checklist rules moved back into doc-review's `SKILL.md`. Both skills point to `shared/hard-surfaces.md` by full path, and `run-eval.py` sends the shared files to the model.

**Why:** Each rule now has one source of truth. `house-style.md` duplicated `checklist.md`, and release-notes restated two shared rules. The script had to change too, because the API sees only the prompt, and moved rules would have vanished from every scripted run.

**Result:** The Run 11 numbers predate this change, and I haven't re-scored since. Later on 2026-09-21 I removed the two pointer rules and renumbered the skill, so the old rules 10, 11, and 12 are now rules 8, 9, and 10. Rule numbers in this file and in the run history are the numbers in force at the time.

## 2026-09-19: Hard cases scored against `hard-surfaces.md`: 3 of 10
**Decision:** I scored each of the 10 inputs in `evals/cases/hard-cases-10.md` against the matching bullet in `shared/hard-surfaces.md`, not just on which skill fired. Doc-review scored 1 of 5 and release-notes scored 2 of 5 (`evals/runs/hard-cases-run-01.md`).

**Why:** A routing check answers a different question. My first draft recorded only which skill fired and reported 4 of 10. Rescoring flipped two verdicts: doc-review ran the checklist on commits instead of saying it didn't apply, and release-notes never asked what "commit notes" meant.

**Result:** The skills now point to `hard-surfaces.md`, and I added the missing wrong-language and wrong-skill bullets. The description gap is still open.

## 2026-09-19: Input format documented, no new rules for merge commits
**Decision:** `tools/read-commits.md` describes the output of `git log --oneline -10` as the skill's input. I added no rule for merge commits or multi-change commits.

**Why:** The skill never runs a command and only receives pasted text. None of the 20 test commits is a merge commit, and every other rule here came from a failure I saw in a real run. If the skill later takes raw `git log` output, that gap becomes real.

## 2026-09-19: Scope limits I accepted
**Decision:** Doc-review reports pass, fail, or unverifiable, and `check-mechanical.py` covers release-notes only.

**Why:** The plan says "not applicable," but the skill, rubric, and gold review all use "unverifiable." Doc-review has no scored rubric yet, so a mechanical checker for it would have nothing to check against.

## 2026-09-18: The trigger reword didn't help: 18 of 20 both times
**Decision:** I reworded the release-notes description once (commit 1b78776) and stopped there, because the plan allows one rewording round. Prompts 4 ("fix my commits") and 6 ("apply review of these commits") should trigger release-notes, and both still missed.

**Why:** The reword added verbs that the passing prompts already used, so it couldn't help prompts that never say "release notes." I re-ran only the 10 release-notes prompts, because only that description changed.

## 2026-09-17: 9 of 20 cases hold across 5 repeats
**Decision:** I ran `run-eval.py --repeats 5` (100 calls, `evals/runs/run-11-stats.csv`). Nine of 20 cases pass in all 5 repeats. Commit 18 fails all 5, commit 6 fails 4, and eight correctly skipped commits fail at least one repeat by attaching a reason to a bare skip.

**Why:** Rule 4 is clear, so the model is ignoring it. I logged the causes in `evals/findings.md` and made no edit. This is an open item.

## 2026-09-17: Run 1 vs Run 5 is the second number, not Run 6
**Decision:** The first headline number is Run 1 (0 of 20) and the second is Run 5 (19 of 20). I don't use Run 6 (4 of 20).

**Why:** Runs 1 and 5 both ran as one batched request, so only the skill changed between them. Run 6 also changed the call format to 20 isolated calls, so pairing it with Run 1 would credit or blame the skill for something it didn't cause.

## 2026-09-17: Grading CSVs stay cumulative
**Decision:** `mechanical-results.csv` and `judgment-grades.csv` each hold every graded run, with a `run` column and a `case` column. The plan puts a separate copy in each run folder, and I chose otherwise on purpose.

**Why:** The point is comparing scores across runs, and one file per run would mean reconciling a dozen CSVs by hand.

## 2026-09-17: Write/skip answer key for the 20 test commits
**Decision:** The key writes notes for commits 1, 2, 4, 8, and 19 and skips the other 15. The skips include commit 6 (a fix to the skill's own description) and commit 12 (ambiguous, covered by the default-to-skip rule).

**Why:** Rule 4 skips anything a user of the skill can't see, and anything about the portfolio site, the evals, or the project itself. Commits 6 and 12 read like feature changes but fall under that rule.

**Result:** Run 8 scored 19 of 20 and Run 9 scored 20 of 20 against this key.

## 2026-09-17: Every run is graded one row per case
**Decision:** The rubric requires one graded row per case, and a whole run never gets a single "applies to all commits" judgment.

**Why:** A holistic grade can hide a violation in one of 20 commits. Run 5's original "7 of 7" summary hid commit 18's hedge this way.

## 2026-09-15: Mechanical and judgment grading split
**Decision:** `check-mechanical.py` grades criteria 1, 2, 4, and 8 from the text alone. A person grades criteria 3, 5, 6, and 7 against the actual commit. Criterion 8 uses both.

**Why:** A keyword check can't tell a legitimate aggregate skip line from one that carries a hidden justification. Automating the text checks makes 100-file runs practical, and hand grading keeps the combined score trustworthy. Cross-checking caught real mistakes, including Run 6's "0 of 20," which should have read 4 of 20.

**Result:** I applied this to Runs 4 through 11.

## 2026-09-15: Unverifiable doesn't count against a commit
**Decision:** A commit passes if none of its criteria is marked Fail.

**Why:** "Unverifiable" usually means a criterion doesn't apply, or that the model rightly declined to guess at an inaccessible repo. Counting it as a fail would fail nearly every commit.

**Result:** I applied this retroactively, and it corrected Run 6 from 0 of 20 to 4 of 20.

## 2026-09-15: Rule 10 gets a default-to-skip clause
**Decision:** When a description could mean the feature itself or its portfolio-level presence and nothing favors either, the skill defaults to skip (commit 512e384).

**Why:** Commit 12 flipped between write and skip across runs with no rule change. A missed note costs less than a fabricated one, and portfolio changes are already skipped.

**Result:** Run 9 passed 20 of 20. Run 10 (per-commit calls, 5 repeats) confirmed the fix for commit 12. Commits 2, 6, 10, and 18 still failed some repeats because they decide correctly and then hedge, so I held off on more rule edits.

## 2026-09-15: Run 6 regressed under per-commit calls, and I hardened the skill anyway
**Decision:** I first logged Run 6 with no fix, because editing the skill might only fix a test artifact. Run 7 (batched) then scored 20 of 20, which confirmed the call format caused the drop. I edited rules 3 and 4 and added rule 10 anyway.

**Why:** Nothing told the model to decide instead of ask, and a caller can't be relied on to always batch requests. `CHANGELOG.md` has the old and new wording.

## 2026-09-14: Portfolio and project-meta commits skip regardless of visibility
**Decision:** A commit that changes the portfolio site, the evals, or the project itself is skipped even when someone can see it, because a portfolio visitor isn't a user of the book-recommendation skill.

**Why:** I had dropped an earlier project-scope rule as redundant with the visibility check. Run 4 disproved that, because three portfolio and project commits got release notes. I applied the change to rule 4 and rubric criterion 3.

## 2026-09-14: Repo checking needs a stop condition
**Decision:** Rule 3 checks a repo only if one is already known in context. It never searches the filesystem, and it marks the commit unverifiable if the repo isn't reachable.

**Why:** Once repo checking was allowed, the model kept hunting for a repo, and the test hashes don't resolve anywhere. Run 4 scored well on its rubric, but the behavior was wrong, and I found that afterward. This rule replaced the earlier blanket ban and changed rubric criterion 6.

## 2026-09-14: Vague notes fail even when accurate
**Decision:** A note that drops the specific mechanism or outcome fails. "Adjusted when it asked" fails, and naming the default it applied passes.

**Why:** Three commits in Run 3 went through two revisions and were still too vague to be useful.

## 2026-09-14: Skipped commits get no output, and Run 1 added three rules
**Decision:** A skipped commit produces no line, which replaces the earlier "SKIP; reason" line. I also added rules for past tense, no internal file names, and not checking other repos.

**Why:** Run 1 showed the skill and rubric contradicting each other, and each new rule answered a failure it found.

## 2026-09-12: Gold answers and first rules
**Decision:** While hand-writing gold answers, I made four calls: notes speak to the user and not to a developer, commits with no user-visible effect are skipped, notes cite "Commit 4 (5da846a): sentence.", and a silent default must be stated.

**Why:** These were the patterns across my own hand-written entries, and I needed one consistent format before grading multiple runs. I encoded them in `SKILL.md` the next day.
