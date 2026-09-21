---
name: release-notes
description: Use when the user asks to create, write, generate, add release notes from commit messages.
---

## Purpose
The agent turns raw git commit messages into user-facing release notes.

## Rules

1. Make tone of release notes user-facing; include what changed and why it matters. Example: "Checked your already-read list before recommending, so you were not shown books you had already read."
2. List release notes or entries in the same order as the input commits.
3. When a commit hash is given, try to check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct. Only check the repo if it is known in context; do not search the filesystem or guess at repo locations. If not immediately accessible, mark unverifiable and still write or skip the entry using the description given. Do not stop the response to ask which reading is correct.
4. Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone; a portfolio visitor is not a user of the book-recommendation skill. Otherwise, skip a commit if the effect is not visible to a user of the book-recommendation skill. Do not add an entry for either kind of skip, and do not write a paragraph explaining, defending, or reconsidering a skip decision. The commit is simply left out. A single aggregate line listing skipped commit numbers is fine; per-commit justification is not. If the commit sounds technical and internal but it changes something for that user, include it.
   - Technical example: A commit adding "a pre-run check against the already-read-books file" sounds like an internal implementation detail, but it changes which books the recommender shows; include it, don't skip it.
   - Meta example: a commit described as "Removed agentic AI section from portfolio site" is a project meta-change that can be skipped.
5. Format release notes answers like this: "Commit 20 (f244f58): Sentence here."
6. Write all release notes in the past tense only.
7. A release note fails if either:
   a. It's factually wrong, or
   b. It's accurate but vague; it leaves out the specific mechanism or outcome.
Examples:
   - Vague (fails): "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond."
   - Specific (passes): "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."
8. Follow the shared rules in shared/house-style.md.
9. When the input is missing, unclear, or out of scope, follow the release-notes section of shared/hard-surfaces.md.
10. Before writing any note, ask the user to confirm what the commit does.