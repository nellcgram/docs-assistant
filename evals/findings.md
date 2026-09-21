# Findings

This file explains why each test run failed, newest first. I gave every failure one of three causes: a gap (the skill never addressed the situation), an ambiguity (the skill addressed it unclearly), or a model limitation (the skill was clear and the model ignored it). I fixed gaps and ambiguities in the skill and logged each fix in `CHANGELOG.md`. I logged model limitations and made no edit. Rule numbers refer to the skill as it stood at the time. On 2026-09-21 the skill was renumbered, and `CHANGELOG.md` explains how.

## CI safety net (2026-09-21)

A GitHub Action re-runs the eval on each push and fails the check below a 0.75 pass rate. To test it, I broke `SKILL.md` on purpose in five ways.

| Change to the skill | Pass rate | Check |
|---|---|---|
| None (correct skill) | 0.95 (19/20) | passed |
| Deleted rules 7 to 10 | 0.80 (16/20) | passed |
| Reversed rule 6 to "present tense" | 0.85 (17/20) | passed |
| Added "ask the user first," left rule 8 ("never ask") in place | 0.85 (17/20) | passed |
| Deleted rule 8, kept "ask the user first" | 0.85 (17/20) | passed |
| Added an explicit override: write no notes, only ask | **0.10 (2/20)** | **failed** |
| Reverted to the correct skill | 0.85 (17/20) | passed |

The override run failed the check at the pass-rate step, not on a crash. Two other early runs also failed because the API credit balance ran out, so I didn't count them.

- **The check catches large regressions but not subtle ones (model limitation).** Four of the five breaks scored 0.80 to 0.85, above the threshold, because the model followed the most specific rule and ignored the bad ones.
- **The `shared/` files back up `SKILL.md` (redundancy, not a defect).** `shared/hard-surfaces.md` already says "Never ask about a commit," and `house-style.md` already bans internal file names. Deleting the skill's own copy therefore changed nothing, and only an override aimed at the shared files got through.
- **The same skill scored differently on two runs (run-to-run noise).** The correct skill scored 0.95, then 0.85 after the revert, with identical files. One case is worth 0.05, so two or three flips is normal. This is why the threshold sits at 0.75 and not 0.90 (see `decisions.md`).
- **The workflow missed shared-file edits (gap, fixed).** It watched only `.claude/skills/`, although the eval also sends `shared/` to the model. It now watches both.

## Hard cases run 1 (2026-09-19): 3 of 10

I scored ten tricky inputs, five per skill, against `shared/hard-surfaces.md` (`evals/runs/hard-cases-run-01.md`). Doc-review scored 1 of 5 and release-notes scored 2 of 5.

- **Neither `SKILL.md` pointed to `hard-surfaces.md` (gap, fixed).** A loaded skill therefore had no instruction to ask for missing input or to say an input was out of scope. This explains most of the eight failures.
- **The skill descriptions don't cover vague or out-of-scope prompts (gap, still open).** No skill loaded for doc-review inputs 2, 4, and 5 or release-notes input 3, so the agent simply did the task.
- **`hard-surfaces.md` had no bullet for a wrong-language document or a wrong skill name (gap, fixed).** I added both.
- **The `house-style.md` reference had no path (ambiguity, fixed).** The agent could not find the file.
- **Release-notes input 4 ("review commits against checklist") went to doc-review (unresolved).** That routing may be reasonable, but I scored it a fail because the response guessed instead of asking.

Each input ran once, so a one-input difference is within noise.

## Trigger runs (2026-09-18): 18 of 20 both times

I ran 20 prompts before and after rewording the release-notes `description:` (`trigger-run-01.md`, `trigger-run-02.md`). Doc-review (5 of 5) and the "neither" group (5 of 5) passed both times.

Prompts 4 ("fix my commits") and 6 ("apply review of these commits") missed both times. This was a gap, because neither prompt says "release notes" and the eight prompts that do say it passed. The reword targeted phrasings that already worked, so it changed nothing. Each prompt ran once.

## Run 11 (2026-09-17): 15 of 20, then 9 of 20 clean across 5 repeats

Run 11 was the first scripted run (one API call per commit). Its 5-repeat variant (`run-11-stats.csv`) found 9 of 20 cases that passed every criterion in all 5 repeats.

- **Eight correct skips fail at least one repeat (model limitation).** Commits 7, 10, 11, 12, 13, 14, 16, and 20 attach a reason to a bare skip, although rule 4 says outright that per-commit justification is not allowed.
- **Commit 6 (1e3c29b) fails 4 of 5 repeats.** The model writes a note for a fix to the skill's own description, which users never see.
- **Commit 18 (b50af03) fails all 5 repeats.** The model writes a note instead of skipping in 4 repeats and hedges in all 5.

I made no edit. My working theory is that one call per commit invites hedging, because each call has no other commit to calibrate against.

## Runs 8 to 10 (2026-09-15)

- **Run 8 scored 19 of 20.** Commit 12 flipped from skip to write with no change to the skill. This was a gap, because rule 10 gave no tiebreak when neither reading was better supported. I fixed it with a default-to-skip clause.
- **Run 9 scored 20 of 20.**
- **Run 10 scored 16 of 20 clean across 5 repeats.** Commits 2 and 10 decide correctly and then add a hedge such as "if you can share the diff, I'll sharpen the entry." Commits 6 and 18 missed as described under Run 11. This was a model limitation, so I made no edit.
- **I fixed a rubric tag.** Criterion 5 was tagged "mechanical" although a person grades it, so it is now "judgment."

## Run 6 (2026-09-15): 4 of 20

Run 6 sent one call per commit instead of one batch. It produced three new failures (`evals/runs/run-06/`).

- **Five commits got no answer (ambiguity).** For commits 2, 6, 10, 12, and 18, the response asked the user to pick a reading. Rule 3's "flag the discrepancy" was written for verified conflicts, and the model stretched it to any ambiguous commit.
- **Nearly every skip came with a paragraph defending it (ambiguity).** Rule 4 said "no entry" but never barred writing about the decision.
- **Prose around skips used the present tense (gap).** The tense rule covered notes only.

Run 7 (batched again) scored 20 of 20, so the call format caused the regression. I fixed the wording anyway.

## Run 5 (2026-09-14): 19 of 20

Commit 18 hedged ("I'm not confident; let me know") instead of deciding. This was a gap, because no rule said to decide instead of ask. I added rule 10.

## Run 4 (2026-09-14): 17 of 20

- **Portfolio and project-meta commits got notes (gap).** Commits 12, 14, and 16 changed the portfolio or the project, but the skip rule only checked visibility to "the user." My first grading missed this, and regrading caught it.
- **The repo-check rule had no stop condition (gap).** The model could keep hunting for a repo. Run 4 didn't trigger this, but I found it afterward.

## Runs 1 to 3 (2026-09-14)

- **Run 1 scored 0 of 20.** Nothing forbade checking other repos, so the model tried to verify hashes elsewhere (gap). Nothing required past tense or barred internal file names (gap). The skill also said both "skip" and "always write a SKIP line," so the model followed the second rule while the rubric wanted no note (ambiguity).
- **Run 2 also scored 0 of 20.** The model still looked commits up, because the rule only said "don't check other repos" (ambiguity).
- **Run 3 also scored 0 of 20.** The model skipped commit 19 although users would see its effect, because the skill had no example showing that technical-sounding commits can matter (gap). Notes for commits 4 and 19 stayed vague through two revisions, so the skill now says an accurate but vague note fails (ambiguity).
