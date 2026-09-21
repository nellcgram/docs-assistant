---
name: release-notes
description: Use when the user asks to create, write, generate, add release notes from commit messages.
---

## Purpose
The agent turns raw git commit messages into user-facing release notes.

## Rules

1. Make tone of release notes user-facing; include what changed and why it matters. See examples.md for worked examples.
2. List release notes or entries in the same order as the input commits.
3. When a commit hash is given, try to check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct. Only check the repo if it is known in context; do not search the filesystem or guess at repo locations. If not immediately accessible, mark unverifiable and still write or skip the entry using the description given. Do not stop the response to ask which reading is correct.
4. Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone; a portfolio visitor is not a user of the book-recommendation skill. Otherwise, skip a commit if the effect is not visible to a user of the book-recommendation skill. Do not add an entry for either kind of skip, and do not write a paragraph explaining, defending, or reconsidering a skip decision. The commit is simply left out. A single aggregate line listing skipped commit numbers is fine; per-commit justification is not. If the commit sounds technical and internal but it changes something for that user, include it. See examples.md for worked examples.
5. Moved to shared/house-style.md, rule 3 (state when a default was applied).
6. Format release notes answers like this: "Commit 20 (f244f58): Sentence here."
7. Write all release notes in the past tense only.
8. Moved to shared/house-style.md, rule 1 (no internal file names).
9. A release note fails if either:
   a. It's factually wrong, or
   b. It's accurate but vague; it leaves out the specific mechanism or outcome.
See examples.md for worked examples.
10. Do not stop to ask the user to disambiguate a commit before finishing the response; decide using the rules above. Example: "Take Book Recommendations project offline" could mean the portfolio listing was pulled (skip) or the skill itself was taken down (write). Pick the reading better supported by the wording, write or skip accordingly, and flag the uncertainty in one clause if it matters. Don't ask which reading is correct. When a description could mean either the feature itself or its portfolio/project-level presence with no stronger signal, default to skip.
11. Follow the shared rules in shared/house-style.md.
12. When the input is missing, unclear, or out of scope, follow the release-notes section of shared/hard-surfaces.md.