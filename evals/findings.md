# Findings
Below are the reasons why ouputs failed, grouped by what numbers matched each result.

## Run 2
For all entries
1. Criterion 1 failed because the prompt did not specify "do not look up the commits." The AI wanted to look up the actual commits for release notes, not use the input I gave it.
2. Criterion 6 was unverifiable since there were no fallbacks or defaults applied.

## Run 1 [2026-09-14]

### Entry 1: Commits 1 and 8
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed and there was no fallback or default mentioned so Criterion 6 was unverifiable. Criterion 4 was unverifiable since this was not a developer-facing commit.

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.

### Entry 2: Commits 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 17, 18, 20
 What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note and no fallback or default mentioned so Criterion 3 passed and Criterion 6 was unverifiable. 
Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results. Criterion 4 did not match the skill: the skill says "skip" and also "Whenever a commit is skipped for any reason, still write a line: SKIP," so results followed the skill and wrote the line but failed the overall skip criterion.

### Entry 3: Commit 12
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed. Criterion 4 was unverifiable since this was not a developer-facing commit. Criterion 5 did not apply (no internal files involved). There was no fallback or default mentioned so Criterion 6 was unverifiable.

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.

### Entry 4: Commit 14
What went wrong: User stopped the AI after it tried to find the commit hashes in another repo, and had to re-write the prompt to say "only use these commits" (Criterion 1).
Entry was not in past tense (Criterion 2) and used internal file names (Criterion 3). There was exactly 1 release note so Criterion 3 passed. Criterion 4 did not match the skill: the skill says "skip" and also "Whenever a commit is skipped for any reason, still write a line: SKIP," so results followed the skill and wrote the line but failed the overall skip criterion. Criterion 5 did not apply (no internal files involved). There was no fallback or default mentioned so Criterion 6 was unverifiable

Skill lack of clarity: The skill did not forbid the AI from checking other repos; it did not request the answer be in past tense; it did not forbid use of internal file names in results.