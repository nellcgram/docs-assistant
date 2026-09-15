# Changelog

## Run 4
### Commit: bc6eef7 (builds on a04b71b, 2b85564), [2026-09-14] - Repo-check rule stops and marks unverifiable instead of searching indefinitely
- Fixed: Rule 3 allowed checking a repo but had no stop condition, so the model kept searching for a repo instead of falling back to unverifiable when none was accessible (the test-case hashes are synthetic and don't resolve to a real repo). Old: "When a commit hash is given and the repo is accessible, check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct." New: "When a commit hash is given, try to check the actual commit. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct. Only check the repo if it is known in context; do not search the filesystem or guess at repo locations. If not immediately accessible, mark unverifiable." Matching rubric criterion 6 old: "When the commit hash and provided description conflict, did it flag the discrepancy instead of silently resolving it one way or the other?" New: "When the commit hash and provided description conflict, did it flag the discrepancy instead of silently resolving it? When the repo/commit couldn't be found, did it stop and mark unverifiable instead of continuing to search?"

### Commit: bc6eef7 (builds on a04b71b, 2b85564; formatting in 60a077a), [2026-09-14] - Portfolio-site/eval/meta commits skipped regardless of visibility
- Fixed: Skip rule only checked visibility to a user, so portfolio-site and eval/project commits with an effect visible to a site visitor (not a skill user) were wrongly written up as release notes. Old: "Skip a commit if the effect is not visible to the user. Do not add an entry for that commit. If the commit sounds technical and internal but it changes something for the user, include it. Example: A commit adding \"a pre-run check against the already-read-books file\" sounds like internal implementation detail, but it changes which books the recommender shows; include it, don't skip it." New: "Skip a commit if it's a portfolio-site, eval, or project-meta change, even if it's visible to someone — a portfolio visitor is not a user of the book-recommendation skill. Otherwise, skip a commit if the effect is not visible to a user of the book-recommendation skill. Do not add an entry for either kind of skip. If the commit sounds technical and internal but it changes something for that user, include it. Technical example: A commit adding \"a pre-run check against the already-read-books file\" sounds like an internal implementation detail, but it changes which books the recommender shows; include it, don't skip it. Meta example: a commit described as \"Removed agentic AI section from portfolio site\" is a project meta-change that can be skipped." Matching rubric criterion 3 updated the same way, with both examples added and a "visbility" typo fixed.

### Commit: ?, [2026-09-14] - Fixed original input for commit #1 (3087743) release-notes-20.md
- Fixed: The 15:01 edit meant for commits #4 and #19 landed on #1 instead of #19, giving #1 wording that actually described #19's change. Old: "Added sentence to skill to check already-read books file before running so don't produce read books." New: "Added sentence to skill specifying the exact heading to look for in the already-read file." Checked evals/gold/release-notes.md, evals/cases/raw-commits.md, and evals/runs/run-01 through run-03 for the same issue — none needed changes (gold has no entry for commit 1, raw-commits.md intentionally keeps the original terse message, and the run outputs are historical records of what was produced at the time).

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