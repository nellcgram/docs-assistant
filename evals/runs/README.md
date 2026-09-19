# Results Index

Every number in this project and the file that backs it. Numbers are copied from the linked files, not recomputed here, so if a source file changes, update this page.

Last checked: 2026-09-18.

Related: [case-study.md](../../case-study.md) (the narrative) · [decisions.md](../../decisions.md) (why) · [CHANGELOG.md](../../CHANGELOG.md) (skill edits) · [findings.md](../findings.md) (failure causes)

## The six plan numbers

**1. First version of the skill: 0 of 20** (Phase 2)
Source: [run-01.md](run-01.md)

**2. After diagnosing and fixing the spec: 19 of 20** (Phase 3)
Source: [run-05.md](run-05.md). Run 5 is used instead of Run 6 because Run 6 changed the call format, not just the skill. See [decisions.md](../../decisions.md).

**3. First scripted run: 15 of 20** (Phase 4)
Source: [v3.md](v3.md), hand-graded.

**4. Trigger accuracy: 18 of 20** (Phase 7). 
Source: [trigger-run-01.md](trigger-run-01.md) and [trigger-run-02.md](trigger-run-02.md) got same response.

## Supporting totals

These aren't among the six numbers, but the plan requires them.

- **Phase 5, mechanical vs. manual grading:** reconciled case by case. The comparison caught wrong summaries in Runs 5, 8 and 9, which were corrected in place. Sources: [mechanical-results.csv](mechanical-results.csv), [judgment-grades.csv](judgment-grades.csv), [decisions.md](../../decisions.md).
- **Phase 6, cases passing all 5 repeats (current skill): 9 of 20.** Source: [v3-stats.csv](v3-stats.csv).
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
- **v3: 15 of 20.** First scripted run, current skill. [v3.md](v3.md)
- **v3 variance: 9 of 20 clean in all 5 repeats.** Same skill, 5 repeats. This is the current consistency number. [v3-stats.csv](v3-stats.csv)
- **Trigger 1: 18 of 20.** Trigger test, 20 prompts, before rewording descriptions. [trigger-run-01.md](trigger-run-01.md)
- **Trigger 2: 18 of 20.** Trigger test, 20 prompts, after rewording descriptions had same results. [trigger-run-02.md](trigger-run-02.md)

Runs 6–10 are iteration history, kept as evidence of the diagnose-fix-verify process. They aren't wrong or superseded. [case-study.md](../../case-study.md) explains which numbers the write-up cites.
