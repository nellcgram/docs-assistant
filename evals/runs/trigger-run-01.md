# Trigger Run 1

- These are the prompts used in trigger-set-20.md. For every prompt, the commits from release-notes-20.md or the doc(s) to evaluate were included.
- Results include grades, as in correct skill fired.

## Should trigger release notes skill
1. create release notes using these commits - correct skill
2. write release notes for all commits here - correct skill
3. write notes for these - correct skill
4. fix my commits — none of them work; agent asks what I want done with the commits and using a skill is not an option given
5. get release notes from these - correct skill
6. apply review of these commits - neither skill fires; code-review skill fires instead
7. using these commits create release notes - correct skill
8. write release notes for the commits listed - correct skill
9. make release notes using this - correct skill
10. add release notes for the commits - correct skill

**Subtotal:** Expected 10 of 10; reality was 8 of 10

## Should trigger `doc-review` (5 phrasings)
1. read doc using checklist - C
2. Use checklist on this doc - C
3. review this document - C
4. review this doc with the checklist - C
5. go over doc using checklist - C

**Subtotal:** Expected 5 of 5; got 5 of 5

## Should trigger neither (5 phrasings)
1. go over this doc
2. summarize this email
3. make this paragraph into a bullet-pointed list
4. summarize these pages in 1 paragraph
5. make this document into a found poem
**Subtotal:** Expected 5 of 5; got 5 of 5

**TOTAL:** 18 of 20 correct