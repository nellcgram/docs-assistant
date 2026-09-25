#!/usr/bin/env python3
"""Call the release-notes skill once per commit case, saving each response separately.

Runs the 20 commit cases into evals/runs/<name>/ (or rep-01/ through rep-NN/
with --repeats). The script never overwrites an existing response file, so
give each run a new --name.
"""

import argparse
import re
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / ".claude/skills/release-notes/SKILL.md"
SHARED_PATHS = [ROOT / "shared/house-style.md", ROOT / "shared/hard-surfaces.md"]
CASES_PATH = ROOT / "evals/cases/release-notes-20.md"
RUNS_DIR = ROOT / "evals/runs"

CASE_LINE_RE = re.compile(r"^\d+\.\s+\S+\s+.+$")


def load_cases(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text().splitlines()
        if CASE_LINE_RE.match(line.strip())
    ]


def load_system_prompt() -> str:
    """SKILL.md plus the shared files it points to. The API sees only this string."""
    text = SKILL_PATH.read_text()
    for path in SHARED_PATHS:
        text += f"\n\n# Contents of {path.relative_to(ROOT)}\n\n{path.read_text()}"
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="output folder under evals/runs/, e.g. run-13")
    parser.add_argument(
        "--repeats",
        type=int,
        default=1,
        help="number of times to run each case (default: 1)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    system_prompt = load_system_prompt()
    cases = load_cases(CASES_PATH)
    output_dir = RUNS_DIR / args.name

    def out_path_for(rep: int, index: int) -> Path:
        rep_dir = output_dir / f"rep-{rep:02d}" if args.repeats > 1 else output_dir
        return rep_dir / f"case-{index:02d}.md"

    existing = [
        out_path_for(rep, i)
        for rep in range(1, args.repeats + 1)
        for i in range(1, len(cases) + 1)
        if out_path_for(rep, i).exists()
    ]
    if existing:
        raise SystemExit(
            f"Refusing to overwrite {len(existing)} existing file(s), for example "
            f"{existing[0].relative_to(ROOT)}. Pick a new --name."
        )

    client = anthropic.Anthropic()

    for rep in range(1, args.repeats + 1):
        for i, case in enumerate(cases, start=1):
            out_path = out_path_for(rep, i)
            out_path.parent.mkdir(parents=True, exist_ok=True)

            response = client.beta.messages.create(
                model="claude-opus-5",
                max_tokens=16000,
                thinking={"type": "adaptive"},
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": f"Write release notes for this commit:\n\n{case}",
                    }
                ],
            )

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
