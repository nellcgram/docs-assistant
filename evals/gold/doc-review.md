# Doc Review Gold

Hand-written findings for `evals/cases/doc-review-3.md`. Each case is a snapshot of a file as it stood when I reviewed it, so the current files differ. A response should raise the findings below, and the rule numbers refer to the doc-review skill's checklist as it stood in Case 2.

## Case 1: README

**Issues:**
- The Structure list omits `scripts/` (which holds the eval runner) and `case-study.md`.
- The Structure descriptions are sentence fragments. They should be full sentences (rule 2).
- `decisions.md` should not be listed. It is an engineering log, and the README is for the case study.

**Missing:**
- How to run evals: the command that runs the eval harness, and how grading works (some criteria are graded mechanically, others by human judgment).
- Requirements and setup: the API key and the Claude Code version the project assumes.

The opening line states the purpose, so rule 1 passes.

## Case 2: Skill

**Issues:**
- The Purpose section is unnecessary. It only says the agent should check each rule, which the Rules section already says.
- "Say pass, fail, or unverifiable" repeats in all seven rules. It should appear once, above the list.
- Rule 7 contradicts itself. It says not to mark an inapplicable item as fail, then lists fail as an option again. It should name the outcome for an inapplicable rule.
- Rule 2 bundles two checks (active voice, full sentences), so one outcome cannot report both.
- Rule 5 cannot be verified without running the links and code. It should expect "unverifiable" when the reviewer cannot run them.

## Case 3: Decisions

**Issues:**
- This entry is engineering-log detail and needs shortening for the case study. It should keep the decision, the reason, and the status.
- It should cut the run numbers, commit hashes, script name, and the list of failing commits.
- It should drop the first-person "I" and the passive "until it's confirmed" for plain active statements.
