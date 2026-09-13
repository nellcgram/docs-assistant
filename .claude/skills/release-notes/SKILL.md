   ---
   name: release-notes
   description: Use when the user asks for release notes or a changelog
     entry generated from commit messages.
   ---

   ## Rules
- Make tone of release notes user-facing; include what changed and why it matters. Example: "The skill now stops to tell user when already-read file is missing, which prevents the skill from running without exclusion filtering."
- Add entries in order of actual book-recs commits.
- Skip a commit if a user of the book recommender would never notice the change.
- When a skill silently defaults to something, say that a default was applied.
- Only write release notes for commits about the book-recommendations assistant. If a commit is about the portfolio website, the docs-assistant eval project, or anything else, skip it entirely, including no note.
- Format answers like this: "Commit 20 (30aace2): Sentence here."