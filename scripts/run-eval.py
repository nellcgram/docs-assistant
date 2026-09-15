#!/usr/bin/env python3
"""Call the release-notes skill once per commit case, saving each response separately."""

import re
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / ".claude/skills/release-notes/SKILL.md"
CASES_PATH = ROOT / "evals/cases/release-notes-20.md"
OUTPUT_DIR = ROOT / "evals/runs/v3"

CASE_LINE_RE = re.compile(r"^\d+\.\s+\S+\s+.+$")


def load_cases(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text().splitlines()
        if CASE_LINE_RE.match(line.strip())
    ]


def main() -> None:
    skill_text = SKILL_PATH.read_text()
    cases = load_cases(CASES_PATH)

    client = anthropic.Anthropic()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for i, case in enumerate(cases, start=1):
        response = client.beta.messages.create(
            model="claude-opus-5",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            system=skill_text,
            messages=[
                {
                    "role": "user",
                    "content": f"Write release notes for this commit:\n\n{case}",
                }
            ],
        )

        out_path = OUTPUT_DIR / f"case-{i:02d}.md"

        if response.stop_reason == "refusal":
            out_path.write_text(f"REFUSED: {response.stop_details}\n")
            print(f"case {i:02d}: refused, wrote {out_path.relative_to(ROOT)}")
            continue

        text = "".join(
            block.text for block in response.content if block.type == "text"
        )
        out_path.write_text(text.strip() + "\n")
        print(f"case {i:02d}: wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
