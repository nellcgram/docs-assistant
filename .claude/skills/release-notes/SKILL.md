   ---
   name: release-notes
   description: Use when the user asks for release notes generated from commit messages.
   ---

   ## Rules

1. Make tone of release notes user-facing; include what changed and why it matters. Example: "The skill now stops to check already-read file, which prevents the skill from running without exclusion filtering."
2. List release notes or entries in the same order as the input commits.
3. When a commit hash is given, try to check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct. If the repo or commit can't be found or accessed, stop searching after one attempt, proceed using the provided description, and say verification wasn't possible.
4. Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone — a portfolio visitor is not a user of the book-recommendation skill. Otherwise, skip a commit if the effect is not visible to a user of the book-recommendation skill. Do not add an entry for either kind of skip. If the commit sounds technical and internal but it changes something for that user, include it. Example: A commit adding "a pre-run check against the already-read-books file" sounds like an internal implementation detail, but it changes which books the recommender shows; include it, don't skip it.
5. When a skill silently defaults to something, say that a default was applied.
6. Format release notes answers like this: "Commit 20 (f244f58): Sentence here."
7. Write all release notes in the past tense only.
8. Do not use internal file names (for example skill, rubric, eval, findings) in release notes.
9. A release note fails if either:
   a. It's factually wrong, or
   b. It's accurate but vague; it leaves out the specific mechanism or outcome.
   Examples:
      - Vague (fails): "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond."
      - Specific (passes): "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."