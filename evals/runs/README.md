# Results Index

Every number in this project and the file that backs it. I copied the numbers from the linked files and didn't recompute them, so update this page whenever a source file changes.

Last checked: 2026-09-19.

Related: [case-study.md](../../case-study.md) (the narrative) · [decisions.md](../../decisions.md) (why) · [CHANGELOG.md](../../CHANGELOG.md) (skill edits) · [findings.md](../findings.md) (failure causes)

## The six plan numbers

**1. First version of the skill: 0 of 20** (Phase 2)
Source: [run-01.md](run-01.md)

**2. After diagnosing and fixing the spec: 19 of 20** (Phase 3)
Source: [run-05.md](run-05.md). I used Run 5 instead of Run 6 because Run 6 changed the call format, not just the skill. See [decisions.md](../../decisions.md).

**3. First scripted run: 15 of 20** (Phase 4)
Source: [v3.md](v3.md), hand-graded.

**4. Trigger accuracy: 18 of 20 before and after rewording** (Phase 7)
Source: [trigger-run-01.md](trigger-run-01.md) and [trigger-run-02.md](trigger-run-02.md). The reword changed nothing.

**5. Hard cases: 3 of 10** (Phase 7)
Source: [hard-cases-01.md](hard-cases-01.md). Doc-review scored 1 of 5 and release-notes 2 of 5.

**6. Context arrangement: not attempted** (Phase 8)
See [decisions.md](../../decisions.md).

## Supporting totals

These aren't among the six numbers, but the plan requires them.

- **Phase 5, mechanical vs. manual grading:** I reconciled them case by case. The comparison caught wrong summaries in Runs 5, 6, 8, and 9, which I corrected in place. Sources: [mechanical-results.csv](mechanical-results.csv), [judgment-grades.csv](judgment-grades.csv), [decisions.md](../../decisions.md).
- **Phase 6, cases passing all 5 repeats: 9 of 20.** Source: [v3-stats.csv](v3-stats.csv). This predates the shared-rules change (see [decisions.md](../../decisions.md)).
- **Phase 6, same measure on an earlier skill (Run 10): 16 of 20.** Source: [run-10-stats.csv](run-10-stats.csv).
- **Phase 9, CI failing once and passing once:** not built. There is no `.github/workflows/eval.yml` and no `scripts/check-pass-rate.py`.

## Every run

What changed since the previous run, and the score.

- **Run 1: 0 of 20.** First version of the skill, no rules yet. [run-01.md](run-01.md)
- **Run 2: 0 of 20.** Added rules against checking other repos, tense, and internal filenames. [run-02.md](run-02.md)
- **Run 3: 0 of 20.** Broadened the repo-check rule. [run-03.md](run-03.md)
- **Run 4: 17 of 20.** Fixed vague notes and a mis-skipped commit. [run-04.md](run-04.md)
- **Run 5: 19 of 20.** Added a repo-check stop condition and a portfolio/eval/meta skip rule. [run-05.md](run-05.md)
- **Run 6: 4 of 20.** Same skill, one call per commit instead of one batch. [run-06/grading.md](run-06/grading.md)
- **Run 7: 20 of 20.** Same skill, batched again. Confirms Run 6 was a call-format artifact. [run-07.md](run-07.md)
- **Run 8: 19 of 20.** Added a "decide, don't ask" rule. [run-08.md](run-08.md)
- **Run 9: 20 of 20.** Added a default-to-skip tiebreak for ambiguous commits. [run-09.md](run-09.md)
- **Run 10: 16 of 20 clean in all 5 repeats.** Same skill, one call per commit, 5 repeats. [run-10-stats.csv](run-10-stats.csv)
- **v3: 15 of 20.** First scripted run. [v3.md](v3.md)
- **v3 variance: 9 of 20 clean in all 5 repeats.** Same skill, 5 repeats. This predates the shared-rules change. [v3-stats.csv](v3-stats.csv)
- **Trigger 1: 18 of 20.** 20 prompts, before rewording the release-notes description. [trigger-run-01.md](trigger-run-01.md)
- **Trigger 2: 18 of 20.** The 10 release-notes prompts re-run after rewording, with identical results. [trigger-run-02.md](trigger-run-02.md)
- **Hard cases 1: 3 of 10.** 10 tricky inputs, scored against `shared/hard-surfaces.md`. [hard-cases-01.md](hard-cases-01.md)

Runs 6 through 10 are iteration history and remain valid evidence of the diagnose-fix-verify process. [case-study.md](../../case-study.md) explains which numbers the write-up cites.
