#!/usr/bin/env python3
"""Check release-notes eval run outputs against the mechanical rubric criteria.

Only rubric.md's Version 2 criteria 1, 2, 4, and 8 are checked here — the ones
that can be judged from the response text alone, without comparing against the
actual commit content. Criteria 3, 6, and 7 need that kind of judgment call and
are out of scope for this script. Version 1 (runs 1-3) predates these criteria
and isn't checked either.

Every check here is a text heuristic, not a guarantee. Ambiguous cases are
marked "unverifiable" rather than guessed at, matching the rubric's own
Pass/Fail/Unverifiable vocabulary. Treat the output as a first pass to spot
obvious violations, not a replacement for the manual grading in run-NN.md.
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "evals/runs"
CASES_PATH = ROOT / "evals/cases/release-notes-20.md"
OUTPUT_CSV = RUNS_DIR / "mechanical-results.csv"

INTERNAL_FILENAMES = [
    "SKILL.md",
    "rubric.md",
    "decisions.md",
    "changelog.md",
    "findings.md",
    "CLAUDE.md",
    "already-read.md",
]

CLARIFY_PATTERNS = [
    r"let me know",
    r"tell me\b",
    r"could you\b",
    r"please confirm",
    r"confirm the\b",
    r"which reading is correct",
    r"point me at",
    r"rather than guess",
    r"needs your input",
    r"i'd need to know",
    r"paste the diff",
    r"and i'll write",
    r"and i'll finalize",
]

RECONSIDER_PATTERNS = [
    r"i'd reassess",
    r"i'm not confident",
    r"not confident",
    r"before publishing",
    r"if it turns out",
    r"leaves some ambiguity",
    r"possible exception",
]

SKIP_WORD_RE = re.compile(r"\bSKIP\b|\bskipped\b|\bno release note\b|\bno entry\b", re.I)
COMMIT_HEADER_RE = re.compile(r"Commit\s+(\d+)\s*\(([0-9a-fA-F]{5,40})\)")
PRESENT_TENSE_RE = re.compile(
    r"\bis a\b|\bis an\b|\bis the\b|\bdoesn't\b|\bisn't\b|\bdoes\b|\bmeans\b|\baffects\b",
    re.I,
)
GERUND_SENTENCE_RE = re.compile(r"(?:^|[.!?]\s+)([A-Z][a-z]+ing)\b")
RUN_NUMBER_RE = re.compile(r"run-(\d+)")


def get_case_count() -> int:
    lines = CASES_PATH.read_text().splitlines()
    return sum(1 for line in lines if re.match(r"^\d+\.\s+\S+", line.strip()))


def discover_runs() -> dict[str, tuple[str, Path]]:
    """Only runs 4-on use the Version 2 rubric that's tagged mechanical."""
    runs: dict[str, tuple[str, Path]] = {}
    for f in RUNS_DIR.glob("run-*-output.md"):
        name = f.stem.removesuffix("-output")
        runs[name] = ("single", f)
    for d in RUNS_DIR.iterdir():
        if d.is_dir() and d.name.startswith("run-") and any(d.glob("case-*.md")):
            runs[d.name] = ("multi", d)

    def run_num(name: str) -> int:
        m = RUN_NUMBER_RE.search(name)
        return int(m.group(1)) if m else -1

    return dict(sorted((k, v) for k, v in runs.items() if run_num(k) >= 4))


def load_response_text(kind: str, path: Path) -> str:
    if kind == "single":
        text = path.read_text()
        parts = re.split(r"^##\s*Response.*$", text, flags=re.M)
        return parts[-1] if len(parts) > 1 else text
    return "\n\n".join(cf.read_text() for cf in sorted(path.glob("case-*.md")))


def parse_segments(text: str) -> dict[int, list[str]]:
    matches = list(COMMIT_HEADER_RE.finditer(text))
    segments: dict[int, list[str]] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        segments.setdefault(num, []).append(text[start:end])
    return segments


def parse_aggregate_skips(text: str) -> set[int]:
    skips: set[int] = set()
    for line in text.splitlines():
        if re.search(r"\bskip", line, re.I) and ":" in line:
            _, _, tail = line.partition(":")
            skips.update(int(n) for n in re.findall(r"\b(\d{1,2})\b", tail) if 1 <= int(n) <= 20)
    return skips


def has_present_tense_flag(text: str) -> str | None:
    m = PRESENT_TENSE_RE.search(text)
    if m:
        start = max(0, m.start() - 30)
        return text[start : m.end() + 10].strip()
    m = GERUND_SENTENCE_RE.search(text)
    if m:
        start = max(0, m.start() - 5)
        return text[start : m.start() + 40].strip()
    return None


def classify_commits(segments: dict[int, list[str]], aggregate_skips: set[int], case_count: int):
    statuses = {}
    for k in range(1, case_count + 1):
        if k in segments:
            joined = " ".join(segments[k])
            if any(re.search(p, joined, re.I) for p in CLARIFY_PATTERNS):
                status = "asked"
            elif SKIP_WORD_RE.search(joined):
                status = "skipped"
            else:
                status = "written"
            statuses[k] = (status, joined)
        elif k in aggregate_skips:
            statuses[k] = ("skipped", "")
        else:
            statuses[k] = ("missing", "")
    return statuses


def check_criterion_1(statuses: dict, full_text: str) -> tuple[str, str]:
    flags = []
    for k, (status, text) in statuses.items():
        if not text:
            continue
        flag = has_present_tense_flag(text)
        if flag:
            flags.append(f"commit {k}: \"{flag}\"")
    for line in full_text.splitlines():
        if re.match(r"\s*(SKIP|Skipped)\b", line, re.I) and ":" in line:
            flag = has_present_tense_flag(line)
            if flag:
                flags.append(f"aggregate skip line: \"{flag}\"")
    if flags:
        return "Fail", "; ".join(flags[:3])
    return "Pass", ""


def check_criterion_2(statuses: dict, segments: dict) -> tuple[str, str]:
    dup_notes = [k for k, texts in segments.items() if len(texts) > 1]
    missing = [k for k, (status, _) in statuses.items() if status == "missing"]
    if dup_notes:
        return "Fail", f"duplicate entries for commit(s): {dup_notes}"
    if missing:
        return "Unverifiable", f"commit(s) not addressed anywhere: {missing}"
    return "Pass", ""


def check_criterion_4(full_text: str) -> tuple[str, str]:
    found = [name for name in INTERNAL_FILENAMES if re.search(re.escape(name), full_text)]
    if found:
        return "Fail", f"named internal file(s): {found}"
    return "Pass", ""


def check_criterion_8(statuses: dict) -> tuple[str, str]:
    asked = [k for k, (status, _) in statuses.items() if status == "asked"]
    reconsidered = []
    for k, (status, text) in statuses.items():
        if text and any(re.search(p, text, re.I) for p in RECONSIDER_PATTERNS):
            reconsidered.append(k)
    missing = [k for k, (status, _) in statuses.items() if status == "missing"]
    if asked:
        return "Fail", f"asked user for clarification on commit(s): {asked}"
    if reconsidered:
        return "Fail", f"reconsidered/hedged on a decision for commit(s): {reconsidered}"
    if missing:
        return "Unverifiable", f"commit(s) not addressed anywhere: {missing}"
    return "Pass", ""


def main() -> None:
    case_count = get_case_count()
    runs = discover_runs()

    rows = []
    for name, (kind, path) in runs.items():
        text = load_response_text(kind, path)
        segments = parse_segments(text)
        aggregate_skips = parse_aggregate_skips(text)
        statuses = classify_commits(segments, aggregate_skips, case_count)

        c1, n1 = check_criterion_1(statuses, text)
        c2, n2 = check_criterion_2(statuses, segments)
        c4, n4 = check_criterion_4(text)
        c8, n8 = check_criterion_8(statuses)

        notes = "; ".join(f"C{c}: {n}" for c, n in [(1, n1), (2, n2), (4, n4), (8, n8)] if n)
        rows.append(
            {
                "run": name,
                "criterion_1_past_tense": c1,
                "criterion_2_one_note_per_commit": c2,
                "criterion_4_no_internal_filenames": c4,
                "criterion_8_decided_every_commit": c8,
                "notes": notes,
            }
        )
        print(f"{name}: C1={c1} C2={c2} C4={c4} C8={c8}")

    with OUTPUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run",
                "criterion_1_past_tense",
                "criterion_2_one_note_per_commit",
                "criterion_4_no_internal_filenames",
                "criterion_8_decided_every_commit",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {OUTPUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
