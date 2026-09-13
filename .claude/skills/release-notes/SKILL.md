   ---
   name: release-notes
   description: Use when the user asks for release notes or a changelog
     entry generated from commit messages.
   ---

   ## Rules
- Make tone of release notes user-facing; include what changed and why it matters. Example: "The skill now stops to tell user when already-read file is missing, which prevents the skill from running without exclusion filtering."
- Add entries in order of actual book-recs commits.
- Whenever a commit is skipped for any reason, still write a line: SKIP; <reason>. Never omit a line.
- When a skill silently defaults to something, say that a default was applied.
- Format answers like this: "Commit 20 (30aace2): Sentence here." OR "Commit 20 (30aace2): SKIP; <reason>."