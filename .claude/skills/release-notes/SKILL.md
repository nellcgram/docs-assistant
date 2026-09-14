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
   b. It's accurate but vague; it leaves out the specific mechanism or outcome (e.g., says 'adjusted when it asked' without naming what default was applied).