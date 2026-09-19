# Findings
Below are the reasons why ouputs failed, grouped by what numbers matched each result.

## Trigger runs 1 and 2 [2026-09-18]
Trigger test, 20 prompts (`evals/cases/trigger-set-20.md`), run before and after rewording the release-notes `description:` (`evals/runs/trigger-run-01.md`, `evals/runs/trigger-run-02.md`). doc-review (5 prompts) and the "neither" group (5 prompts) matched expectations in run 1 and were not re-run.

Prompts 4 ("fix my commits") and 6 ("apply review of these commits") did not trigger release-notes in either run. In run 1, prompt 4 got a clarifying question and prompt 6 fired the built-in code-review skill. In run 2, prompt 4 behaved the same and prompt 6 fired nothing (the agent said it couldn't review commits that don't exist in the repo).

**Expectation:** both prompts were written on purpose as indirect phrasings that should trigger release-notes, so both count as misses. The release-notes subtotal is 8 of 10 in both runs, and the 20-prompt total is 18 of 20 in both.

**Cause: the spec never addressed indirect phrasings** (the first of the three causes). The description only covers explicit requests. Neither prompt says "release notes" or "notes", and the eight prompts that do passed in both runs. The reword added more explicit verbs ("create, write, generate, add"), which is why it changed nothing: it targeted phrasings that were already passing. Prompt 6 also collides with the built-in code-review skill in run 1, a competing description this project doesn't control.

Under the Phase 3 approach, a "spec never addressed this" cause is one where the wording gets edited, so a second description reword aimed at these indirect phrasings is the plan-consistent next step. It carries a real risk of false triggers on other commit-related requests, and the 5-prompt "neither" group is too small to detect that. Whether to attempt it is open, tracked in `decisions.md` (2026-09-18).

**Caveats on the comparison:**
- `trigger-run-01.md` says the prompts were run without the accompanying commits or docs. `trigger-run-02.md` says the commits and docs were included. If both are accurate, the before/after differs in two ways at once (description and input), not just the description.
- Each prompt was run once, so a one- or two-prompt difference is within run-to-run noise.

## v3 variance [2026-09-17]
5 repetitions of all 20 cases (`scripts/run-eval.py --repeats 5`, `evals/runs/v3/rep-01` through `rep-05`), graded in `evals/runs/v3-stats.csv`. **9 of 20 cases pass every criterion in all 5 reps.**

Commit 18 (b50af03) fails all 5 reps: wrote a release note instead of skipping in 4 of them, and hedged (asked for more detail) in all 5. Commit 6 (1e3c29b) fails 4 of 5 — the same skip-rule miss named in the `v3` entry below. Both are known-unstable cases under the isolated-call format.

Eight more commits that are otherwise correctly skipped in every rep (7, 10, 11, 12, 13, 14, 16, 20) fail at least one rep anyway, each by attaching an unauthorized per-commit reason to an otherwise bare skip line — the same rule 4 violation the `v3` entry below documents for commit 20. No SKILL.md or rubric edit made from this finding yet.

## v3 [2026-09-17]
Single non-repeat scripted run (`scripts/run-eval.py`), graded one row per case in `evals/runs/v3.md` per the grading rule added to `evals/rubric.md`. 15 of 20 passed every criterion.

Commit 6 (1e3c29b) failed criterion 3: wrote a release note for a fix to the skill's own "what it does" description, which is internal/developer-facing — SKILL.md's self-description is never seen by a user of the recommender.

Commits 10 (ec87a17), 11 (1ac826a), 18 (b50af03), and 20 (f244f58) failed criterion 8: each added a per-commit reason clause for its skip decision, which rule 4 explicitly bars ("A single aggregate line listing skipped commit numbers is fine; per-commit justification is not"), and commit 18 additionally asked to reconsider. This is the same isolated-call decide-then-hedge pattern Run 10 identified below — a fresh data point for an already-identified failure mode, not a new spec gap.

## Run 8/9 completed to full 20-case grading [2026-09-17]
`run-08.md` and `run-09.md` are graded one row per case, all 20, per the write/skip ground truth in decisions.md: `run-08.md` is **19 of 20** (only commit 12's misclassification fails), `run-09.md` is **20 of 20**.

## Run 10 [2026-09-15]
Ran evals/cases/release-notes-20.md through scripts/run-eval.py as 20 isolated single-commit API calls, 5 repetitions (evals/runs/run-10/rep-01 through rep-05), to close the open item from the "Run 7 confirmed..." decision (decisions.md, 2026-09-15): confirm whether the rule 10 default-to-skip fix actually holds under the isolated-call format that caused Run 6's regressions, rather than assuming from the rule text alone. Per-case pass rate is in evals/runs/run-10-stats.csv.

### The decide-then-hedge pattern
16 of 20 commits passed all 5 reps. Commits 2 (2d10267, failed 4 of 5 reps) and 10 (ec87a17, failed 1 of 5) show a failure mode distinct from Run 6's outright refusal to decide: the response does write a note or skip, satisfying rule 10 on its face, but then appends a hedging sentence asking for the diff or confirmation — e.g. commit 2, rep 1: "The message says only that the line's format was fixed, so the specific formatting change ... isn't captured here; if you can share the diff, I'll sharpen the entry." That trailing request still trips criterion 8 (mechanical-results.csv's clarify-pattern check matches "share the diff").

### A real skip-rule miss, not just hedging
Commit 6 (1e3c29b, failed 3 of 5 reps) wrongly wrote a release note treating a fix to the skill's own "what it does" summary as user-visible, instead of skipping it as an internal/meta change. Commit 18 (b50af03, failed 3 of 5 reps) mixed both patterns: one rep correctly skipped but still asked for clarification, two reps wrongly wrote a note.

### Not yet fixed
No SKILL.md or rubric edit made from these results. See decisions.md 2026-09-15 entry — the working theory is that the isolated single-commit format itself (no other commit's context, no conversation) makes hedging more likely independent of rule wording, so a further rule change is being held until that's confirmed rather than the script's call shape.

## Run 9 [2026-09-15]
Passed all 8 Version 2 criteria (evals/runs/run-09.md). Commit 12 (6fce484) was correctly folded into the aggregate skip line, with no release note and no reconsidering language — confirms the rule 10 default-to-skip clause (commit 512e384) fixed the exact misclassification Run 8 had.

### Rubric tagging gap found while automating grading
While adding scripts/check-mechanical.py, evals/rubric.md's Version 2 criterion 5 ("Is a fallback or default explained when one applies?") was found still tagged "mechanical," but it isn't checked by the script (which only covers criteria 1, 2, 4, 8) and is graded by hand in evals/runs/judgment-grades.csv alongside criteria 3, 6, 7. The a432401 fix that retagged 3, 6, 7 from "mechanical" to "judgment" missed criterion 5. Corrected in evals/rubric.md to "judgment."

## Run 8 [2026-09-15]
Commits 1, 2, 4, 8 passed all Version 2 criteria (evals/runs/run-08.md). Commit 12 (6fce484, "Take Book Recommendations project offline") failed criteria 3 and 8: the response wrote a release note treating it as a book-recommendation feature change, when gold and the 2026-09-14 9:05 PM decision treat this as a portfolio/project-level change to skip. The entry also included a parenthetical weighing both readings ("...leaves some ambiguity about whether this meant discontinuing the feature itself versus removing its portfolio listing; this reads as the former"), which reads as reconsidering the call rather than a single flagged clause, failing criterion 8.

### Not a new wording gap
Rule 10 and the skip rule were unchanged between Run 7 (evals/runs/run-07.md, passed 7/7, correctly skipped commit 12) and this run — same skill, same batched-prompt format, same input. Rule 10's own worked example describes this exact ambiguity ("could mean the portfolio listing was pulled (skip) or the skill itself was taken down (write)") but only tells the model to "pick the reading better supported by the wording," with no tiebreak for when neither reading is more supported than the other. That leaves this specific commit's classification unstable run to run: written in Run 1, wrongly written in Run 4, no answer in Run 6, correctly skipped in Run 7, wrongly written again here. See decisions.md 2026-09-15 entry ("Ambiguous feature-vs-portfolio commits default to skip") for the fix direction.

## Run 6 [2026-09-15]
Run 6 was run as 20 separate single-commit cases (evals/runs/run-06/case-01.md through case-20.md) instead of one batched 20-commit conversation like Run 5. Three failure modes showed up that Run 5 did not have:

### Several commits got no answer at all
Commits 2 (2d10267), 6 (1e3c29b), 10 (ec87a17), 12 (6fce484), and 18 (b50af03) produced neither a release note nor a skip decision — the response stopped and asked the user to supply more detail or pick between readings instead of doing what Runs 1-5 did (make the call from the description given). For example, commit 12 ends with "Tell me which reading is correct (or point me at the repo), and I'll finalize or drop the entry," and commit 10 ends with "Rather than guess, could you either confirm the repo location... or tell me what the skill-language edit changed." The skill's "unverifiable" outcome was meant to mark a release note that can't be confirmed against the repo, not license to stop and ask instead of landing on skip-or-write.

### Skipped commits still resulted in full write-up files, not "no entry"
Nearly every commit correctly identified as skippable (3, 5, 7, 9, 11, 13, 14, 15, 16, 17, 20) still generated a multi-paragraph file restating the skip rule, flagging unverifiability, and inviting the user to override the call — instead of "no entry," which is what the skip rule says and what Run 5 actually did (one line: "Skipped (no visible effect...): 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20"). No single rubric criterion scores this directly, but it's a sharp behavior regression from Run 5.

### Many responses were not in past tense
The release notes themselves (commits 1, 4, 8, 19) stayed in past tense and were fine. The skip explanations and clarifying-question responses were written in present tense throughout — e.g., commit 3: "Editing the changelog is a project-meta change. It doesn't alter..."; commit 16: "Moving run-01 results into docs so it publishes to the site affects..."; commit 7: "'Edited skill formatting' describes a change... Nothing... points to...". The past-tense rule was written with release notes in mind and doesn't obviously cover this new category of skip/clarification prose.

### Likely cause, not yet confirmed
Run 5's single batched pass made a judgment call on every ambiguous commit and flagged only one (commit 18) as uncertain. Running each commit as its own isolated case seems to have pushed the model toward hedging and asking rather than deciding, with no other commit's context to calibrate against. Worth re-running Run 6 batched, the way Run 5 was, before deciding whether this is a skill-wording gap or an artifact of the isolated-case format.

### Root cause identified, skill updated [2026-09-15]
Run 7 (evals/runs/run-07.md) re-ran the same 20 commits batched, as planned, and passed 7/7 — confirming the regression was produced by isolated single-commit calls, not a wording gap that only surfaces under batching. Tracing the two failure modes above to specific rule text:
- The no-answer responses (case-10, case-12 in evals/runs/run-06/) came from rule 3's "flag the discrepancy back to the user rather than guessing" — written for a verified commit disagreeing with its description, but with no scope fence, so the model generalized it to any ambiguous description with no conflict at all.
- The per-commit skip essays (case-03) came from rule 4 barring an entry but never barring prose about the decision.
- Neither failure mode was ever explicitly forbidden anywhere in SKILL.md's history — the closest check, Version 1 rubric criterion 1 ("ran through without interrupting for user feedback"), was retired at Run 4 with no matching skill rule written to replace it.

Fixed by tightening rule 3 (mark unverifiable and still write/skip, don't stop to ask), tightening rule 4 (no per-commit skip essays, aggregate line ok), and adding rule 10 (decide, don't ask, with a worked example on commit 12's ambiguity). Matching evals/rubric.md Version 2 criterion 8 added. See decisions.md 2026-09-15 entry. Not yet re-verified with a new isolated-case run.

Commits 1, 4, 8, and 19 were acceptable. 

### Summary line corrected, [2026-09-15] - Unverifiable doesn't disqualify a commit from the pass count
run-06/grading.md originally read "Passed every criteria: 0 of 20." That was wrong: the "commits 1, 4, 8, 19" group has zero Fails across all 8 criteria (criterion 5 is Unverifiable, everything else Pass), and criterion 5 being Unverifiable there isn't a shortcoming — no fallback applies to any of those four commits, so there's nothing to explain. Run 08.md already established the working convention for this ("4 of 5," where commits 1, 2, 4, 8 count as passing despite criterion 3 and 5 being Unverifiable, and only commit 12's actual Fails exclude it). Applying that same convention to Run 6, the correct total is 4 of 20, not 0. See decisions.md 2026-09-15 entry ("Unverifiable does not disqualify a commit from the pass count").

## Run 4 [2026-09-14]
## For all entries:
- Criterion 3 was originally graded Pass, which was wrong: the response wrote release notes for commits 12 (6fce484, "Take Book Recommendations project offline"), 14 (f21345d, "Removed agentic AI section from portfolio site"), and 16 (8a39d5e, "Move run-01 results into docs so it publishes to the site") — all portfolio-site/project-meta changes that a book-recommendation skill user would never see. The rubric at the time only checked visibility to "the user," and these commits are visible to a portfolio site visitor, so they slipped through grading. This was found afterward, not caught by the original grading pass, and is why the skip rule and rubric criterion 3 were rewritten to skip portfolio/eval/project-meta commits regardless of visibility, with a worked meta example added. run-04.md has since been corrected to Criterion 3: Fail.
- Criterion 6 was marked Unverifiable because this run's own prompt told the model not to check any repo, so no verification was attempted either way. Separately (not from this run's grading), it was later found that the repo-check rule itself had no stop condition — once repo-checking was allowed, the model could keep searching for a repo instead of falling back to unverifiable when none was accessible. That gap was fixed afterward even though nothing in Run 4 exercised or caught it directly.
- The grading summary line originally read "Passed every criteria: 7 of 7," which contradicted its own breakdown (Criterion 6: Unverifiable, and, per the point above, Criterion 3 should have read Fail). After the criteria were corrected, the summary line itself still needed fixing — it briefly read "0 of 8" (Version 2 has 7 criteria, not 8, and the project's convention for a run that doesn't pass everything is the single-letter "O," not a fraction, per run-01.md and run-02.md). Corrected to "O."

Commits 1, 2, 4, 8, and 19 were acceptable.

## Run 3 [2026-09-14]
## For all entries:
- Criterion 4 failed because it removed commit #19 which was still user-facing, not developer-facing.

- Across 2 commits, the language is less precise than the actual commits:
 1. Commit 4 (5da846a)
- V1: It was marked skip in version 1 but it should not have been
- V2 Revised too vaguely: "Clarified that the recommender asked which genre when a user was present to answer."
- V3 revised less vaguely but missing information: "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond"
- It should say: "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."

 Commit 19 (b971722)
 - V1 Original: "The skill now checks the already-read file before running, so it won't proceed without applying exclusion filtering."
- Revised V2: "Commit 19 (b971722): Added a check that ran before the recommender started, so it stopped and told the user if something needed was missing."
- Revised V3: Skipped completely.
- It should say: "Checked the file of already read books before running, so the result won't produce books the user has already read."

Commit 1, 4, 8, 12 were acceptable.

## Run 2 [2026-09-14]
## For all entries:
1. Criterion 1 failed because the prompt did not specify "do not look up the commits." The AI wanted to look up the actual commits for release notes, not use the input I gave it.
2. Criterion 6 was unverifiable since there were no fallbacks or defaults applied.

## Run 1 [2026-09-14]

### Entry 1: Commits 1 and 8
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed and there was no fallback or default mentioned so Criterion 6 was unverifiable. Criterion 4 was unverifiable since this was not a developer-facing commit.

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.

### Entry 2: Commits 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 17, 18, 20
 What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note and no fallback or default mentioned so Criterion 3 passed and Criterion 6 was unverifiable. 
Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results. Criterion 4 did not match the skill: the skill says "skip" and also "Whenever a commit is skipped for any reason, still write a line: SKIP," so results followed the skill and wrote the line but failed the overall skip criterion.

### Entry 3: Commit 12
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed. Criterion 4 was unverifiable since this was not a developer-facing commit. Criterion 5 did not apply (no internal files involved). There was no fallback or default mentioned so Criterion 6 was unverifiable.

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.

### Entry 4: Commit 14
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed. Criterion 4 did not match the skill: the skill says "skip" and also "Whenever a commit is skipped for any reason, still write a line: SKIP," so results followed the skill and wrote the line but failed the overall skip criterion. Criterion 5 did not apply (no internal files involved). There was no fallback or default mentioned so Criterion 6 was unverifiable

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.
