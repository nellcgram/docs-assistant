# Changelog

## Run 3 
### Commit: c503947, [2026-09-14] - Fixed original input for commit #19 (b971722) release-notes-20.md
-Fixed: For Commit #19 b971722, changed release-notes.md because only making the original input more precise would add enough detail to results. Old: "Added instruction to skill, check before running section." New: "Edited skill to check already-read.md before running so won't reproduce read books."

### Commit: ceb3cc8, [2026-09-14] - Fixed original input for commit #4 (5da846a) release-notes-20.md
-Fixed: For Commit #4 5da846a, changed release-notes.md because only making the original input more precise would add enough detail to results. Old: "Edited skill format about user being there to ask which genre." New: "Adjusted skill wording to default to contemporary genre and tell user."

## Run 2
### Commit: 4dc4c81, [2026-09-14] - Rewrote checking repos rule
- Fixed: Rewrote rule telling AI not to check repos for commits. Old: "Do not check other repos for the release notes commit hashes; use only the raw commits the user gives you." New: "Do not check any repo for commits before generating release notes. Use only the input the user gives you to generate release notes."

## Run 1 [2026-09-14]
OVERALL: Rubric did not match the skill.

### Commit: 16c67f5, [2026-09-14] - Duplicate entry
- Fixed: Findings Entry #2 duplicated Entry #3, giving conflicting guidance. Old: Entry #2 restated Entry #3. New: Deleted Entry #2 and renumbered the remaining entries.

### Commit: a59fc9d, [2026-09-14] - Rubric criteria
- Fixed: The skill had no rule against checking other repos to verify commit hashes, letting the model "correct" the user's data. New: "Do not check other repos for the commit hashes; use only the raw commits the user gives you."
- Fixed: The skill had no rule requiring one consistent tense across release notes. New: "Write all release notes in the past tense only."
- Fixed: The skill had no rule barring internal file names in release notes. New: "Do not use internal file names (for example skill, rubric, eval, findings) in release notes."
- Fixed: The skip rule gave two contradicting requirements, and the model followed the wrong one (writing a SKIP line). Old: "Skip a commit if a user of the book recommender would never notice the change. Whenever a commit is skipped for any reason, still write a line: SKIP; <reason>. Never omit a line." New: "Skip a commit if a user of the book recommender would never notice the change. Do not add an entry for that commit."
- Fixed: The format instruction still described a SKIP line that no longer applies. Old: "Format answers like this: "Commit 20 (f244f58): Sentence here." OR "Commit 20 (f244f58): SKIP; <reason>."" New: "Format answers like this: "Commit 20 (f244f58): Sentence here.""