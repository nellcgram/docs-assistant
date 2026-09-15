# Changelog

## Run 4
### Commit: ?, [2026-09-14] - Rewrote repo-check rule to allow verification
- Fixed: Skill forbade checking any repo, which was only ever needed to keep eval test cases reproducible, not a real production requirement. Old: "Do not check any repo for commits before generating release notes. Use only the input the user gives you to generate release notes." New: "When a commit hash is given and the repo is accessible, check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct."

### Commit: ?, [2026-09-14] - Added worked example to skip rule
- Fixed: Skip rule stated the principle (judge by visible effect, not technical-sounding wording) but gave no example, despite commit 19 already having been wrongly skipped for this exact reason in Run 3. Added: "Example: A commit adding \"a pre-run check against the already-read-books file\" sounds like internal implementation detail, but it changes which books the recommender shows; include it, don't skip it."

### Commit: ?, [2026-09-14] - Rubric: retired repo-check criterion, added conflict-flag criterion, versioned the file
- Fixed: Criterion 1 (never check repos) contradicted the new repo-check rule above. Split evals/rubric.md into "Version 1 (Runs 1-3)," preserved exactly as originally graded, and "Version 2 (Run 4-on)," which drops criterion 1 and adds: "When the commit hash and provided description conflict, did it flag the discrepancy instead of silently resolving it one way or the other?"

### Commit: ?, [2026-09-14] - Replaced real commit hashes with synthetic ones across eval files
- Fixed: Eval test cases used real hashes from real past commits (this repo's own history) that Claude could look up directly, undermining the eval's controlled input. Replaced all 20 test-case hashes with synthetic, non-resolvable ones, consistently across evals/cases/, evals/gold/, evals/runs/, and SKILL.md's format example.

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