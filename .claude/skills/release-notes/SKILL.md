   ---
   name: release-notes
   description: Use when the user asks for release notes or a changelog entry generated from commit messages.
   ---

   ## Rules

   ### Rules for release notes
- Make tone of release notes user-facing; include what changed and why it matters. Example: "The skill now stops to tell user when already-read file is missing, which prevents the skill from running without exclusion filtering."
- List release notes or entries in the same order as the input commits.
- Skip a commit if a user of the book recommender would never notice the change. Do not add an entry for that commit.
- When a skill silently defaults to something, say that a default was applied.
- Format release notes answers like this: "Commit 20 (30aace2): Sentence here."
- Do not check other repos for the release notes commit hashes; use only the raw commits the user gives you.
- Write all release notes in the past tense only.
- Do not us internal file names (for example skill, rubriv, eval, findings) in release notes.

   ### Rules for changelog
- Make changelog concise and engineer-facing.
- List changelog entries in chronological order, most recent first.
- Separate changelog entries into ##Added, ##Deleted, ##Changed.
- Body format: "Fixed: The rule had 2 contradicting requirements. Old: "Text here." New: "Rewritten text here."

EXAMPLE:
### Changed
- `abc1234` Fixed contradictory instructions in the recommendation skill. Old: "Text here." New: "Rewritten text here."

- When a skill silently defaults to something, say that a default was applied.
- Do not check other repos for the commit hashes; use only the raw commits the user gives you.
- Write all changelog notes in the past tense only.