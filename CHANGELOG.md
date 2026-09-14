# Changelog

## Run 1

### Numbers 1 and 8 [2026-09-14]
OVERALL: Rubric did not match the skill.

- Fixed: Missing a rule telling AI not to check other repos for the commit hashes to get 'correct' commit. New: "Do not check other repos for the commit hashes; use only the raw commits the user gives you."

- Fixed: Missing a rule telling AI to give answers in 1 consistent tense. New: " Write all release notes in the past tense only."

- Fixed: Missing a rule telling AI not to use internal file names in release notes. New: "Do not us internal file names (for example skill, rubriv, eval, findings) in release notes."

- Fixed: In Findings, found and deleted  duplicate Entry #2.

- Fixed: The 'skip' rule had 2 contradicting requirements and was followin the second (writing a line describing the skip). Clarified the rule. Old: "Skip a commit if a user of the book recommender would never notice the change. Whenever a commit is skipped for any reason, still write a line: SKIP; <reason>. Never omit a line." New: "Skip a commit if a user of the book recommender would never notice the change. Do not add an entry for that commit."

- Fixed: Deleted half of format requirement because I am no longer including a SKIP reason. Old: "- Format answers like this: "Commit 20 (30aace2): Sentence here." OR "Commit 20 (30aace2): SKIP; <reason>."" New: "- Format answers like this: "Commit 20 (30aace2): Sentence here.""

- Fixed: Added rules for changelog since it is different formatting from release notes and the description of the skill includes both.