# Case Study: Building and Evaluating Two Claude Code Skills

This was my first completed project to teach myself how to build an agentic AI skill, rubric, and eval harness.

**Summary:** I wrote two Claude Code skills, one that turns git commits into release notes and one that reviews a document against a checklist. I built an evaluation around the first: 20 real commits, a hand-written answer key, a graded rubric, scripted runs, and a GitHub Action that fails on regressions. The scores moved a lot, but what I learned from the failures is worth more than any score. The test commits come from a separate book-recommendation project of mine, and every number below links to the file behind it.

## Four things I found

**1. My first 0 of 20 was my own documents disagreeing.** The rubric required past tense and no internal file names. The skill never said either, and it also told the model to write a SKIP line where the rubric wanted no note at all. Most of the climb to 19 of 20 was making the spec and the rubric agree, so read that jump as "I finished writing the spec," not "the model improved." I made the same kind of mistake twice more, between `hard-surfaces.md` and rule 10, and between `house-style.md` rule 3 and skill rules 4 and 8. I caught both by reading, before a test showed them.

**2. A passing test gate can be nearly blind, because of redundancy.** The GitHub Action (since removed) failed a push below a 0.75 pass rate. To test it, I broke the skill five ways on purpose. Four of the breaks passed at 0.80 to 0.85, including deleting four rules and reversing the tense rule, because the shared files repeat the key rules and the model followed those. Only an explicit override scored 0.10 and failed. The identical correct skill scored 0.95 and then 0.85, since one case is worth 0.05, so a stricter threshold would have failed a good skill. Duplicated instructions make a prompt robust and its tests insensitive.

**3. How I called the skill changed the score more than most rule edits.** The same skill scored 20 of 20 when all 20 commits went in one request (Run 7) and 4 of 20 when each commit was its own call (Run 6). With no other commit to calibrate against, the model wrote notes for changes no user sees and attached reasons to skips the skill forbids. A score measures the skill and the way it is called together.

**4. The skill is right more often than it is consistent, and my own summaries were wrong.** Across 5 repeats of 20 cases, only 9 cases passed every time. The misses were mostly correct decisions with extra explanation attached: eight correct skips failed at least once that way. Separately, grading a whole run as one verdict hid failures. Reconciling the script's grades with mine corrected four run summaries (Runs 5, 6, 8, and 9), including Run 6, which went from "0 of 20" to 4 of 20. That is why every run is now graded one row per case.

## What the numbers can and can't show

| Phase | What I measured | Result | What it can't show |
|---|---|---|---|
| 2 | First version of `release-notes` | 0 of 20 | Model quality: the rubric asked for rules the skill never had (finding 1) |
| 3 | After diagnosing and fixing the spec | 19 of 20 | Generalization: I tuned on these same 20 commits |
| 4 | First scripted run (one API call per commit) | 15 of 20 | Skill quality alone: the call format changed too (finding 3) |
| 6 | Cases that pass in all 5 repeats | 9 of 20 | Which failures matter: most are extra explanation on a correct answer |
| 7 | Whether the right skill fires (before and after a reword) | 18 of 20, then 18 of 20 | Anything about vague prompts: I ran each prompt once |
| 7 | Handling of missing, unclear, and out-of-scope input | 3 of 10 | Precision: ten inputs, so one flipped verdict is 10 points |
| 8 | CI check on a deliberately broken skill | failed at 0.10, passed at 0.85 once fixed | Subtle regressions (finding 2) |

Every score above comes from the same 20 commits I tuned the skill against, graded by me alone. They show that the method works and how the skill behaved on those cases. They do not show that it works on commits it has never seen. A separate set of commits the skill was never tuned on would show that, and I did not build one (see [`decisions.md`](decisions.md)).

[`evals/runs/README.md`](evals/runs/README.md) links every number to the file behind it, and [`README.md`](README.md) explains how to re-run any of it.

## First number (Phase 2): 0 of 20

Before writing the skill, I hand-wrote the answer key explaining which of the 20 commits deserve a note and what each note should say ([`evals/gold/release-notes.md`](evals/gold/release-notes.md)). I then ran the first version of the skill ([`.claude/skills/release-notes/SKILL.md`](.claude/skills/release-notes/SKILL.md)) against the 20 commit descriptions ([`evals/cases/release-notes-20.md`](evals/cases/release-notes-20.md)) and graded each case by hand against a 6-criterion rubric ([`evals/rubric.md`](evals/rubric.md), Version 1). Result, in [`evals/runs/run-01.md`](evals/runs/run-01.md): **0 of 20 cases passed every criterion.**

The skill had no rule against checking other repos, so it stopped to ask about them. It had no tense requirement, so notes switched between past and present. It had no rule against naming internal files like `SKILL.md`.

## Diagnosis and second number (Phase 3): 0 of 20 to 19 of 20

I traced every failure to one of four causes in [`evals/findings.md`](evals/findings.md): a **gap** (the skill never addressed the situation), an **ambiguity** (it addressed it unclearly), a **model limitation** (the skill was clear and the model ignored it), or a **tool or product problem** (the way the skill was run or set up caused it). Run 1's failures were almost all gaps, so each became a rule, and [`CHANGELOG.md`](CHANGELOG.md) logs the old and new wording. For example, Run 4 still wrote notes for portfolio-site and eval commits:

> Old: *"Skip a commit if the effect is not visible to the user."*
> New: *"Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone. A portfolio visitor is not a user of the book-recommendation skill."*

After several more rounds of fixes, Run 5 ([`evals/runs/run-05.md`](evals/runs/run-05.md)) scored **19 of 20**, and later runs reached 20 of 20 ([`evals/runs/README.md`](evals/runs/README.md) lists every run). Run 5, not the regressed Run 6, is the second number because Run 6 changed the call format as well as the skill ([`decisions.md`](decisions.md)).

## Automating the run (Phase 4): 15 of 20

Once the skill held up under manual testing, I automated the harness. [`scripts/run-eval.py`](scripts/run-eval.py) reads the skill and the 20 cases and calls the API once per commit, where before I pasted prompts into a fresh session by hand. A script ran the cases, but grading was still by hand at this point. The scripted run (Run 11, [`evals/runs/run-11.md`](evals/runs/run-11.md)) scored **15 of 20**.

That is lower than Run 5's 19, and the gap came from the call format: each commit was judged with no other commit to calibrate against. The model wrote a note for a fix to the skill's own description, which no user ever saw, and it attached reasons to four correct skips, which the skill forbids.

## Automating grading, partially (Phase 5)

The script [`scripts/check-mechanical.py`](scripts/check-mechanical.py) graded 4 of the 8 rubric criteria that needed only the response text: past tense, one note per commit, no internal file names, and no asking. I graded the other four against what each commit actually meant, in [`evals/runs/judgment-grades.csv`](evals/runs/judgment-grades.csv). Splitting them made 100-file runs practical, and hand grading kept the combined score trustworthy.

Reconciling the mechanical and human grades case by case caught four runs whose summaries were wrong (Runs 5, 6, 8, and 9). I corrected them in place and kept the original numbers visible beside the fix ([`decisions.md`](decisions.md)).

## Consistency (Phase 6): 9 of 20 clean across 5 repeats

A single pass didn't show whether the skill holds up on repeat, so [`evals/runs/run-11-stats.csv`](evals/runs/run-11-stats.csv) ran all 20 cases 5 times each (100 calls via `run-eval.py --repeats 5`) and counted how many of 5 repeats passed per case. **9 of 20 cases passed every criterion in all 5 repeats.** For comparison, [`run-10-stats.csv`](evals/runs/run-10-stats.csv) measured the same thing on an earlier version of the skill and got 16 of 20.

- **Commit 18 failed all 5 repeats.** It wrote a note instead of skipping in 4 of them and hedged in every one.
- **Commit 6 failed 4 of 5.** It wrote a note for an internal fix no user would see.
- **Eight correct skips failed at least one repeat** by attaching a reason to the skip.

The rule was clear, so I classed this as a model limitation, logged it, and made no edit. My working theory is that one call per commit invites hedging. This finding is still open.

## A second skill (Phase 7)

I built `doc-review` by reviewing three documents by hand ([`evals/cases/doc-review-3.md`](evals/cases/doc-review-3.md)), writing down what an editor would flag ([`evals/gold/doc-review.md`](evals/gold/doc-review.md)), and turning the repeated patterns into a checklist ([`.claude/skills/doc-review/checklist.md`](.claude/skills/doc-review/checklist.md)) before I wrote any rule in SKILL.md. I checked the skill's output against that gold file by eye, not with a scored rubric, so unlike release-notes, doc-review's own accuracy isn't one of the numbers in this case study. That review flagged that the README never said how to run the evals, which is why the README now has a "Running it yourself" section.

The hard-surfaces.md file had the skill ask about uncertainties early on but Rule 10 said not to ask, so I found it and took out the earlier references.

**Trigger accuracy: 18 of 20 before and after a reword** ([`trigger-run-01.md`](evals/runs/trigger-run-01.md), [`trigger-run-02.md`](evals/runs/trigger-run-02.md)). Doc-review (5 of 5) and the "neither" group (5 of 5) passed both times. Two release-notes prompts, "fix my commits" and "apply review of these commits," never said "release notes" and missed both times. I reworded the `description:` line once:

> Old: *"Use when the user asks for release notes generated from commit messages."*
> New: *"Use when the user asks to create, write, generate, add release notes from commit messages."*

Only the 10 release-notes prompts were re-run, since the other skill didn't change. The reword changed nothing, because it added verbs the passing prompts already used ([`decisions.md`](decisions.md)).

**Hard inputs: 3 of 10** ([`hard-cases-run-01.md`](evals/runs/hard-cases-run-01.md)). I scored ten tricky inputs, five per skill, against the matching bullet in [`shared/hard-surfaces.md`](shared/hard-surfaces.md): doc-review scored 1 of 5 and release-notes 2 of 5. My first draft recorded only which skill fired and reported 4 of 10, and rescoring against the bullets flipped two verdicts. Neither `SKILL.md` pointed to `hard-surfaces.md`, so I fixed that and added bullets for wrong-language and wrong-skill inputs. I also found that its "ask for it" bullets could be read as permission to ask about a commit, which the skill's decide-every-commit rule forbids. I scoped the bullets to the whole request and wrote "never ask about a commit" ([`CHANGELOG.md`](CHANGELOG.md), 2026-09-19). Two of my own files had disagreed, and I caught it before it showed up in a test result. I also documented the real input format in [`tools/read-commits.md`](tools/read-commits.md). The skill descriptions still don't cover vague prompts, and I left that gap open.

**One source of truth.** Both skills originally restated some of the same rules, so I moved the three shared ones into `shared/house-style.md` and left each skill with a single reference. `run-eval.py` had to be changed to send the shared files to the model, so the Run 11 numbers predate this move ([`decisions.md`](decisions.md)).

## A safety net (Phase 8)

A GitHub Action re-ran the 20 cases whenever a file under `.claude/skills/` or `shared/` changed, then ran `check-mechanical.py` and [`scripts/check-pass-rate.py`](scripts/check-pass-rate.py). The gate scores only the run the job just produced, because the results file holds every past run and averaging them would let old good runs hide a new bad one. It fails if it finds no rows, so an eval that produced nothing can't pass. The workflow first watched only `.claude/skills/`, and I fixed that gap when I saw that `shared/` edits change the model's behavior too.

I removed the workflow and its API key secret on 2026-09-25 now that the project is finished, so the screenshots in [`findings.md`](evals/findings.md) are the record of it working. To test it, I broke `SKILL.md` on purpose five ways and reverted each one ([`findings.md`](evals/findings.md), "CI safety net"):

| Change to the skill | Pass rate | Check |
|---|---|---|
| None (correct skill) | 0.95 (19/20) | passed |
| Deleted rules 7 to 10 | 0.80 (16/20) | passed |
| Reversed the tense rule to "present tense" | 0.85 (17/20) | passed |
| Added "ask the user first," left "never ask" in place | 0.85 (17/20) | passed |
| Deleted "never ask," kept "ask the user first" | 0.85 (17/20) | passed |
| Added an override: write no notes, only ask | **0.10 (2/20)** | **failed** |
| Reverted to the correct skill | 0.85 (17/20) | passed |

Four simple breaks passed because the shared files repeat the skill's key rules, so removing or contradicting one copy did nothing. The identical correct skill scored 0.95 before the tests and 0.85 after, which is run-to-run noise (one case is worth 0.05). That is why the threshold sits at 0.75 and not 0.90, which would have failed a good skill.

The failing run's log shows the gate itself caught it: every earlier step succeeded, then `check-pass-rate.py` reported `FAIL: pass rate 0.10 is below the minimum 0.75`.

![Log of failed run #8: the run-eval and check-mechanical steps passed, then check-pass-rate.py failed with "pass rate 0.10 is below the minimum 0.75"](evals/screenshots/log%20error%20message.png)

After I reverted the override, the next run (commit `12e8829`) passed, directly above the failed one:

![GitHub Actions run list: run #9, "fixed skill, done testing," passed, directly above the failed run #8](evals/screenshots/fixed%20skill%201.png)

## Limits of this work

I built the full evaluation method on one skill, `release-notes`, to show it in depth rather than repeat it on two. Not everything is covered: `doc-review` is checked by eye, the automated check catches only large regressions, and the results come from a small test set that the skill was tuned against. The list below states each gap.


- **The check catches large regressions, not subtle ones.** It grades only the four mechanical criteria plus one guard that the five commits with a gold-file note must get one, so a skill that skips everything fails. Four of my five test breaks passed, and I added the guard after those tests, so the tests don't cover it. Tone, whether the right commits were skipped, and whether a note is specific enough are judgment criteria that stay hand-graded, so automation has a real ceiling here.
- **Scripted runs can't test the repo-check rule.** `run-eval.py` sends the skill text and one commit to the API with no repo access, so the rule that checks a commit against its description never fires, and rubric criterion 6 is always "unverifiable" in those runs. The earlier manual runs used Claude Code, which can look at a repo, so the two kinds of run don't test exactly the same thing.
- **The skill's examples come from the test cases, and I have no held-out result.** Its worked examples quote or paraphrase commits 4, 12, 14, and 19 from the same 20 test cases, and I fixed the rules against those same cases. I also reworded commits 4 and 19 after Run 3 so they were specific enough to demand a precise note. A score of 19 of 20 partly shows the skill knows these 20, not that it generalizes. I have no held-out set: the other 20 of my original 40 real commits could not be recovered.
- **One person graded.** The gold answers and every judgment grade are mine, with no independent second grade. Only the four mechanical criteria are checked by script.
- **The Run 11 scores predate the shared-rules change.** I have not re-scored the skill by hand since moving rules into `shared/`, apart from the CI runs.
- **The 5-repeat result is still open.** Correct skips still pick up unwanted reasons, and I made no edit.
- **Skill descriptions don't cover vague prompts.** Two release-notes trigger prompts and several hard-case inputs show this gap.
- **`doc-review` has no scored rubric.** I built the eval method in full on `release-notes` only. Everything for `doc-review` is checked by eye, and `check-mechanical.py` covers only `release-notes`.
- **Most measurements ran once.** The trigger and hard-case inputs each ran a single time, so a one-input difference is within noise.
