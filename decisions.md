# Decisions

## [2026-09-17] — Phase 8 (context arrangement) not attempted
**Decision:** The plan's Phase 8 — testing whether identical skill instructions score differently depending on arrangement (inline vs. referenced via `examples.md`, vs. read late in a long session) — was not run. No sixth number exists.

**Why:** Time was spent instead on grounding the second skill (Phase 7) and on the mechanical/judgment grading verification (Phase 5), both of which surfaced real, concrete issues worth fixing. Phase 8 tests a different, narrower question (token arrangement sensitivity) that doesn't depend on anything built so far, so skipping it doesn't block any other phase's numbers.

**Status:** Not done. Logged here explicitly, per the plan's own instruction for this exact situation, rather than left to silently disappear — see `case-study.md`'s "Context arrangement (Phase 8): not attempted" section. If picked back up, the plan's Phase 8 steps (split `SKILL.md`'s worked examples into `examples.md`, run the same 20 cases inline vs. referenced vs. late-session) are unchanged from the original.

## [2026-09-17] — Fresh 5-repeat variance run: only 9 of 20 cases hold up across all 5 reps
**Decision:** Ran the statistical-rigor test (`scripts/run-eval.py --repeats 5`) into `evals/runs/v3/rep-01` through `rep-05` (100 calls), graded in `evals/runs/v3-stats.csv`. **9 of 20 cases pass every criterion in all 5 reps.** Commit 18 fails all 5 (wrote a note instead of skipping in 4, hedged in all 5). Commit 6 fails 4 of 5 (same skip-rule miss). Eight more otherwise-correctly-skipped commits (7, 10, 11, 12, 13, 14, 16, 20) fail at least one rep by adding an unauthorized per-commit justification clause to an otherwise bare skip line — a rule 4 violation ("a single aggregate line listing skipped commit numbers is fine; per-commit justification is not").

**Why:** Rule 4 is explicit that a skip gets no entry or one bare aggregate line, never a reason attached to an individual commit, and the skill does this across a wide set of commits under no current rule change.

**Status:** Applied. `evals/runs/v3-stats.csv`, `mechanical-results.csv`, and `judgment-grades.csv` all reflect this run. No SKILL.md or rubric edit made from this finding yet — logged here and in findings.md as an open item.

## [2026-09-17] — Run 1 vs Run 5 is the second number, not Run 6
**Decision:** The first number is Run 1 (0 of 20, `evals/runs/run-01.md`, graded against the Version 1 rubric). The second number is **Run 5 (19 of 20, `evals/runs/run-05.md`, graded against the Version 2 rubric)** — commit 18 hedged ("I'm not confident; let me know if you want it included") instead of deciding. Run 6 (4 of 20) is not used as the second number.

**Why:** Run 1 and Run 5 were both run the same way — one batched request covering all 20 commits in a single conversation — so the only thing that changed between them is the skill itself (fixed after Run 1's findings, and again after Run 4's). Run 6 deliberately changed the call format to 20 isolated single-commit API calls to stress-test robustness; pairing it with Run 1 would credit or blame the skill for a format change it didn't cause, mixing two variables into one number. Run 6 belongs with the Phase 6 consistency story, not with Phase 3's diagnose-fix-reverify number.

**Status:** Applied. This is the pairing case-study.md should cite for Phase 3's "second number" — 19 of 20.

## [2026-09-17] — Grading CSVs stay cumulative at evals/runs/, not split per-run inside each run's own folder
**Decision:** `evals/runs/mechanical-results.csv` and `evals/runs/judgment-grades.csv` hold every graded run in one file each, distinguished by a `run` column and a `case` column — not a separate copy of each file inside `evals/runs/<run>/`, which is what the original project plan describes.

**Why:** A hiring manager reading this project needs to compare scores across runs — that's the entire point of Phases 2-6 (first number vs. second number, Run 8 vs. Run 9, consistency across reps). One file per run, scattered across folders, makes that comparison harder: you'd have to open and reconcile a dozen separate CSVs by hand instead of filtering one. A single file with a `run` column is the standard shape for this kind of data.

**Status:** Applied; not planned to change. A deliberate deviation from the plan's literal file layout, not an oversight.

## [2026-09-17] — Write/skip ground truth for all 20 test commits
**Decision:** The correct write/skip split for `evals/cases/release-notes-20.md`: **write** commits 1, 2, 4, 8, 19 (5 commits); **skip** everything else, including commit 6 (1e3c29b, "Edited skill 'what it does' to be accurate" — an internal SKILL.md self-description fix, never seen by a user of the recommender) and commit 12 (6fce484, ambiguous, covered by the default-to-skip rule below).

**Why:** SKILL.md rule 4 skips a commit if its effect isn't visible to a user of the book-recommendation skill or if it's a portfolio-site/eval/project-meta change; commit 6 and 12 both fall under that even though they read as plausible feature changes at a glance.

**Status:** Applied. `run-08.md` and `run-09.md` graded against this ground truth for all 20 commits: `run-08.md` is 19 of 20 (commit 12's misclassification fails), `run-09.md` is 20 of 20.

## [2026-09-17] — Mechanical and judgment grading, cross-checked
**Decision:** `scripts/check-mechanical.py` grades criteria 1, 2, 4, and 8 automatically, one row per case per run, into `evals/runs/mechanical-results.csv`. Criteria 3, 5, 6, and 7 need judgment against the actual commit content and are hand-graded into `evals/runs/judgment-grades.csv`, same row-per-case layout. Criterion 8 has both a mechanical half (did it explicitly ask for clarification — keyword-detectable) and a judgment half (did it silently attach an unauthorized reason to a skip without asking — not reliably keyword-detectable, since a bare, aggregate-shaped line can still carry an attached per-commit reason), so it's graded by both methods together rather than by the script alone.

**Why:** Automating the mechanical half makes grading every case of every run tractable; keeping the judgment half separate and hand-graded is what makes the combined score trustworthy, since a script pattern-matching on wording can't tell a legitimate aggregate skip line from one that still carries a hidden justification.

**Status:** Applied across every graded run (4 through v3).

## [2026-09-17] — Every run graded one row per case, out of N; no more run-level aggregate judgments
**Decision:** Added a grading rule to `evals/rubric.md`: every run is graded one row per case, out of N (N = number of input commits in that run). A whole run may never be graded as a single "applies to all commits" aggregate judgment again, even when every case happens to score the same.

**Why:** Grading a whole run as one holistic judgment can miss a violation buried in one of 20 commits in a way that grading case-by-case can't — and it makes runs impossible to compare case-for-case against each other. Locking in one consistent shape prevents both problems.

**Status:** Applied to `evals/rubric.md`, and to every run graded since.

## [2026-09-15] — Rule 10 default-to-skip fix applied; holds in batched format, still gapped in isolated single-commit calls
**Decision:** Applied the fix left pending by the "Ambiguous feature-vs-portfolio commits default to skip" entry below, adding a clause to rule 10 (commit 512e384): "When a description could mean either the feature itself or its portfolio/project-level presence with no stronger signal, default to skip." Verified with two follow-up runs: Run 9 (batched, matching Runs 5/7's format) passed 8/8 and correctly skipped commit 12. Run 10 (5 repetitions of the isolated single-commit format that caused Run 6's original regressions, run via the new scripts/run-eval.py against the API directly) confirmed the fix holds for commit 12 specifically, but 4 of the 20 cases (commits 2, 6, 10, 18) still failed a subset of reps — not by refusing to decide as in Run 6, but by deciding and then appending a hedging follow-up asking for the diff, which still trips criterion 8.

**Why:** The isolated single-commit format has now caused two different failure modes at two different points (Run 6's outright non-decisions, Run 10's decide-then-hedge) despite two rounds of rule tightening (rules 3/4/10, then rule 10's default-to-skip clause). This suggests the format itself, not just remaining wording gaps, makes hedging more likely — each isolated case has no other commit's context to calibrate confidence against, unlike the batched conversational format Runs 5, 7, and 9 all used.

**Status:** Rule 10 clause applied (512e384). No further rule change made yet — evals/findings.md logs the specific commits/reps from Run 10. Holding off on another rule edit until it's confirmed this isn't specific to the script's call shape (a single system-prompt-plus-one-message call, no conversation, no tools) versus Claude Code's actual runtime, which is how Runs 1-9 were produced.

## [2026-09-15] — Mechanical criteria split out from judgment criteria for scripted grading
**Decision:** Added scripts/check-mechanical.py to grade rubric Version 2 criteria 1 (past tense), 2 (one note per commit), 4 (no internal filenames), and 8 (decided every commit without asking or hedging) automatically from run output text, writing evals/runs/mechanical-results.csv. Criteria 3, 6, and 7 stay hand-graded in evals/runs/judgment-grades.csv. Retagged evals/rubric.md's Version 2 criteria 3, 6, and 7 from "mechanical" to "judgment" to match (commit a432401).

**Why:** Criteria 1, 2, 4, and 8 can be checked with text pattern matching alone; criteria 3 (skip-rule correctness), 6 (conflict-flag/unverifiable), and 7 (factual accuracy plus specific mechanism) all require comparing the response against what the actual commit means, which a script can't do. Automating the mechanical half makes re-grading past runs and grading Run 10's 100 case files (5 reps × 20 commits) tractable, since only the judgment half needs to be graded by hand.

**Status:** Applied: scripts/check-mechanical.py and scripts/run-eval.py added; evals/runs/mechanical-results.csv and evals/runs/judgment-grades.csv created; runs 4 through 10 graded with this split (evals/runs/grading-total.md, run-10-stats.csv), which is what surfaced and corrected Run 6's "0 of 20" summary-line error (see the entry below). evals/rubric.md criterion 5 was found still tagged "mechanical" (the a432401 retagging pass missed it, despite it being graded in judgment-grades.csv, not checked by the script) and has since been corrected to "judgment." (`grading-total.md` itself was later removed [2026-09-17] once its Run 7 entry was found to have a stray, uncorrected error and the individual `run-NN.md` files plus `evals/runs/README.md` had become the more reliable source.)

## [2026-09-15] — Unverifiable does not disqualify a commit from the pass count
**Decision:** For a run's "Passed every criteria: X of N" summary line, a commit counts toward X as long as none of its criteria are marked Fail. A criterion marked Unverifiable does not disqualify it.

**Why:** Unverifiable usually means either the criterion doesn't apply to that commit (e.g. criterion 5's fallback check, when no fallback exists in that commit) or the model correctly followed the skill's rule to flag rather than guess against an inaccessible repo — neither is a fault in the response. Disqualifying on Unverifiable would make it nearly impossible for any commit in this test set to ever count, since almost every commit hits Unverifiable on criterion 3, 5, or 6 for reasons unrelated to response quality. run-08.md already used this convention ("4 of 5," where commits 1, 2, 4, 8 count despite criterion 3 and 5 being Unverifiable, and only commit 12 is excluded for its actual Fails), but run-06/grading.md's "0 of 20" summary didn't apply it — the "1, 4, 8, 19" group has zero Fails and should have counted.

**Status:** Applied retroactively: run-06/grading.md corrected to "4 of 20." Logged in CHANGELOG.md and evals/findings.md.

## [2026-09-15] — Ambiguous feature-vs-portfolio commits default to skip
**Decision:** When a commit description could mean either the book-recommendation feature itself or its portfolio/project-level presence, and nothing in the wording favors one reading over the other, default to skip.

**Why:** Run 8 wrote a release note for commit 12 (6fce484, "Take Book Recommendations project offline"), repeating the exact misclassification Run 4 made and Run 7 avoided — with no rule change in between. Rule 10's worked example names this ambiguity but only says to "pick the reading better supported by the wording," with no tiebreak for the case where the wording doesn't favor either reading, which is why this same commit has flipped between write and skip across runs (write in Run 1, wrongly write in Run 4, no answer in Run 6, correctly skip in Run 7, wrongly write in Run 8). Skip is the safer default here since it matches the existing posture that portfolio/eval/project-meta changes are skipped regardless of visibility (2026-09-14 9:05 PM decision below), and a missed release note is a smaller error than fabricating one for a change a skill user never sees.

**Status:** Logged in evals/findings.md (Run 8) and CHANGELOG.md. Not yet applied to SKILL.md rule 10 or evals/rubric.md — pending.

## [2026-09-15] — Run 7 confirmed Run 6 was a batching artifact; skill hardened anyway against isolated-call ambiguity
**Decision:** Ran the same 20 commits batched in one pass (Run 7) to resolve the open item from the Run 6 entry below. It passed 7/7 cleanly, confirming Run 6's regressions were produced by running each commit as an isolated single-commit call, not by a wording gap that only shows up under batching. Despite that, edited SKILL.md rules 3 and 4 and added rule 10, and added evals/rubric.md Version 2 criterion 8, because the underlying behavior — stopping to ask the user instead of deciding, and writing per-commit essays instead of "no entry" for skips — isn't something a caller can be relied on to avoid by always batching requests.

**Why:** Case-10 and case-12 (evals/runs/run-06/) show the model generalizing rule 3's "flag the discrepancy back to the user" language, written for a verified-commit-vs-description conflict, to any ambiguous description with no conflict at all. Case-03 shows a correctly-skipped commit still getting a paragraph re-litigating the call. Both are things a single, non-batched request could trigger regardless of how the prompt is phrased. Separately, no rule ever told the model to decide rather than ask — that check existed only as Version 1 rubric criterion 1, retired at Run 4 without a matching SKILL.md rule ever being written to replace it.

**Status:** Applied to SKILL.md rules 3, 4, and new rule 10; evals/rubric.md Version 2 criterion 8 added to match. Logged in CHANGELOG.md. Not yet committed to git. Open item: re-run the isolated single-commit format (as Run 6 did) against the updated skill to confirm the fix actually closes the gap, rather than assuming from the rule wording alone.

## [2026-09-15] — Run 6 findings logged; no skill or rubric fix decided yet, format change suspected
**Decision:** Logged Run 6's regressions (no-answer responses, verbose skip write-ups standing in for "no entry," present-tense hedging) in findings.md without editing SKILL.md or evals/rubric.md yet.

**Why:** Run 6 was run as 20 separate single-commit cases instead of one batched 20-commit conversation like Run 5. Run 5, batched, passed cleanly; Run 6, run per-commit, regressed on behavior the current rubric doesn't cleanly score (hedging, asking for input instead of deciding, verbosity, tense drift in non-release-note prose). It isn't yet clear whether this is a real skill-wording gap or an artifact of running each commit in isolation with no other commit's context to calibrate against. Editing the skill now risks fixing a test-harness artifact instead of an actual behavior problem.

**Status:** Logged in CHANGELOG.md and evals/findings.md under Run 6. Open item: re-run the same 20 commits batched, as Run 5 was, to see if the regression reproduces before deciding on a skill or rubric fix.

## [2026-09-15] — Run 5 confirmed the Run 4 fixes hold; skill and rubric left unchanged
**Decision:** Made no further edits to SKILL.md or evals/rubric.md after Run 5 scored 7/7 on the Version 2 criteria — the repo-check stop condition and the portfolio/eval/meta skip rule added after Run 4 both held on a fresh session re-run of the same 20 test-case commits.

**Why:** Run 4 had scored well on its own rubric but still turned out to need a rule fix afterward (the stop-condition gap wasn't caught by grading). Run 5 exists to re-test the same commits against the tightened rules before treating the skill as stable, rather than trusting Run 4's score alone.

**Status:** Logged in CHANGELOG.md under Run 5. evals/runs/run-05.md and run-05-output.md hold the grading and output.

## [2026-09-14 9:05 PM] — Portfolio-site and eval/project-meta commits are skipped regardless of visibility
**Decision:** Reinstated a project-scope skip condition: a commit is skipped if it's a portfolio-site, eval, or project-meta change even when its effect is visible to someone — a portfolio visitor is not a user of the book-recommendation skill. Added a worked "meta example" alongside the existing "technical example" so the rule isn't just a stated principle.

**Why:** The 2026-09-12 6:06 PM decision below dropped an earlier project-scope rule as redundant with the general visibility check, assuming portfolio/eval commits would always fail that check on their own. Run 4 disproved this — "Take Book Recommendations project offline," "Removed agentic AI section from portfolio site," and "Move run-01 results into docs so it publishes to the site" all passed the visibility check and were wrongly written up as release notes for the book-recommendation skill.

**Status:** Applied to SKILL.md rule 4 and evals/rubric.md criterion 3 (commits a04b71b, 2b85564, bc6eef7, 60a077a). Logged in CHANGELOG.md. Open item: the worked example only covers the portfolio-page case; "took the whole skill offline" and "published eval results to the site" are still ambiguous and not yet covered by an example.

## [2026-09-14 8:49 PM] — Repo-check rule needed a stop condition, not just permission to check
**Decision:** Tightened skill rule 3 so it only checks a repo already known in context, never searches the filesystem or guesses at repo locations, and marks the commit unverifiable if not immediately accessible. Matching rubric criterion 6 now grades for this stop condition explicitly, not just conflict-flagging.

**Why:** Run 4 scored 7/7 on the existing rubric, but the underlying behavior was wrong: once repo-checking was allowed (Run 4's earlier repo-check rule), the model kept trying to locate a repo instead of falling back to unverifiable when none was accessible — the test-case hashes are synthetic and don't resolve to a real repo. The rubric's "Unverifiable" outcome already existed for this case, but nothing in the skill told the model to stop and land there.

**Status:** Applied to SKILL.md rule 3 and evals/rubric.md criterion 6 (commits a04b71b, 2b85564, bc6eef7). Logged in CHANGELOG.md.

## [2026-09-14 <6:35 PM>] — Commit #1's input wording was fixed after landing on it by mistake meant for #19
**Decision:** Restored evals/cases/release-notes-20.md commit #1's description to describe its own real change (specifying the exact heading to look for in the already-read file) instead of the #19-shaped wording it had picked up.

**Why:** The 2:50 PM edit intended for commits #4 and #19 landed on #1 instead of #19 in its first pass; #19 was then separately and correctly rewritten in the next commit to nearly the same content, so #1 and #19 ended up as near-duplicates in the current release-notes-20.md. Caught before Run 4 used the file.

**Status:** Applied to evals/cases/release-notes-20.md; logged in CHANGELOG.md under Run 4. Checked evals/gold/release-notes.md, evals/cases/raw-commits.md, and evals/runs/run-01 through run-03 output files for the same problem — none needed changes.

## [2026-09-14 6:06 PM] — Version 1 rubric must stay exactly as graded, not get retroactive fixes
**Decision:** Restored evals/rubric.md's "Version 1 (Runs 1-3)" section to the original wording actually used to grade those runs — reverted criterion 4 to "Are developer-facing commits correctly skipped (no note at all)?" (no example) and removed criterion 7 (mechanism/outcome), since neither existed in that form when Runs 1-3 were graded.

**Why:** After splitting the rubric into Version 1/Version 2, the Version 1 section had been overwritten with Version 2's improved wording (skip-rule example, mechanism/outcome criterion). That makes old findings citing criterion numbers (e.g. "Criterion 4 failed") misleading — a reader would assume the improved criteria applied at grading time when they didn't.

**Status:** Applied to evals/rubric.md.

## [2026-09-14 <2:50 PM>] — Fixing the skill won't add missing detail
**Decision:** I decided to change the input commit list, not the skill rules.

**Why:** I had already tried changing the skill rules between versions 1, 2, and 3 with imprecise wording resulting. I talked to Claude and realized because I was not asking the skill to check actual commits (only using user input), the skill lacked context Git normally gave it, so it needed better input to run on specifically for commits 4 and 19. 

**Status:** Applied edits to release-notes-20.md for commits 4 and 19; gold file reconciled 2026-09-14 6:06 PM.

## [2026-09-14 2:28 PM] — Skip rule depends on visible effect, not how technical a commit sounds
**Decision:** Commit 19 (a pre-run check against the already-read-books file) should not have been skipped, even though its description sounds like an internal implementation detail — it changes which books the recommender shows the user.

**Why:** Run 3 findings showed this commit was wrongly marked skip. The skip rule is about whether the *effect* is visible to the user, not about whether the commit's own description uses technical-sounding language.

**Status:** Logged in evals/findings.md (Run 3). Logged to skill and rubric.

## [2026-09-14 2:28 PM] — A technically-accurate release note that omits the specific outcome still fails
**Decision:** A release note counts as a failure if it's vaguely accurate but drops the specific mechanism or outcome of the commit (for example, describing "adjusted when it asked" without saying what default was applied), not only if it's factually wrong.

**Why:** Three commits in Run 3 went through two rounds of revision and were still judged too imprecise compared to the actual commit — the model kept generalizing away the specific default or check that made the note useful.

**Status:** Logged in evals/findings.md (Run 3). Logged in skill. Logged in rubric.

## [2026-09-14 1:31 PM] — Broadened "don't check other repos" to "don't check any repo"
**Decision:** Rewrote the rule from "Do not check other repos for the release notes commit hashes; use only the raw commits the user gives you" to "Do not check any repo for commits before generating release notes. Use only the input the user gives you to generate release notes."

**Why:** Run 2 showed the model still tried to look up the commits itself even under the narrower wording from Run 1.

**Status:** Applied to SKILL.md; logged in CHANGELOG.md under Run 2.

## [2026-09-14 12:06 PM] — Changelog entries must quote the exact old/new rule text and cite a commit hash
**Decision:** Rewrote CHANGELOG.md so each entry is grouped under the commit hash that made the change and states the literal before/after rule wording, instead of being grouped loosely by run number with paraphrased summaries.

**Why:** A paraphrased changelog entry can't be checked against what the rule actually said before and after; quoting the exact text makes each fix verifiable.

**Status:** Applied to CHANGELOG.md; used as the format for all later changelog entries.

## [2026-09-14 11:54 AM] — Skill does one job (release notes); changelog is tracked by hand, separately
**Decision:** Removed the "Rules for changelog" section that had been added to SKILL.md and reverted its description to mention only release notes. The skill generates release notes only; changelog entries documenting the skill's own edits are written directly into CHANGELOG.md, not generated by the skill.

**Why:** Loading both release-note rules and changelog rules into one skill made it unclear which rule set a given run was actually following, and complicated grading. Splitting them keeps the skill's job — and its evaluation — to one thing.

**Status:** Applied to SKILL.md and CHANGELOG.md.

## [2026-09-14 11:31 AM] — Skipped commits get no entry at all, not a SKIP line (reverses 2026-09-12 4:35 PM decision below)
**Decision:** Changed the skill's skip rule and format rule so a skipped commit produces no output at all, removing the earlier "SKIP; <reason>" line requirement.

**Why:** Run 1 grading showed the rubric's actual requirement was "no note at all" for developer-facing commits. The SKILL.md skip rule and the rubric contradicted each other, and the model followed the skill's SKIP-line instruction correctly but still failed the rubric criterion. The SKIP-line was useful while hand-writing gold answers but is wrong for what the shipped skill should output.

**Status:** Applied to SKILL.md. Supersedes the 2026-09-12 4:35 PM decision below (kept for history).

## [2026-09-14 11:31 AM] — Added rules for tense, internal file names, and checking other repos
**Decision:** Added three new SKILL.md rules: write all release notes in past tense only; never use internal file names (skill, rubric, eval, findings) in release notes; don't check other repos to verify commit hashes, use only what the user provides.

**Why:** Run 1 found the model mixed tenses, referenced internal file names, and stopped mid-run to ask about looking up commits elsewhere — none of these were forbidden by the skill at the time.

**Status:** Applied to SKILL.md.

## [2026-09-12 6:06 PM] — Project-scope skip rule dropped as redundant; skip conditions consolidated
**Decision:** A rule limiting release notes to book-recommendations-assistant commits only (added 5:26 PM) was removed about 18 minutes later; the "skip if a user of the book recommender would never notice" condition and the "always write a SKIP line" requirement were merged back into one combined skip rule, and the ordering rule was generalized from "book-recs commits" to "input commits."

**Why:** The project-scope rule was redundant — a commit from the portfolio site or eval project is already something a book-recommender user would never notice, so the general skip condition already covered it.

**Status:** Applied to SKILL.md across three edits (4bff7ca added the scope rule, 46f8733 removed it and merged skip conditions, b2810f4 restored the "would never notice" wording alongside the SKIP-line rule).

## [2026-09-12 5:25 PM] — Standardized how commits are cited in release notes
**Decision:** Reformatted commit citations from "#4 5da846a - sentence" to "Commit 4 (5da846a): sentence."

**Why:** Needed one consistent citation format before generating and grading multiple release-note runs.

**Status:** Applied to evals/gold/release-notes.md; encoded the next day as the "Format answers like this" rule in SKILL.md.

## [2026-09-12 5:08 PM] — Silent defaults must be stated explicitly
**Decision:** Added a skill rule: "When a skill silently defaults to something, say that a default was applied."

**Why:** A default applied without being called out is indistinguishable from a bug or a lucky guess — for example, the recommender falling back to the contemporary genre when no genre was given needs to say so, not just act on it.

**Status:** Applied to SKILL.md from its first draft; carried through all later revisions and reinforced by the 2026-09-14 2:28 PM decision above on commit 4.

## [2026-09-12 4:43 PM] — Skip developer-facing commits from release notes
**Decision:** Commits that only touch internal files (eval templates, example lists, moved-but-not-changed content) are excluded from
release notes entirely — not given a note explaining the skip, just absent.

**Why:** While hand-writing gold answers, two commits (adding example entries to already-read-example.md, moving a rubric into the evals folder) had no effect a user of the skill would ever see. Writing a release note for either would describe a change that doesn't exist from the reader's side.

**Status:** Applied in gold answers for cases #18 and #20. Written into SKILL.md as the skip rule.

## [2026-09-12 4:35 PM] — Commits that produce no release notes are "skip"
**Decision:** For a commit that should produce no release note, the correct gold answer is SKIP plus a one-line reason, not omitting the line. 

**Why:** This matters for scoring: an absent line and a "verified-no-note-needed" line would otherwise look identical to a grader.

**Status:** Corrected evals/gold/release-notes.md to include why skipping commits.

## [2026-09-12 4:20 PM] — Release notes speak to the user, not to a developer
**Decision:** Release notes voice should tell user what changed and why, not give technical details such as skill edits.

**Why:** These are user-facing, not developer-facing.

**Status:** Rewrote release-notes.md to correct voice across all entries.
