# Trigger Test: 20 Prompts

Draft for Phase 7's trigger-accuracy test: does the right skill fire for a given prompt, independent of whether its output is good?

The release-notes prompts given below each deliberately repeat the full 20-commit list inline instead of pointing at `evals/cases/release-notes-20.md` by name. A prompt that only references a filename tests whether Claude reads a file and figures out what to do with it, which isn't the same question as whether a given phrase reliably triggers the skill. Keeping each prompt self-contained isolates the thing this test is actually for.

## create release notes using these commits; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## write release notes for all commits here; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## write notes for these; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## fix my commits; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## get release notes from these; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## apply review of these commits; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## using these commits create release notes; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## write release notes for the commits listed; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## make release notes using this; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## add release notes for the commits; expected: release-notes skill
1. 3087743 Added sentence to skill specifying the exact heading to look for in the already-read file
2. 2d10267 Fix skill format "other bks by author" line
3. 06d7e80 edited changelog to describe skill live user edit
4. 5da846a adjusted skill wording to default to contemporary genre and tell user
5. 32c3bb8 Edited changelog
6. 1e3c29b Edited skill "what it does" to be accurate
7. 6217927 Edited skill formatting
8. 3c8eb5b Deleted "other bks by author" note in skill, unnecessarily complicated
9. b682575 reworded guardianship rubric again
10. ec87a17 Edited changelog and skill language
11. 1ac826a Regrade Run 1 with an independent session, fix rubric gap it exposed
12. 6fce484 Take Book Recommendations project offline
13. 78dcb74 Fix case study inconsistencies: rescore Run 1, clarify verification, naming, and terminology
14. f21345d Removed agentic AI section from portfolio site
15. 2cce803 Updated README
16. 8a39d5e Move run-01 results into docs so it publishes to the site
17. 0853964 added note on repo history to README
18. b50af03 fixed already read example file
19. b971722 Edited skill to check already-read.md before running so won't reproduce read books
20. f244f58 moved rubric to eval file

## All 5 should trigger doc-review skill
1. Review this doc using checklist - Expected: doc-review skill
2. Use checklist on this doc - Expected: doc-review skill
3. review this document - Expected: doc-review skill
4. review this doc with the checklist - Expected: doc-review skill
5. go over doc using checklist - Expected: doc-review skill

## All 5 should trigger neither skill
1. go over this doc - Expected: neither
2. summarize this email - Expected: neither
3. make this paragraph into a bullet-pointed list - Expected: neither
4. summarize these pages in 1 paragraph - Expected: neither
5. make this document into a found poem - Expected: neither
