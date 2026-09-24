# Results Index

This file is every number in this project and the file that backs it. I copied the numbers from the linked files and didn't recompute them, so update this page whenever a source file changes.

Last checked: 2026-09-21.

Related: [case-study.md](../../case-study.md) (the narrative) · [decisions.md](../../decisions.md) (why) · [CHANGELOG.md](../../CHANGELOG.md) (skill edits) · [findings.md](../findings.md) (failure causes)

## The five plan numbers

**1. First version of the skill: 0 of 20** (Phase 2)
Source: [run-01.md](run-01.md)

**2. After diagnosing and fixing the spec: 19 of 20** (Phase 3)
Source: [run-05.md](run-05.md). I used Run 5 instead of Run 6 because Run 6 changed the call format, not just the skill. See [decisions.md](../../decisions.md).

**3. First scripted run: 15 of 20** (Phase 4)
Source: [run-11.md](run-11.md), hand-graded.

**4. Trigger accuracy: 18 of 20 before and after rewording** (Phase 7)
Source: [trigger-run-01.md](trigger-run-01.md) and [trigger-run-02.md](trigger-run-02.md). Only the 10 release-notes prompts were re-run, since the other skill didn't change. The reword changed nothing.

**5. Hard cases: 3 of 10** (Phase 7)
Source: [hard-cases-run-01.md](hard-cases-run-01.md). Doc-review scored 1 of 5 and release-notes 2 of 5.

## Supporting totals

These aren't among the five numbers, but the plan requires them.

- **Phase 5, mechanical vs. manual grading:** I reconciled them case by case. The comparison caught wrong summaries in Runs 5, 6, 8, and 9, which I corrected in place. Sources: [mechanical-results.csv](mechanical-results.csv), [judgment-grades.csv](judgment-grades.csv), [decisions.md](../../decisions.md).
- **Phase 6, cases passing all 5 repeats: 9 of 20.** Source: [run-11-stats.csv](run-11-stats.csv). This predates the shared-rules change (see [decisions.md](../../decisions.md)).
- **Phase 6, same measure on an earlier skill (Run 10): 16 of 20.** Source: [run-10-stats.csv](run-10-stats.csv).
- **CI failing once and passing once:** a deliberately broken skill scored 0.10 (2 of 20) and failed the check (commit `58ba015`). After the revert the identical skill scored 0.85 (17 of 20) and passed (commit `12e8829`). Sources: [findings.md](../findings.md), `.github/workflows/eval.yml`, and screenshots of the GitHub Actions pages: the [run list](../screenshots/all%20workflows%20error%20message.png), the [failing log](../screenshots/log%20error%20message.png), the [passing run list](../screenshots/fixed%20skill%201.png), and the [passing log](../screenshots/fixed%20skill%202_log.png).

## Every run

Each entry says what changed since the previous run and what the run scored. Every scripted run uses the `run-NN` name, and CI writes to `run-12`.

- **Run 1: 0 of 20.** The first version of the skill had no rules yet. [run-01.md](run-01.md)
- **Run 2: 0 of 20.** I added rules against checking other repos, using the wrong tense, and naming internal files. [run-02.md](run-02.md)
- **Run 3: 0 of 20.** I broadened the repo-check rule. [run-03.md](run-03.md)
- **Run 4: 17 of 20.** I fixed vague notes and one wrongly skipped commit. [run-04.md](run-04.md)
- **Run 5: 19 of 20.** I added a repo-check stop condition and a skip rule for portfolio, eval, and project-meta commits. [run-05.md](run-05.md)
- **Run 6: 4 of 20.** The same skill ran one call per commit instead of one batch. [run-06.md](run-06.md)
- **Run 7: 20 of 20.** The same skill ran batched again, which confirmed that Run 6 was a call-format artifact. [run-07.md](run-07.md)
- **Run 8: 19 of 20.** I added a "decide, don't ask" rule. [run-08.md](run-08.md)
- **Run 9: 20 of 20.** I added a default-to-skip tiebreak for ambiguous commits. [run-09.md](run-09.md)
- **Run 10: 16 of 20 clean in all 5 repeats.** The same skill ran one call per commit, 5 times. [run-10-stats.csv](run-10-stats.csv)
- **Run 11: 15 of 20.** This was the first scripted run. [run-11.md](run-11.md)
- **Run 11 variance: 9 of 20 clean in all 5 repeats.** The same skill ran 5 times, before the shared-rules change. [run-11-stats.csv](run-11-stats.csv)
- **Trigger 1: 18 of 20.** I ran 20 prompts before rewording the release-notes description. [trigger-run-01.md](trigger-run-01.md)
- **Trigger 2: 18 of 20.** I re-ran the 10 release-notes prompts after the reword and got identical results. [trigger-run-02.md](trigger-run-02.md)
- **Hard cases: 3 of 10.** I scored 10 tricky inputs against `shared/hard-surfaces.md`. [hard-cases-run-01.md](hard-cases-run-01.md)
- **CI, correct skill: 0.95 (19 of 20), then 0.85 (17 of 20) after the revert.** The same skill scored differently, which is run-to-run noise. The check uses mechanical criteria only. See [findings.md](../findings.md).
- **CI, four mild breaks: 0.80 to 0.85.** All four passed the 0.75 gate.
- **CI, override break: 0.10 (2 of 20).** This run failed the check.

Runs 6 through 10 are iteration history and remain valid evidence of the diagnose, fix, and verify process. [case-study.md](../../case-study.md) explains which numbers the write-up cites.
