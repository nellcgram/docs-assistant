# Decisions

## [2026-09-12 4:43 PM] — Skip developer-facing commits from release notes
**Decision:** Commits that only touch internal files (eval templates, example lists, moved-but-not-changed content) are excluded from
release notes entirely — not given a note explaining the skip, just absent.

**Why:** While hand-writing gold answers, two commits (adding example entries to already-read-example.md, moving a rubric into the evals folder) had no effect a user of the skill would ever see. Writing a release note for either would describe a change that doesn't exist from the reader's side.

**Status:** Applied in gold answers for cases #18 and #20. Not yet written into SKILL.md. That happens when the spec is drafted in Phase 2.

## [2026-09-12 4:35 PM] — Commits that produce no release notes are "skip"
**Decision:** For a commit that should produce no release note, the correct gold answer is SKIP plus a one-line reason, not omitting the line. 

**Why:** This matters for scoring: an absent line and a "verified-no-note-needed" line would otherwise look identical to a grader.

**Status:** Corrected evals/gold/release-notes.md to include why skipping commits.

## [2026-09-12 4:20 PM] — 
**Decision:** Release notes voice should tell user what changed and why, not give technical details such as skill edits.

**Why:** These are user-facing, not developer-facing.

**Status:** Rewrote release-notes.md to correct voice across all entries.