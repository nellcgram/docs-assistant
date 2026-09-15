# Findings
Below are the reasons why ouputs failed, grouped by what numbers matched each result.

## Run 6 [2026-09-15]
Run 6 was run as 20 separate single-commit cases (evals/runs/run-06/case-01.md through case-20.md) instead of one batched 20-commit conversation like Run 5. Three failure modes showed up that Run 5 did not have:

### Several commits got no answer at all
Commits 2 (2d10267), 6 (1e3c29b), 10 (ec87a17), 12 (6fce484), and 18 (b50af03) produced neither a release note nor a skip decision — the response stopped and asked the user to supply more detail or pick between readings instead of doing what Runs 1-5 did (make the call from the description given). For example, commit 12 ends with "Tell me which reading is correct (or point me at the repo), and I'll finalize or drop the entry," and commit 10 ends with "Rather than guess, could you either confirm the repo location... or tell me what the skill-language edit changed." The skill's "unverifiable" outcome was meant to mark a release note that can't be confirmed against the repo, not license to stop and ask instead of landing on skip-or-write.

### Skipped commits still resulted in full write-up files, not "no entry"
Nearly every commit correctly identified as skippable (3, 5, 7, 9, 11, 13, 14, 15, 16, 17, 20) still generated a multi-paragraph file restating the skip rule, flagging unverifiability, and inviting the user to override the call — instead of "no entry," which is what the skip rule says and what Run 5 actually did (one line: "Skipped (no visible effect...): 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20"). No single rubric criterion scores this directly, but it's a sharp behavior regression from Run 5.

### Many responses were not in past tense
The release notes themselves (commits 1, 4, 8, 19) stayed in past tense and were fine. The skip explanations and clarifying-question responses were written in present tense throughout — e.g., commit 3: "Editing the changelog is a project-meta change. It doesn't alter..."; commit 16: "Moving run-01 results into docs so it publishes to the site affects..."; commit 7: "'Edited skill formatting' describes a change... Nothing... points to...". The past-tense rule was written with release notes in mind and doesn't obviously cover this new category of skip/clarification prose.

### Likely cause, not yet confirmed
Run 5's single batched pass made a judgment call on every ambiguous commit and flagged only one (commit 18) as uncertain. Running each commit as its own isolated case seems to have pushed the model toward hedging and asking rather than deciding, with no other commit's context to calibrate against. Worth re-running Run 6 batched, the way Run 5 was, before deciding whether this is a skill-wording gap or an artifact of the isolated-case format.

Commits 1, 4, 8, and 19 were acceptable. 

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