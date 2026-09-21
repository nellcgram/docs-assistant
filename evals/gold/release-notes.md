# Release Notes Gold

Hand-written answers for `evals/cases/release-notes-20.md`. Commits 1, 2, 4, 8, and 19 get a note, and every other commit is skipped. A skipped commit gets no entry, per rule 4 of the skill (see `decisions.md`, "Write/skip ground truth").

## Release notes

Commit 1 (3087743): Made the already-read list check more reliable. The recommender now looks for a specific heading in your list, so it finds your read books and doesn't recommend them again.

Commit 2 (2d10267): Fixed the formatting of the "other books by this author" line in recommendations so it displayed correctly.

Commit 4 (5da846a): Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted.

Commit 8 (3c8eb5b): Removed a note that flagged when an author had additional qualifying books, simplifying the recommendation format.

Commit 19 (b971722): Checked your list of already-read books before running, so the results did not include books you had already read.

## Skipped (no entry)

3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20.

Reasons, for reference only (a response should not include them):
- Commit 6: an internal fix to the skill's own description.
- Commit 10: editing the changelog and skill language is a developer-facing change.
- Commit 12: ambiguous, so it defaults to skip.
- Commit 18: editing the already-read list down to 3 examples is a developer-facing change.
- Commit 20: moving the rubric to the eval files is a developer-facing change.