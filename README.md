# Docs Assistant

An agent skill that turns raw git commit messages into user-facing release notes, built and tested with Claude Code.

## Structure

- `.claude/skills/release-notes/` — the skill instructions
- `evals/cases/` — test cases (raw commits, selected for testing)
- `evals/gold/` — hand-written correct answers for a few cases
- `evals/rubric.md` — how output is scored
- `evals/runs/` — saved outputs from each test run
- `evals/findings.md` — diagnosis of what went wrong and why
- `shared/` — rules used by more than one skill
- `tools/` — descriptions of tools the skill can use
- `CHANGELOG.md` — record of changes to the skill, with reasons
- `decisions.md` — why the project is structured this way