# Run 07 Output

## Prompt
Use the release-notes skill and write release notes for all 20 commits in evals/cases/release-notes-20.md, in a single pass — one response covering all 20, not one at a time.

## Response
I ran the release-notes skill against evals/cases/release-notes-20.md. Two things worth flagging before the notes:

Verification: None of the 20 hashes resolve in this repo (git show returns "unknown revision" for each) — treating the provided descriptions as unverified rather than guessing.
Skips: Per the skill's rules, I omitted entries for changelog/README/rubric/eval/portfolio-site/project-meta commits, and for two entries too vague to write a specific, non-guessed note. Skipped: #3, #5, #6, #7, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #20.
Release Notes
Commit 1 (3087743): Specified the exact heading the recommender looks for in your already-read list, so it reliably locates your read books when generating recommendations.

Commit 2 (2d10267): Fixed the formatting of the "other books by this author" line shown in recommendations.

Commit 4 (5da846a): Adjusted genre selection so that when a preference wasn't provided, the recommender defaulted to the contemporary genre and told you it had applied that default, instead of picking silently.

Commit 8 (3c8eb5b): Removed the "other books by this author" note from recommendations, since it added unnecessary complexity to the output.

Commit 19 (b971722): Added a check against your already-read list before generating recommendations, so it no longer suggests books you've already read.