# Case Study: Building and Evaluating a Release-Notes Skill

## The problem

Turning a raw git commit message into a release note that a user can read has no obvious spec. Someone must decide which commits matter to a user, what tense to use, how to handle a commit that can't be verified, and what to do when a description is ambiguous. Without a written and tested spec, "generate release notes" means "guess, inconsistently, every time."

I built that spec as a Claude Code skill, the way I would build any software I want to trust. I wrote a first version, ran it against real cases, diagnosed each failure, fixed the spec, and re-ran it. I then built a second skill, `doc-review`, and put an automated check around both.

## Results at a glance

| Phase | What I measured | Result |
|---|---|---|
| 2 | First version of `release-notes` | 0 of 20 |
| 3 | After diagnosing and fixing the spec | 19 of 20 |
| 4 | First scripted run (one API call per commit) | 15 of 20 |
| 6 | Cases that pass in all 5 repeats | 9 of 20 |
| 7 | Whether the right skill fires (before and after a reword) | 18 of 20, then 18 of 20 |
| 7 | Handling of missing, unclear, and out-of-scope input | 3 of 10 |
| 9 | CI check on a deliberately broken skill | failed at 0.10, passed at 0.85 once fixed |

[evals/runs/README.md](evals/runs/README.md) links every number to the file behind it.

## Phase 2: 0 of 20

I ran the first version of the skill ([SKILL.md](.claude/skills/release-notes/SKILL.md)) against 20 real commit descriptions ([release-notes-20.md](evals/cases/release-notes-20.md)) and graded each response against a rubric ([rubric.md](evals/rubric.md), Version 1). Zero cases passed every criterion ([run-01.md](evals/runs/run-01.md)). The skill had no rule against checking other repos, no tense requirement, and no ban on naming internal files. A first draft with no rules should fail this way, and the failures gave me concrete things to diagnose.

## Phase 3: 0 of 20 to 19 of 20

I traced every failure to one of three causes in [findings.md](evals/findings.md): a gap (the skill never addressed the situation), an ambiguity (it addressed it unclearly), or a model limitation (the skill was clear and the model ignored it). Most of Run 1's failures were gaps. I turned each gap into a rule and logged the old and new wording in [CHANGELOG.md](CHANGELOG.md). For example, Run 4 still wrote notes for portfolio-site and eval commits:

> Old: *"Skip a commit if the effect is not visible to the user."*
> New: *"Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone. A portfolio visitor is not a user of the book-recommendation skill."*

It took five runs to reach 19 of 20 ([run-05.md](evals/runs/run-05.md)). The one miss, commit 18, hedged ("I'm not confident; let me know") instead of deciding, and the file still shows it.

Run 6 scored 4 of 20 with no skill change, because I switched to one API call per commit. Run 7, batched again, scored 20 of 20, so the call format caused the drop. I paired Run 1 with Run 5 because only the skill changed between them ([decisions.md](decisions.md)).

## Phase 4: 15 of 20

[run-eval.py](scripts/run-eval.py) calls the API once per commit, where before I pasted prompts into a fresh session by hand. The scripted run (Run 11) scored 15 of 20 ([run-11.md](evals/runs/run-11.md)). The gap from Run 5 comes from the call format. Each commit is judged alone, and the model wrote a note for commit 6 that it should have skipped and attached reasons to four correct skips, which rule 4 forbids.

## Phase 5: automated grading, cross-checked by hand

[check-mechanical.py](scripts/check-mechanical.py) grades 4 of the 8 rubric criteria that need only the text: tense, one note per commit, no internal file names, and no asking. A person grades the other four in [judgment-grades.csv](evals/runs/judgment-grades.csv). Reconciling the two methods case by case caught real errors. The original Run 5 summary ("7 of 7") had missed commit 18's hedge, and Runs 8 and 9 had never checked whether their skipped commits were correct skips. I corrected all three in place and kept the original numbers visible.

## Phase 6: consistency

A single pass doesn't show whether the skill holds up on repeat. I ran all 20 cases 5 times each (100 calls, [run-11-stats.csv](evals/runs/run-11-stats.csv)), and only 9 cases passed every time. Commit 18 failed all 5 repeats, and commit 6 failed 4. Eight more correct skips failed at least one repeat by attaching a reason to a bare skip. That is a model limitation, since the rule is clear, so I logged it and made no edit.

## Phase 7: a second skill, trigger accuracy, and hard inputs

I built `doc-review` from three real documents. I reviewed each by hand ([doc-review-3.md](evals/cases/doc-review-3.md)), wrote the review an editor would give ([gold/doc-review.md](evals/gold/doc-review.md)), and turned the repeated patterns into a [checklist](.claude/skills/doc-review/checklist.md) before writing any rule.

- **Trigger accuracy: 18 of 20 before and after a reword** ([trigger-run-01.md](evals/runs/trigger-run-01.md), [trigger-run-02.md](evals/runs/trigger-run-02.md)). Two prompts never said "release notes" and missed both times. The reword targeted phrasings that already worked, so it changed nothing.
- **Hard inputs: 3 of 10** ([hard-cases-run-01.md](evals/runs/hard-cases-run-01.md)). The skills often guessed at a vague request or did an out-of-scope task instead of asking or declining. Neither skill pointed to [hard-surfaces.md](shared/hard-surfaces.md), so I fixed that and added bullets for wrong-language and wrong-skill inputs. The skill descriptions still don't cover vague prompts, and I left that gap open.

I also moved the rules both skills share into [house-style.md](shared/house-style.md), so each rule lives in one place.

## Phase 8: not attempted

I did not test whether identical instructions score differently depending on where they sit in the context, so this phase has no number. I spent the time on the second skill and on verifying the grading, which surfaced more concrete problems.

## Phase 9: the CI safety net

A [GitHub Action](.github/workflows/eval.yml) re-runs the 20 cases when a skill or shared file changes and fails the check below a 0.75 pass rate. To test it, I broke the skill on purpose five ways. Four mild breaks scored 0.80 to 0.85 and passed, because the shared files repeat the skill's key rules. An override that told the model to write no notes and only ask scored 0.10 and failed. After I reverted it, the same skill scored 0.85 and passed. The identical correct skill scored 0.95 before the tests and 0.85 after the revert, which is why the threshold sits at 0.75 and not 0.90. [findings.md](evals/findings.md) has the full table.

## What this doesn't cover

- **The check catches large regressions, not subtle ones.** Four of my five test breaks passed. A person still reviews small changes, and the four judgment criteria stay hand-graded.
- **The Run 11 scores predate the shared-rules change.** I have not re-scored the skill since I moved rules into `shared/`, apart from the CI runs.
- **The 5-repeat result is still open.** Correct skips still pick up unwanted reasons, and I made no edit.
- **Skill descriptions don't cover vague prompts.** Two release-notes trigger prompts and four hard-case inputs show this gap.
- **`doc-review` has no scored rubric yet.** Everything for that skill is graded by hand, and `check-mechanical.py` covers only `release-notes`.
- **Phase 8 was not run.**
