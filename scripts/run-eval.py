#!/usr/bin/env python3
"""Call the release-notes skill once per commit case, saving each response separately."""

import argparse
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repeats",
        type=int,
        default=1,
        help="number of times to run each case (default: 1)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    skill_text = SKILL_PATH.read_text()
    cases = load_cases(CASES_PATH)

    client = anthropic.Anthropic()

    for rep in range(1, args.repeats + 1):
        rep_dir = OUTPUT_DIR / f"rep-{rep:02d}" if args.repeats > 1 else OUTPUT_DIR
        rep_dir.mkdir(parents=True, exist_ok=True)

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

            out_path = rep_dir / f"case-{i:02d}.md"

            if response.stop_reason == "refusal":
                out_path.write_text(f"REFUSED: {response.stop_details}\n")
                print(f"rep {rep:02d} case {i:02d}: refused, wrote {out_path.relative_to(ROOT)}")
                continue

            text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            out_path.write_text(text.strip() + "\n")
            print(f"rep {rep:02d} case {i:02d}: wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
