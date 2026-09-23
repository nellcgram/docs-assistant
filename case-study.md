# Case Study: Building and Evaluating Two Claude Code Skills

## The problem

This project builds two Claude Code skills and tests them like production software. The first, `release-notes`, turns raw git commit messages into release notes a user can read. Its spec had to cover writing in past tense and active voice, handling a commit whose hash can't be verified, and handling an ambiguous description. Without a spec, release notes would be inconsistent and unspecific.

To build it, I wrote a first version, ran it against 20 real commits, diagnosed each failure, fixed the spec, and re-ran it. I automated the runs and the grading, measured how consistent the skill is, built a second skill (`doc-review`) whose checklist came from hand-reviewing three real documents (I did not build a rubric, scored runs, or automated checks for it, because the goal was to show the method in depth on one skill), and put a GitHub Action around both. The test commits come from a separate book-recommendation project of mine.

## Results at a glance

| Phase | What I measured | Result |
|---|---|---|
| 2 | First version of `release-notes` | 0 of 20 |
| 3 | After diagnosing and fixing the spec | 19 of 20 |
| 4 | First scripted run (one API call per commit) | 15 of 20 |
| 6 | Cases that pass in all 5 repeats | 9 of 20 |
| 7 | Whether the right skill fires (before and after a reword) | 18 of 20, then 18 of 20 |
| 7 | Handling of missing, unclear, and out-of-scope input | 3 of 10 |
| 8 | CI check on a deliberately broken skill | failed at 0.10, passed at 0.85 once fixed |

[`evals/runs/README.md`](evals/runs/README.md) links every number to the file behind it, and [`README.md`](README.md) explains how to re-run any of it.

## First number (Phase 2): 0 of 20

Before writing the skill, I hand-wrote the answer key explaining which of the 20 commits deserve a note and what each note should say ([`evals/gold/release-notes.md`](evals/gold/release-notes.md)). I then ran the first version of the skill ([`.claude/skills/release-notes/SKILL.md`](.claude/skills/release-notes/SKILL.md)) against the 20 commit descriptions ([`evals/cases/release-notes-20.md`](evals/cases/release-notes-20.md)) and graded each case by hand against a 6-criterion rubric ([`evals/rubric.md`](evals/rubric.md), Version 1). Result, in [`evals/runs/run-01.md`](evals/runs/run-01.md): **0 of 20 cases passed every criterion.**

The skill had no rule against checking other repos, so it stopped to ask about them. It had no tense requirement, so notes switched between past and present. It had no rule against naming internal files like `SKILL.md`.

## Diagnosis and second number (Phase 3): 0 of 20 to 19 of 20

I traced every failure to one of three causes in [`evals/findings.md`](evals/findings.md): a **gap** (the skill never addressed the situation), an **ambiguity** (it addressed it unclearly), or a **model limitation** (the skill was clear and the model ignored it). Run 1's failures were almost all gaps, so each became a rule, and [`CHANGELOG.md`](CHANGELOG.md) logs the old and new wording. For example, Run 4 still wrote notes for portfolio-site and eval commits:

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

**Hard inputs: 3 of 10** ([`hard-cases-run-01.md`](evals/runs/hard-cases-run-01.md)). I scored ten tricky inputs, five per skill, against the matching bullet in [`shared/hard-surfaces.md`](shared/hard-surfaces.md): doc-review scored 1 of 5 and release-notes 2 of 5. My first draft recorded only which skill fired and reported 4 of 10, and rescoring against the bullets flipped two verdicts. Neither `SKILL.md` pointed to `hard-surfaces.md`, so I fixed that and added bullets for wrong-language and wrong-skill inputs. I also documented the real input format in [`tools/read-commits.md`](tools/read-commits.md). The skill descriptions still don't cover vague prompts, and I left that gap open.

**One source of truth.** Both skills originally restated some of the same rules, so I moved the three shared ones into `shared/house-style.md` and left each skill with a single reference. `run-eval.py` had to be changed to send the shared files to the model, so the Run 11 numbers predate this move ([`decisions.md`](decisions.md)).

## A safety net (Phase 8)

A [GitHub Action](.github/workflows/eval.yml) re-runs the 20 cases whenever a file under `.claude/skills/` or `shared/` changes, then runs `check-mechanical.py` and [`scripts/check-pass-rate.py`](scripts/check-pass-rate.py). The gate scores only the run the job just produced, because the results file holds every past run and averaging them would let old good runs hide a new bad one. It fails if it finds no rows, so an eval that produced nothing can't pass. The workflow first watched only `.claude/skills/`, and I fixed that gap when I saw that `shared/` edits change the model's behavior too.

To test it, I broke `SKILL.md` on purpose five ways and reverted each one ([`findings.md`](evals/findings.md), "CI safety net"):

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

## What the GitHub Action doesn't cover

- **The check catches large regressions, not subtle ones.** It grades only the four mechanical criteria plus one guard that the five commits with a gold-file note must get one, so a skill that skips everything fails. Four of my five test breaks passed, and I added the guard after those tests, so the tests don't cover it. Tone, whether the right commits were skipped, and whether a note is specific enough are judgment criteria that stay hand-graded, so automation has a real ceiling here.
- **Scripted runs can't test the repo-check rule.** `run-eval.py` sends the skill text and one commit to the API with no repo access, so the rule that checks a commit against its description never fires, and rubric criterion 6 is always "unverifiable" in those runs. The earlier manual runs used Claude Code, which can look at a repo, so the two kinds of run don't test exactly the same thing.
- **The Run 11 scores predate the shared-rules change.** I have not re-scored the skill by hand since moving rules into `shared/`, apart from the CI runs.
- **The 5-repeat result is still open.** Correct skips still pick up unwanted reasons, and I made no edit.
- **Skill descriptions don't cover vague prompts.** Two release-notes trigger prompts and several hard-case inputs show this gap.
- **`doc-review` has no scored rubric.** I built the eval method in full on `release-notes` only. Everything for `doc-review` is checked by eye, and `check-mechanical.py` covers only `release-notes`.
- **Most measurements ran once.** The trigger and hard-case inputs each ran a single time, so a one-input difference is within noise.