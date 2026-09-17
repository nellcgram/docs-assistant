# Results Index

One line per run: what changed since the last one, and the score. For the narrative behind these numbers, see [`case-study.md`](../case-study.md). For the reasoning behind a specific number, see [`decisions.md`](../decisions.md), [`CHANGELOG.md`](../CHANGELOG.md), and [`findings.md`](../findings.md).

| Run | What changed | Score | File |
|---|---|---|---|
| 1 | First version of the skill (no rules yet) | 0 of 20 | [run-01.md](run-01.md) |
| 2 | Added rules against checking other repos, tense, internal filenames | 0 of 20 | [run-02.md](run-02.md) |
| 3 | Broadened the repo-check rule after Run 2 still tried to look up commits | 0 of 20 | [run-03.md](run-03.md) |
| 4 | Fixed vague notes and a mis-skipped commit found in Run 3 | 17 of 20 | [run-04.md](run-04.md) |
| 5 | Added a repo-check stop condition and a portfolio/eval/meta skip rule | 19 of 20 | [run-05.md](run-05.md) |
| 6 | Same skill as Run 5, tested with isolated single-commit calls instead of one batched request | 4 of 20 | [run-06/grading.md](run-06/grading.md) |
| 7 | Same skill as Run 6, re-run batched — confirms Run 6 was a call-format artifact | 20 of 20 | [run-07.md](run-07.md) |
| 8 | Added a "decide, don't ask" rule after Run 6's regression | 19 of 20 | [run-08.md](run-08.md) |
| 9 | Added a default-to-skip tiebreak for ambiguous commits | 20 of 20 | [run-09.md](run-09.md) |
| 10 | Same skill as Run 9, isolated-call format, 5 repeats — historical variance snapshot | 16 of 20 clean across 5 reps | [run-10-stats.csv](run-10-stats.csv) |
| v3 | First scripted run (`scripts/run-eval.py`), current skill, isolated-call format | 15 of 20 | [v3.md](v3.md) |
| v3 variance | Same skill as v3, 5 repeats — current, live consistency number | 9 of 20 clean across 5 reps | [v3-stats.csv](v3-stats.csv) |

**Current, load-bearing numbers:** first (Run 1, 0/20), second (Run 5, 19/20), Phase 4 (v3, 15/20), Phase 6 consistency (v3 variance, 9/20 clean). Runs 6–10 are earlier iteration history, kept as evidence of the diagnose-fix-verify process, not superseded or wrong — see `case-study.md` for which numbers the write-up actually cites and why.
