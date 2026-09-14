   ---
   name: release-notes
   description: Use when the user asks for release notes generated from commit messages.
   ---

   ## Rules

- Make tone of release notes user-facing; include what changed and why it matters. Example: "The skill now stops to tell user when already-read file is missing, which prevents the skill from running without exclusion filtering."
- List release notes or entries in the same order as the input commits.
- Skip a commit if a user of the book recommender would never notice the change. Do not add an entry for that commit.
- When a skill silently defaults to something, say that a default was applied.
- Format release notes answers like this: "Commit 20 (30aace2): Sentence here."
- Do not check any repo for commits before generating release notes. Use only the input the user gives you to generate release notes.
- Write all release notes in the past tense only.
- Do not us internal file names (for example skill, rubriv, eval, findings) in release notes.
- A release note fails if either:
   a. It's factually wrong, or
   b. It's accurate but vague; it leaves out the specific mechanism or outcome
   Vague (fails): "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond."
Specific (passes): "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."