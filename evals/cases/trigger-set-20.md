# Trigger set

## 20 prompts: 10 that should clearly trigger
release-notes, 5 that should trigger doc-review, 5 that should trigger neither.

## Prompts to trigger release notes
1. use the release-notes skill and write release notes for all 20 commits in release-notes-20.md (ran correct skill + a lot of other files + tried to write notes inside files, not chat)
2. write release notes for all commits in release-notes-20.md (ran correct skill)
3. write release notes for release-notes-20.md (triggered trigger-set file, then correct skill)
4. fix my commits in release-notes-20.md (ran correct skill)
5. use release-notes-20.md (ran correct skill but only because it first read trigger-set)
**Matched what I expected:** 3 of 5


## Prompts to trigger doc review
1. Review this doc using doc-review skill
2. Use doc-review skill to review this documentation
3. check this document
ation against checklist
4. Is this doc missing anything?
5. review doc against checklist using doc review
**Matched what I expected:** ? of 5

## Prompts to trigger neither one
1. go over this doc
2. 
