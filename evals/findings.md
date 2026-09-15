# Findings
Below are the reasons why ouputs failed, grouped by what numbers matched each result.

## Run 4 [2026-09-14]
## For all entries:
- Criterion 3 was originally graded Pass, which was wrong: the response wrote release notes for commits 12 (6fce484, "Take Book Recommendations project offline"), 14 (f21345d, "Removed agentic AI section from portfolio site"), and 16 (8a39d5e, "Move run-01 results into docs so it publishes to the site") — all portfolio-site/project-meta changes that a book-recommendation skill user would never see. The rubric at the time only checked visibility to "the user," and these commits are visible to a portfolio site visitor, so they slipped through grading. This was found afterward, not caught by the original grading pass, and is why the skip rule and rubric criterion 3 were rewritten to skip portfolio/eval/project-meta commits regardless of visibility, with a worked meta example added. run-04.md has since been corrected to Criterion 3: Fail.
- Criterion 6 was marked Unverifiable because this run's own prompt told the model not to check any repo, so no verification was attempted either way. Separately (not from this run's grading), it was later found that the repo-check rule itself had no stop condition — once repo-checking was allowed, the model could keep searching for a repo instead of falling back to unverifiable when none was accessible. That gap was fixed afterward even though nothing in Run 4 exercised or caught it directly.
- The grading summary line originally read "Passed every criteria: 7 of 7," which contradicted its own breakdown (Criterion 6: Unverifiable, and, per the point above, Criterion 3 should have read Fail). After the criteria were corrected, the summary line itself still needed fixing — it briefly read "0 of 8" (Version 2 has 7 criteria, not 8, and the project's convention for a run that doesn't pass everything is the single-letter "O," not a fraction, per run-01.md and run-02.md). Corrected to "O."

Commits 1, 2, 4, 8, and 19 were acceptable.

## Run 3 [2026-09-14]
## For all entries:
- Criterion 4 failed because it removed commit #19 which was still user-facing, not developer-facing.

- Across 2 commits, the language is less precise than the actual commits:
 1. Commit 4 (5da846a)
- V1: It was marked skip in version 1 but it should not have been
- V2 Revised too vaguely: "Clarified that the recommender asked which genre when a user was present to answer."
- V3 revised less vaguely but missing information: "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond"
- It should say: "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."

 Commit 19 (b971722)
 - V1 Original: "The skill now checks the already-read file before running, so it won't proceed without applying exclusion filtering."
- Revised V2: "Commit 19 (b971722): Added a check that ran before the recommender started, so it stopped and told the user if something needed was missing."
- Revised V3: Skipped completely.
- It should say: "Checked the file of already read books before running, so the result won't produce books the user has already read."

Commit 1, 4, 8, 12 were acceptable.

## Run 2 [2026-09-14]
## For all entries:
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