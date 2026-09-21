# Case Study: Building and Evaluating Two Claude Code Skills

## The problem

Turning a raw git commit message into a release note a user can read has no obvious spec. Someone has to decide which commits matter to a user, what tense to write in, how to handle a commit whose hash can't be verified, and what to do when a description is ambiguous. Without a written and tested spec, "generate release notes" means "guess, inconsistently, every time."

I built that spec as a Claude Code skill, `release-notes`, the way I would build software I want to trust. I wrote a first version, ran it against 20 real commits, diagnosed each failure, fixed the spec, and re-ran it. I then automated the runs and the grading, measured how consistent the skill is, built a second skill (`doc-review`) the same way, and put a GitHub Action around both. The test commits come from a real feature, the book-recommendation skill behind [nellcgram.github.io](https://nellcgram.github.io), so "would a user notice this change?" has a real answer.

## Results at a glance

| Phase | What I measured | Result |
|---|---|---|
| 2 | First version of `release-notes` | 0 of 20 |
| 3 | After diagnosing and fixing the spec | 19 of 20 |
| 4 | First scripted run (one API call per commit) | 15 of 20 |
| 6 | Cases that pass in all 5 repeats | 9 of 20 |
| 7 | Whether the right skill fires (before and after a reword) | 18 of 20, then 18 of 20 |
| 7 | Handling of missing, unclear, and out-of-scope input | 3 of 10 |
| 8 | Context arrangement | not attempted |
| 9 | CI check on a deliberately broken skill | failed at 0.10, passed at 0.85 once fixed |

[`evals/runs/README.md`](evals/runs/README.md) links every number to the file behind it, and [`README.md`](README.md) explains how to re-run any of it.

## First number (Phase 2): 0 of 20

Before writing the skill, I hand-wrote the answer key: which of the 20 commits deserve a note and what each note should say ([`evals/gold/release-notes.md`](evals/gold/release-notes.md)). I then ran the first version of the skill ([`.claude/skills/release-notes/SKILL.md`](.claude/skills/release-notes/SKILL.md)) against the 20 commit descriptions ([`evals/cases/release-notes-20.md`](evals/cases/release-notes-20.md)) as one batched request in a fresh Claude session, and graded each case by hand against a 6-criterion rubric ([`evals/rubric.md`](evals/rubric.md), Version 1). Result, in [`evals/runs/run-01.md`](evals/runs/run-01.md): **0 of 20 cases passed every criterion.**

The skill had no rule against checking other repos for the real commit, so it interrupted the run to ask about them. It had no tense requirement, so notes drifted between past and present. It had no rule against naming internal files like `SKILL.md`, which don't belong in user-facing output. A first draft with no rules should fail this way, and the failures gave me concrete things to diagnose.

## Diagnosis and second number (Phase 3): 0 of 20 to 19 of 20

I traced every failure to one of three causes in [`evals/findings.md`](evals/findings.md): a **gap** (the skill never addressed the situation), an **ambiguity** (it addressed it unclearly), or a **model limitation** (the skill was clear and the model ignored it). Run 1's failures were almost all gaps: nothing forbade checking other repos, required past tense, or barred internal file names. Each gap became a rule, and [`CHANGELOG.md`](CHANGELOG.md) logs the old and new wording. For example, Run 4 still wrote notes for portfolio-site and eval commits:

> Old: *"Skip a commit if the effect is not visible to the user."*
> New: *"Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone. A portfolio visitor is not a user of the book-recommendation skill."*

It took several rounds. Runs 1 to 3 all scored 0 of 20: Run 2 still tried to look commits up under narrower wording, and Run 3 turned up notes that were accurate but too vague to be useful (an accurate-but-vague note now fails the rubric). Run 4 scored 17 of 20 and exposed the portfolio and project-meta misclassification above, plus a repo-check rule with no stop condition. Run 5 ([`evals/runs/run-05.md`](evals/runs/run-05.md)) scored **19 of 20**. The one miss, commit 18, hedged ("I'm not confident; let me know if you want it included") instead of deciding, and the file still shows it. I added a "decide, don't ask" rule and a default-to-skip tiebreak for ambiguous commits, and Runs 8 and 9 scored 19 and then 20 of 20 ([`evals/runs/README.md`](evals/runs/README.md) lists every run).

Run 6 scored 4 of 20 with no skill change, because I switched to one API call per commit. Run 7, batched again, scored 20 of 20, so the call format caused the drop. Runs 1 and 5 both ran as one batched request, so only the skill changed between them, and that is why Run 5, not Run 6, is the second number ([`decisions.md`](decisions.md), "Run 1 vs Run 5 is the second number, not Run 6").

## Automating the run (Phase 4): 15 of 20

Once the skill held up under manual testing, I automated the harness. [`scripts/run-eval.py`](scripts/run-eval.py) reads the skill and the 20 cases and calls the API once per commit, where before I pasted prompts into a fresh session by hand. A script now runs the cases, but grading was still by hand at this point. The scripted run (Run 11, [`evals/runs/run-11.md`](evals/runs/run-11.md)) scored **15 of 20**.

That is lower than Run 5's 19, and the gap comes from the call format, not a worse skill. Each commit is judged alone, with no other commit to calibrate against. The model wrote a note for commit 6 (a fix to the skill's own description) that a user never sees and should have been skipped. It also attached reasons to four correct skips (commits 10, 11, 18, and 20), which rule 4 forbids ("a single aggregate line listing skipped commit numbers is fine; per-commit justification is not").

## Automating grading, partially (Phase 5)

[`scripts/check-mechanical.py`](scripts/check-mechanical.py) grades 4 of the 8 rubric criteria that need only the response text: past tense, one note per commit, no internal file names, and no asking. A person grades the other four against what each commit actually means, in [`evals/runs/judgment-grades.csv`](evals/runs/judgment-grades.csv). Splitting them makes 100-file runs practical, and hand grading keeps the combined score trustworthy.

The honest result isn't "the two methods agreed." It is that reconciling them case by case caught real mistakes. `run-05.md`'s original "7 of 7" summary had graded the whole run as one holistic judgment and missed commit 18's hedge. `run-08.md` and `run-09.md` had graded only their written commits and never checked whether their 14 or 15 skipped commits were correct skips. Run 6's "0 of 20" was really 4 of 20, because "unverifiable" had been counted as a fail. I corrected all of them in place and kept the original numbers visible next to the fix ([`decisions.md`](decisions.md)). A systematic check surfacing errors that a well-intentioned holistic read missed is the evidence the grading method works. I also made the rubric require one graded row per case for this reason.

## Consistency, not just correctness (Phase 6): 9 of 20 clean across 5 repeats

A single pass doesn't show whether the skill holds up on repeat. [`evals/runs/run-11-stats.csv`](evals/runs/run-11-stats.csv) runs all 20 cases 5 times each (100 calls via `run-eval.py --repeats 5`) and counts how many of 5 repeats passed per case. **9 of 20 cases pass every criterion in all 5 repeats.** For comparison, [`run-10-stats.csv`](evals/runs/run-10-stats.csv) measured the same thing on an earlier version of the skill and got 16 of 20.

- **Commit 18 (`b50af03`) fails all 5 repeats.** It wrote a note instead of skipping in 4 of them and hedged in every one.
- **Commit 6 (`1e3c29b`) fails 4 of 5.** It wrote a note for the same kind of internal self-description fix that Run 11 already caught once.
- **Eight correct skips (commits 7, 10, 11, 12, 13, 14, 16, 20) fail at least one repeat.** Each attaches a reason to a bare skip, against rule 4.

Rule 4 is clear, so I classed this as a model limitation, logged it, and made no edit. My working theory is that one call per commit invites hedging. This finding is still open.

## A second skill, and a single source of truth (Phase 7)

I built `doc-review` the same way as the first skill, from evidence and not from guesses. I reviewed three real documents by hand ([`evals/cases/doc-review-3.md`](evals/cases/doc-review-3.md)), wrote down what an editor would flag ([`evals/gold/doc-review.md`](evals/gold/doc-review.md)), and turned the repeated patterns into a checklist ([`.claude/skills/doc-review/checklist.md`](.claude/skills/doc-review/checklist.md)) before writing any rule. That review flagged that the README never said how to run the evals, which is why the README now has a "Running it yourself" section.

**Trigger accuracy: 18 of 20 before and after a reword** ([`trigger-run-01.md`](evals/runs/trigger-run-01.md), [`trigger-run-02.md`](evals/runs/trigger-run-02.md)). Doc-review (5 of 5) and the "neither" group (5 of 5) passed both times. Two release-notes prompts, "fix my commits" and "apply review of these commits," never said "release notes" and missed both times. I reworded the `description:` line once:

> Old: *"Use when the user asks for release notes generated from commit messages."*
> New: *"Use when the user asks to create, write, generate, add release notes from commit messages."*

The reword changed nothing, because it added verbs the passing prompts already used. I kept it and logged that it wasn't a fix ([`decisions.md`](decisions.md)).

**Hard inputs: 3 of 10** ([`hard-cases-run-01.md`](evals/runs/hard-cases-run-01.md)). I scored ten tricky inputs, five per skill, against the matching bullet in [`shared/hard-surfaces.md`](shared/hard-surfaces.md): doc-review scored 1 of 5 and release-notes 2 of 5. My first draft recorded only which skill fired and reported 4 of 10, and rescoring against the bullets flipped two verdicts. Neither `SKILL.md` pointed to `hard-surfaces.md`, so I fixed that and added bullets for wrong-language and wrong-skill inputs. I also wrote [`tools/read-commits.md`](tools/read-commits.md) to document the input format the skill really receives. The skill descriptions still don't cover vague prompts, and I left that gap open.

**One source of truth.** `shared/house-style.md` first duplicated the doc-review checklist, and release-notes restated two of its rules. On 2026-09-19 I cut it to the three rules both skills use, turned the duplicates into one-line pointers (later removed), and moved the checklist rules back into doc-review. Each rule now has one home. The change also forced a script fix: `run-eval.py` had to send the shared files to the model, because the API sees only the prompt, and moved rules would have vanished from every scripted run. The Run 11 numbers predate this change ([`decisions.md`](decisions.md)).

## Context arrangement (Phase 8): not attempted

I did not test whether identical instructions score differently depending on where they sit in the context (inline, in a referenced file, or late in a long session), so this phase has no number and I make no claim about it. I spent the time on the second skill and on verifying the grading, which surfaced more concrete problems.

## A safety net (Phase 9)

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

Four simple breaks passed because `shared/hard-surfaces.md` and `house-style.md` repeat the skill's key rules, so removing or contradicting one copy did nothing. Only an override aimed at the shared files got through. The check failed at the pass-rate step, not on a crash, in commit `58ba015`, and passed again after the revert in commit `12e8829`. The identical correct skill scored 0.95 before the tests and 0.85 after, which is run-to-run noise (one case is worth 0.05). That is why the threshold sits at 0.75 and not 0.90, which would have failed a good skill. The GitHub Actions logs aren't stored in the repo, so the scores above come from `findings.md`. Two early runs also failed because my API credit ran out, and I didn't count them.

## What this doesn't cover

- **The check catches large regressions, not subtle ones.** It grades only the four mechanical criteria, and four of my five test breaks passed. Tone, whether the right commits were skipped, and whether a note is specific enough are judgment criteria that stay hand-graded, so automation has a real ceiling here.
- **The Run 11 scores predate the shared-rules change.** I have not re-scored the skill by hand since moving rules into `shared/`, apart from the CI runs.
- **The 5-repeat result is still open.** Correct skips still pick up unwanted reasons, and I made no edit.
- **Skill descriptions don't cover vague prompts.** Two release-notes trigger prompts and several hard-case inputs show this gap.
- **`doc-review` has no scored rubric yet.** Everything for that skill is graded by hand, and `check-mechanical.py` covers only `release-notes`.
- **Most measurements ran once.** The trigger and hard-case inputs each ran a single time, so a one-input difference is within noise.
- **Phase 8 was not run.**
