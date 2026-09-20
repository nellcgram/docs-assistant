# Findings

Why each run failed, newest first. Every failure gets one of three causes: the spec never addressed the situation, the spec addressed it unclearly, or the spec was clear and the model didn't follow it. The first two get a spec edit (logged in `CHANGELOG.md`). The third gets logged and nothing else.

## Hard cases run 1 (2026-09-19): 3 of 10

Ten tricky inputs, five per skill, scored against `shared/hard-surfaces.md` (`evals/runs/hard-cases-01.md`). Doc-review scored 1 of 5 and release-notes 2 of 5.

- **Spec gap: the skills never point to `hard-surfaces.md`.** Neither SKILL.md mentions the file, so a skill that loads has no instruction to ask for missing input or to say an input is out of scope. This explains most of the eight failures.
- **Spec gap: the descriptions don't cover vague or out-of-scope prompts.** No skill loaded for doc-review inputs 2, 4, and 5 or for release-notes input 3, so the agent just did the task.
- **Spec gap: `hard-surfaces.md` had no bullet for two cases the plan names.** It said nothing about a wrong-language document (doc-review input 4) or a wrong skill named (release-notes input 2). I added both bullets on 2026-09-19 (`CHANGELOG.md`).
- **Spec ambiguity: the `house-style.md` reference has no path.** Release-notes rule 11 and doc-review rule 2 name the file, which lives in `shared/`. On release-notes input 1 the agent couldn't find it.
- **Unresolved routing question.** Release-notes input 4 ("review commits against checklist") went to doc-review. The prompt does ask for a checklist review, so this may be reasonable routing. I scored it as a fail because the response guessed instead of asking.

Each input ran once, so a one-input difference is within noise. The first and fourth items are fixed in both SKILL.md files as of 2026-09-19 (`CHANGELOG.md`). The description gap remains open.

## Trigger runs 1 and 2 (2026-09-18): 18 of 20 both times

Twenty prompts, run before and after rewording the release-notes `description:` (`evals/runs/trigger-run-01.md`, `evals/runs/trigger-run-02.md`). Both runs included the commits or docs with every prompt. Only the 10 release-notes prompts were re-run, since only that description changed. Doc-review (5 of 5) and the "neither" group (5 of 5) passed in run 1.

Prompts 4 ("fix my commits") and 6 ("apply review of these commits") missed in both runs. In run 1, prompt 4 got a clarifying question and prompt 6 fired the built-in code-review skill. In run 2, prompt 4 behaved the same and prompt 6 fired nothing.

- **Cause: spec gap.** Neither prompt says "release notes", and the eight prompts that do passed in both runs. The reword added more explicit verbs, so it targeted phrasings that already passed and changed nothing.
- **Caveat:** each prompt ran once, so a one- or two-prompt difference is within noise.

## v3 and v3 variance (2026-09-17): 15 of 20, and 9 of 20 clean in 5 reps

The first scripted run scored 15 of 20 (`evals/runs/v3.md`). The 5-repeat run (`evals/runs/v3-stats.csv`) found 9 of 20 cases passing every criterion in all 5 reps.

- **Cause: model limitation, clear rule not followed.** Eight otherwise-correct skips (commits 7, 10, 11, 12, 13, 14, 16, 20) fail at least one rep by attaching a reason to a bare skip. Rule 4 says outright that "per-commit justification is not" allowed. Commits 10, 11, 18, and 20 failed this way in the single run too.
- **Commit 6 (1e3c29b) fails 4 of 5 reps.** It wrote a note for a fix to the skill's own "what it does" text. Users of the recommender never see that text, so rule 4 says to skip it.
- **Commit 18 (b50af03) fails all 5 reps.** It wrote a note instead of skipping in 4, and it hedged in all 5.

No SKILL.md or rubric edit followed. The working theory is that the one-call-per-commit format itself invites hedging, because each call has no other commit to calibrate against.

## Runs 8, 9, and 10 (2026-09-15)

- **Run 8: 19 of 20.** Commit 12 (6fce484, "Take Book Recommendations project offline") failed criteria 3 and 8. The skill and input hadn't changed since Run 7, which skipped it correctly. **Cause: spec gap.** Rule 10 told the model to pick the better-supported reading but gave no tiebreak when neither reading was better supported. The fix was the default-to-skip clause.
- **Run 9: 20 of 20.** The clause fixed commit 12.
- **Run 10: 16 of 20 clean in all 5 reps** (`evals/runs/run-10-stats.csv`). Commits 2 and 10 write a note or skip correctly, then add a hedge like "if you can share the diff, I'll sharpen the entry." Commits 6 and 18 made the same skip-rule misses described above. **Cause: model limitation.** No edit followed.
- **Rubric tagging gap.** While building `scripts/check-mechanical.py`, I found criterion 5 still tagged "mechanical" even though a person grades it. It is now tagged "judgment."

## Run 6 (2026-09-15): 4 of 20

Run 6 ran as 20 separate single-commit cases instead of one batched conversation like Run 5. It showed three failures Run 5 didn't have (`evals/runs/run-06/`).

- **No answer at all** for commits 2, 6, 10, 12, and 18. The response asked the user to pick a reading or supply detail. **Cause: spec ambiguity.** Rule 3's "flag the discrepancy" language was written for a verified commit that disagrees with its description, and the model stretched it to any ambiguous description.
- **A paragraph for nearly every skip** instead of "no entry." **Cause: spec ambiguity.** Rule 4 said "do not add an entry" but never barred writing about the decision.
- **Present-tense skip and clarification prose.** The tense rule covered release notes only.

Run 7 (batched again) scored 20 of 20, so the format caused the regression. I fixed the wording anyway (`CHANGELOG.md`, 2026-09-15).

## Run 5 (2026-09-14): 19 of 20

Commit 18 hedged ("I'm not confident; let me know if you want it included") instead of deciding. That fails criterion 8, and every other commit passed. **Cause: spec gap.** No rule told the model to decide instead of ask, and rule 10 was added afterward.

## Run 4 (2026-09-14): 17 of 20

- **Cause: spec gap.** Commits 12, 14, and 16 were portfolio-site or project-meta changes but got release notes, because the skip rule only checked visibility to "the user." Run 4's first grading missed this and marked criterion 3 as a pass. Regrading corrected it.
- **Cause: spec gap.** The repo-check rule had no stop condition, so the model could keep hunting for a repo when none was accessible. Run 4 didn't trigger this, because its prompt told the model not to check any repo. I found it afterward.

## Run 3 (2026-09-14)

- **Cause: spec gap.** Commit 19 was skipped although it was user-facing. The skill had no example showing that technical-sounding commits can still change what users see.
- **Cause: spec ambiguity.** The notes for commits 4 and 19 stayed vague through two revisions. A note that says "adjusted when the recommender asked" without naming the default it applied is accurate but useless. The skill now says a vague note fails.

## Run 2 (2026-09-14)

**Cause: spec ambiguity.** The model still tried to look up the commits itself. The rule only said "don't check other repos," which left room to check the same repo.

## Run 1 (2026-09-14): 0 of 20

- **Cause: spec gap.** Nothing forbade checking other repos, so the model tried to verify hashes elsewhere and I had to stop it.
- **Cause: spec gap.** Nothing required past tense or barred internal filenames, so notes drifted between tenses and named files like SKILL.md.
- **Cause: spec ambiguity.** The skill said both "skip" and "always write a SKIP line," so it followed the second while the rubric wanted no note at all.
