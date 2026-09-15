# Rubric
Important: After Version 1 runs 1-3, criterion 1 was deleted so runs 4-on use Version 2

## Criteria Version 2 (Run 4-on):
1. Is the response in past tense?
Outcomes: Pass, fail, unverifiable

2. Is there exactly one release note per non-skipped commit?
Outcomes: Pass, fail unverifiable

3. Are commits skipped when they're portfolio-site, eval, or project-meta changes (regardless of their visibility), or when their effect is not visible to the user of the books-recommendation skill, and never skipped only because the commit's own description sounds technical or internal?
- Technical example: a commit described as "added a pre-run check against the already-read-books file" sounds like internal details, but it changes which books the user is shown. Skipping it fails this criterion even though the wording sounds developer-facing.
- Meta example: a commit described as "Removed agentic AI section from portfolio site" is a project meta-change that can be skipped.
Outcomes: Pass, fail, unverifiable

4. Does it avoid naming internal filenames (SKILL.md, rubric.md, etc.)?
Outcomes: Pass, fail, unverifiable

5. Is a fallback or default explained when one applies?
Outcomes: Pass, fail, unverifiable

6. When the commit hash and provided description conflict, did it flag the discrepancy instead of silently resolving it? When the repo/commit couldn't be found, did it stop and mark unverifiable instead of continuing to search?
Outcomes: Pass, fail, unverifiable

7. Is the release note both factually correct AND includes the specific mechanism or outcome 
- Example: Vague (fails): "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond."
- Specific (passes): "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."
Outcomes: Pass, fail, unverifiable


## Criteria Version 1 (Runs 1-3) — preserved exactly as graded, do not edit:
Important: #1 RETIRED for Run 04 onward; see decisions.md

1. Did it run through the skill without interrupting for user feedback (for ex. asking if I wanted to find the commits in another repo)
Outcomes: Pass, fail, unverifiable

2. Is the response in past tense?
Outcomes: Pass, fail, unverifiable

3. Is there exactly one release note per non-skipped commit?
Outcomes: Pass, fail, unverifiable

4. Are developer-facing commits correctly skipped (no note at all)?
Outcomes: Pass, fail, unverifiable

5. Does it avoid naming internal filenames (SKILL.md, rubric.md, etc.)?
Outcomes: Pass, fail, unverifiable

6. Is a fallback or default explained when one applies?
Unverifiable
Outcomes: Pass, fail, unverifiable