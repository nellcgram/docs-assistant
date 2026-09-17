# Run 08

Graded one row per case, out of 20, per the grading rule in `evals/rubric.md` and the write/skip ground truth in `decisions.md`: write {1, 2, 4, 8, 19}, skip everything else.

| Case | Decision | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Passed all? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1  | Write | P | P | P | P | U | P | P | P | Yes |
| 2  | Write | P | P | P | P | U | P | U | P | Yes |
| 3  | Skip  | U | P | P | P | U | U | U | P | Yes |
| 4  | Write | P | P | P | P | P | P | P | P | Yes |
| 5  | Skip  | U | P | P | P | U | U | U | P | Yes |
| 6  | Skip  | U | P | P | P | U | U | U | P | Yes |
| 7  | Skip  | U | P | P | P | U | U | U | P | Yes |
| 8  | Write | P | P | P | P | U | P | P | P | Yes |
| 9  | Skip  | U | P | P | P | U | U | U | P | Yes |
| 10 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 11 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 12 | Write | P | P | **F** | P | U | P | U | **F** | **No** |
| 13 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 14 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 15 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 16 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 17 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 18 | Skip  | U | P | P | P | U | U | U | P | Yes |
| 19 | Write | P | P | P | P | U | P | P | P | Yes |
| 20 | Skip  | U | P | P | P | U | U | U | P | Yes |

**Passed every criteria: 19 of 20.**

Only commit 12 (6fce484, "Take Book Recommendations project offline") fails: written up as a feature change instead of skipped, per SKILL.md's ambiguous-defaults-to-skip rule (see `evals/findings.md`'s Run 8 entry and `decisions.md`'s "Ambiguous feature-vs-portfolio commits default to skip"). Criterion 8 also fails on commit 12: "The wording leaves some ambiguity about whether this meant discontinuing the feature itself versus removing its portfolio listing; this reads as the former" is a reconsidering/hedging clause. C7 is graded Unverifiable rather than Fail for commit 12, since once C3 fails, whether the note's content is "specific enough" is moot.
