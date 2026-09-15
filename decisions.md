# Decisions

## [2026-09-15] — Run 5 confirmed the Run 4 fixes hold; skill and rubric left unchanged
**Decision:** Made no further edits to SKILL.md or evals/rubric.md after Run 5 scored 7/7 on the Version 2 criteria — the repo-check stop condition and the portfolio/eval/meta skip rule added after Run 4 both held on a fresh session re-run of the same 20 test-case commits.

**Why:** Run 4 had scored well on its own rubric but still turned out to need a rule fix afterward (the stop-condition gap wasn't caught by grading). Run 5 exists to re-test the same commits against the tightened rules before treating the skill as stable, rather than trusting Run 4's score alone.

**Status:** Logged in CHANGELOG.md under Run 5. evals/runs/run-05.md and run-05-output.md hold the grading and output.

## [2026-09-14 9:05 PM] — Portfolio-site and eval/project-meta commits are skipped regardless of visibility
**Decision:** Reinstated a project-scope skip condition: a commit is skipped if it's a portfolio-site, eval, or project-meta change even when its effect is visible to someone — a portfolio visitor is not a user of the book-recommendation skill. Added a worked "meta example" alongside the existing "technical example" so the rule isn't just a stated principle.

**Why:** The 2026-09-12 6:06 PM decision below dropped an earlier project-scope rule as redundant with the general visibility check, assuming portfolio/eval commits would always fail that check on their own. Run 4 disproved this — "Take Book Recommendations project offline," "Removed agentic AI section from portfolio site," and "Move run-01 results into docs so it publishes to the site" all passed the visibility check and were wrongly written up as release notes for the book-recommendation skill.

**Status:** Applied to SKILL.md rule 4 and evals/rubric.md criterion 3 (commits a04b71b, 2b85564, bc6eef7, 60a077a). Logged in CHANGELOG.md. Open item: the worked example only covers the portfolio-page case; "took the whole skill offline" and "published eval results to the site" are still ambiguous and not yet covered by an example.

## [2026-09-14 8:49 PM] — Repo-check rule needed a stop condition, not just permission to check
**Decision:** Tightened skill rule 3 so it only checks a repo already known in context, never searches the filesystem or guesses at repo locations, and marks the commit unverifiable if not immediately accessible. Matching rubric criterion 6 now grades for this stop condition explicitly, not just conflict-flagging.

**Why:** Run 4 scored 7/7 on the existing rubric, but the underlying behavior was wrong: once repo-checking was allowed (Run 4's earlier repo-check rule), the model kept trying to locate a repo instead of falling back to unverifiable when none was accessible — the test-case hashes are synthetic and don't resolve to a real repo. The rubric's "Unverifiable" outcome already existed for this case, but nothing in the skill told the model to stop and land there.

**Status:** Applied to SKILL.md rule 3 and evals/rubric.md criterion 6 (commits a04b71b, 2b85564, bc6eef7). Logged in CHANGELOG.md.

## [2026-09-14 <6:35 PM>] — Commit #1's input wording was fixed after landing on it by mistake meant for #19
**Decision:** Restored evals/cases/release-notes-20.md commit #1's description to describe its own real change (specifying the exact heading to look for in the already-read file) instead of the #19-shaped wording it had picked up.

**Why:** The 2:50 PM edit intended for commits #4 and #19 landed on #1 instead of #19 in its first pass; #19 was then separately and correctly rewritten in the next commit to nearly the same content, so #1 and #19 ended up as near-duplicates in the current release-notes-20.md. Caught before Run 4 used the file.

**Status:** Applied to evals/cases/release-notes-20.md; logged in CHANGELOG.md under Run 4. Checked evals/gold/release-notes.md, evals/cases/raw-commits.md, and evals/runs/run-01 through run-03 output files for the same problem — none needed changes.

## [2026-09-14 6:06 PM] — Version 1 rubric must stay exactly as graded, not get retroactive fixes
**Decision:** Restored evals/rubric.md's "Version 1 (Runs 1-3)" section to the original wording actually used to grade those runs — reverted criterion 4 to "Are developer-facing commits correctly skipped (no note at all)?" (no example) and removed criterion 7 (mechanism/outcome), since neither existed in that form when Runs 1-3 were graded.

**Why:** After splitting the rubric into Version 1/Version 2, the Version 1 section had been overwritten with Version 2's improved wording (skip-rule example, mechanism/outcome criterion). That makes old findings citing criterion numbers (e.g. "Criterion 4 failed") misleading — a reader would assume the improved criteria applied at grading time when they didn't.

**Status:** Applied to evals/rubric.md.

## [2026-09-14 <2:50 PM>] — Fixing the skill won't add missing detail
**Decision:** I decided to change the input commit list, not the skill rules.

**Why:** I had already tried changing the skill rules between versions 1, 2, and 3 with imprecise wording resulting. I talked to Claude and realized because I was not asking the skill to check actual commits (only using user input), the skill lacked context Git normally gave it, so it needed better input to run on specifically for commits 4 and 19. 

**Status:** Applied edits to release-notes-20.md for commits 4 and 19; gold file reconciled 2026-09-14 6:06 PM.

## [2026-09-14 2:28 PM] — Skip rule depends on visible effect, not how technical a commit sounds
**Decision:** Commit 19 (a pre-run check against the already-read-books file) should not have been skipped, even though its description sounds like an internal implementation detail — it changes which books the recommender shows the user.

**Why:** Run 3 findings showed this commit was wrongly marked skip. The skip rule is about whether the *effect* is visible to the user, not about whether the commit's own description uses technical-sounding language.

**Status:** Logged in evals/findings.md (Run 3). Logged to skill and rubric.

## [2026-09-14 2:28 PM] — A technically-accurate release note that omits the specific outcome still fails
**Decision:** A release note counts as a failure if it's vaguely accurate but drops the specific mechanism or outcome of the commit (for example, describing "adjusted when it asked" without saying what default was applied), not only if it's factually wrong.

**Why:** Three commits in Run 3 went through two rounds of revision and were still judged too imprecise compared to the actual commit — the model kept generalizing away the specific default or check that made the note useful.

**Status:** Logged in evals/findings.md (Run 3). Logged in skill. Logged in rubric.

## [2026-09-14 1:31 PM] — Broadened "don't check other repos" to "don't check any repo"
**Decision:** Rewrote the rule from "Do not check other repos for the release notes commit hashes; use only the raw commits the user gives you" to "Do not check any repo for commits before generating release notes. Use only the input the user gives you to generate release notes."

**Why:** Run 2 showed the model still tried to look up the commits itself even under the narrower wording from Run 1.

**Status:** Applied to SKILL.md; logged in CHANGELOG.md under Run 2.

## [2026-09-14 12:06 PM] — Changelog entries must quote the exact old/new rule text and cite a commit hash
**Decision:** Rewrote CHANGELOG.md so each entry is grouped under the commit hash that made the change and states the literal before/after rule wording, instead of being grouped loosely by run number with paraphrased summaries.

**Why:** A paraphrased changelog entry can't be checked against what the rule actually said before and after; quoting the exact text makes each fix verifiable.

**Status:** Applied to CHANGELOG.md; used as the format for all later changelog entries.

## [2026-09-14 11:54 AM] — Skill does one job (release notes); changelog is tracked by hand, separately
**Decision:** Removed the "Rules for changelog" section that had been added to SKILL.md and reverted its description to mention only release notes. The skill generates release notes only; changelog entries documenting the skill's own edits are written directly into CHANGELOG.md, not generated by the skill.

**Why:** Loading both release-note rules and changelog rules into one skill made it unclear which rule set a given run was actually following, and complicated grading. Splitting them keeps the skill's job — and its evaluation — to one thing.

**Status:** Applied to SKILL.md and CHANGELOG.md.

## [2026-09-14 11:31 AM] — Skipped commits get no entry at all, not a SKIP line (reverses 2026-09-12 4:35 PM decision below)
**Decision:** Changed the skill's skip rule and format rule so a skipped commit produces no output at all, removing the earlier "SKIP; <reason>" line requirement.

**Why:** Run 1 grading showed the rubric's actual requirement was "no note at all" for developer-facing commits. The SKILL.md skip rule and the rubric contradicted each other, and the model followed the skill's SKIP-line instruction correctly but still failed the rubric criterion. The SKIP-line was useful while hand-writing gold answers but is wrong for what the shipped skill should output.

**Status:** Applied to SKILL.md. Supersedes the 2026-09-12 4:35 PM decision below (kept for history).

## [2026-09-14 11:31 AM] — Added rules for tense, internal file names, and checking other repos
**Decision:** Added three new SKILL.md rules: write all release notes in past tense only; never use internal file names (skill, rubric, eval, findings) in release notes; don't check other repos to verify commit hashes, use only what the user provides.

**Why:** Run 1 found the model mixed tenses, referenced internal file names, and stopped mid-run to ask about looking up commits elsewhere — none of these were forbidden by the skill at the time.

**Status:** Applied to SKILL.md.

## [2026-09-14 10:13 AM] — Numbered the rubric criteria
**Decision:** Changed evals/rubric.md from bulleted criteria to a numbered list.

**Why:** Numbering lets findings reference a specific criterion by number (e.g., "Criterion 4 failed") instead of restating it each time.

**Status:** Applied to evals/rubric.md; used throughout Run 1-3 findings.

## [2026-09-12 6:06 PM] — Project-scope skip rule dropped as redundant; skip conditions consolidated
**Decision:** A rule limiting release notes to book-recommendations-assistant commits only (added 5:26 PM) was removed about 18 minutes later; the "skip if a user of the book recommender would never notice" condition and the "always write a SKIP line" requirement were merged back into one combined skip rule, and the ordering rule was generalized from "book-recs commits" to "input commits."

**Why:** The project-scope rule was redundant — a commit from the portfolio site or eval project is already something a book-recommender user would never notice, so the general skip condition already covered it.

**Status:** Applied to SKILL.md across three edits (4bff7ca added the scope rule, 46f8733 removed it and merged skip conditions, b2810f4 restored the "would never notice" wording alongside the SKIP-line rule).

## [2026-09-12 5:25 PM] — Standardized how commits are cited in release notes
**Decision:** Reformatted commit citations from "#4 5da846a - sentence" to "Commit 4 (5da846a): sentence."

**Why:** Needed one consistent citation format before generating and grading multiple release-note runs.

**Status:** Applied to evals/gold/release-notes.md; encoded the next day as the "Format answers like this" rule in SKILL.md.

## [2026-09-12 5:08 PM] — Silent defaults must be stated explicitly
**Decision:** Added a skill rule: "When a skill silently defaults to something, say that a default was applied."

**Why:** A default applied without being called out is indistinguishable from a bug or a lucky guess — for example, the recommender falling back to the contemporary genre when no genre was given needs to say so, not just act on it.

**Status:** Applied to SKILL.md from its first draft; carried through all later revisions and reinforced by the 2026-09-14 2:28 PM decision above on commit 4.

## [2026-09-12 4:43 PM] — Skip developer-facing commits from release notes
**Decision:** Commits that only touch internal files (eval templates, example lists, moved-but-not-changed content) are excluded from
release notes entirely — not given a note explaining the skip, just absent.

**Why:** While hand-writing gold answers, two commits (adding example entries to already-read-example.md, moving a rubric into the evals folder) had no effect a user of the skill would ever see. Writing a release note for either would describe a change that doesn't exist from the reader's side.

**Status:** Applied in gold answers for cases #18 and #20. Written into SKILL.md as the skip rule.

## [2026-09-12 4:35 PM] — Commits that produce no release notes are "skip"
**Decision:** For a commit that should produce no release note, the correct gold answer is SKIP plus a one-line reason, not omitting the line. 

**Why:** This matters for scoring: an absent line and a "verified-no-note-needed" line would otherwise look identical to a grader.

**Status:** Corrected evals/gold/release-notes.md to include why skipping commits.

## [2026-09-12 4:20 PM] — 
**Decision:** Release notes voice should tell user what changed and why, not give technical details such as skill edits.

**Why:** These are user-facing, not developer-facing.

**Status:** Rewrote release-notes.md to correct voice across all entries.