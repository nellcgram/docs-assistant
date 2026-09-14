# Changelog

## Run 1 [2026-09-14]
OVERALL: Rubric did not match the skill.

### Commit: 16c67f5, [2026-09-14]
- Fixed: Findings Entry #2 duplicated Entry #3, giving conflicting guidance. Old: Entry #2 restated Entry #3. New: Deleted Entry #2 and renumbered the remaining entries.

### Commit: a59fc9d, [2026-09-14] - Rubric criteria
- Fixed: The skill had no rule against checking other repos to verify commit hashes, letting the model "correct" the user's data. New: "Do not check other repos for the commit hashes; use only the raw commits the user gives you."
- Fixed: The skill had no rule requiring one consistent tense across release notes. New: "Write all release notes in the past tense only."
- Fixed: The skill had no rule barring internal file names in release notes. New: "Do not use internal file names (for example skill, rubric, eval, findings) in release notes."
- Fixed: The skip rule gave two contradicting requirements, and the model followed the wrong one (writing a SKIP line). Old: "Skip a commit if a user of the book recommender would never notice the change. Whenever a commit is skipped for any reason, still write a line: SKIP; <reason>. Never omit a line." New: "Skip a commit if a user of the book recommender would never notice the change. Do not add an entry for that commit."
- Fixed: The format instruction still described a SKIP line that no longer applies. Old: "Format answers like this: "Commit 20 (30aace2): Sentence here." OR "Commit 20 (30aace2): SKIP; <reason>."" New: "Format answers like this: "Commit 20 (30aace2): Sentence here.""