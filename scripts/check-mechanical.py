#!/usr/bin/env python3
"""Check release-notes eval run outputs against the mechanical rubric criteria.

Rubric.md's Version 2 criteria 1, 2, 4, and 8 are checked here: the ones that can be
judged from the response text alone, without comparing against the actual commit
content. A fifth guard, gold_commit_written, fails a case when the gold file says the
commit gets a note but the response skipped or asked about it, so a skill that skips
everything can't pass. Criteria 3, 5, 6, and 7 need a judgment call and are out of
scope for this script. Version 1 (runs 1-3) predates these criteria and isn't checked
either.

Criterion 2 only catches duplicate entries and commits the response never
addresses. Whether a skipped commit should have been written up is criterion
3, which a person grades. Criterion 4 flags any ".md" file name in the response.
It doesn't flag bare words like "skill", because a release note can say "the
skill" without naming a file.

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
GOLD_PATH = ROOT / "evals/gold/release-notes.md"
OUTPUT_CSV = RUNS_DIR / "mechanical-results.csv"

# Any markdown file name counts as internal, so a new file such as
# house-style.md or hard-surfaces.md is caught without editing a list.
INTERNAL_FILENAME_RE = re.compile(r"[\w./-]+\.md\b", re.I)

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
    r"share the diff",
    r"and i'll write",
    r"and i'll finalize",
    r"if you can (tell|share|confirm)",
    r"i'll (sharpen|revise|update|adjust) the entry",
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
# Used only for "single" runs (one file holding all 20 commits), where the
# skill's own format rule ("Commit N (hash): sentence") is consistently
# followed. Requires the hash so a "commit N" mention buried mid-sentence in
# another commit's prose (e.g. "Skipped: commit 11 (eval/project-meta
# change...)") can't be mistaken for the start of commit 11's own segment and
# swallow the tail of the segment before it. "Multi" runs (one file per
# commit) don't use this at all — see statuses_for_multi below, which reads
# each file directly instead of joining and regex-splitting a blob.
COMMIT_HEADER_RE = re.compile(r"Commit\s+(\d+)\s*\(([0-9a-fA-F]{5,40})\)", re.I)
CASE_FILENAME_RE = re.compile(r"case-(\d+)\.md$")
PRESENT_TENSE_RE = re.compile(
    r"\bis a\b|\bis an\b|\bis the\b|\bdoesn't\b|\bisn't\b|\bdoes\b|\bmeans\b|\baffects\b",
    re.I,
)
GERUND_SENTENCE_RE = re.compile(r"(?:^|[.!?]\s+)([A-Z][a-z]+ing)\b")
RUN_NUMBER_RE = re.compile(r"run-(\d+)")
# Verification disclaimers ("Note: I could not verify this commit against the
# repository, since it isn't accessible...") are correctly present tense since
# they describe current verification status, not the commit's effect. They
# aren't part of the release note, so criterion 1 shouldn't scan them. Matches
# an optional leading markdown emphasis marker (*Note:*, **Note:**).
NOTE_SPLIT_RE = re.compile(r"^\s*[*_]*\s*Note\s*:", re.M | re.I)
QUOTED_SPAN_RE = re.compile(r"[\"“][^\"”]*[\"”]")
# Same verification-disclaimer problem as NOTE_SPLIT_RE, but for the other
# format the model uses: an inline parenthetical instead of its own "Note:"
# line, e.g. "...it didn't have. (Unverifiable — the commit contents weren't
# available to check, so the specific wording that changed isn't reflected
# here.)" — legitimately present tense, not part of the release note. Matched
# by keyword ("verif*"/"accessib*" anywhere inside the parenthetical) rather
# than a fixed leading phrase, since the model phrases this disclaimer
# inconsistently ("Unverifiable — ...", "Not verifiable...", "Commit contents
# were not verifiable here..."). A release note's own content isn't expected
# to use these words, so matching on them anywhere inside a parenthetical is
# safe.
DISCLAIMER_PAREN_RE = re.compile(r"\([^)]*(?:verif\w*|accessib\w*)[^)]*\)", re.I)


def get_gold_write_set() -> set[int]:
    """Commit numbers the gold file says get a release note (its "Commit N (hash):" lines)."""
    return {
        int(n)
        for n in re.findall(r"^Commit (\d+) \(", GOLD_PATH.read_text(), flags=re.M)
    }


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
        if not (d.is_dir() and d.name.startswith("run-")):
            continue
        # A run folder can hold a single run's case files directly (the
        # non-repeat run) AND rep-*/ subfolders (a --repeats run) at the same
        # time, as run-11 and run-12 do — check both, don't stop at the first match.
        if any(d.glob("case-*.md")):
            runs[d.name] = ("multi", d)
        for rep_dir in sorted(d.glob("rep-*")):
            if rep_dir.is_dir() and any(rep_dir.glob("case-*.md")):
                runs[f"{d.name}-{rep_dir.name}"] = ("multi", rep_dir)

    def run_num(name: str) -> int:
        m = RUN_NUMBER_RE.search(name)
        return int(m.group(1)) if m else -1

    return dict(sorted((k, v) for k, v in runs.items() if run_num(k) >= 4))


def parse_segments(text: str) -> dict[int, list[str]]:
    matches = list(COMMIT_HEADER_RE.finditer(text))
    segments: dict[int, list[str]] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        segments.setdefault(num, []).append(text[start:end])
    return segments


def parse_aggregate_skips(text: str, case_count: int) -> set[int]:
    skips: set[int] = set()
    for line in text.splitlines():
        if re.search(r"\bskip", line, re.I) and ":" in line:
            _, _, tail = line.partition(":")
            skips.update(
                int(n) for n in re.findall(r"\b(\d{1,2})\b", tail) if 1 <= int(n) <= case_count
            )
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


def classify_text(text: str) -> str:
    if any(re.search(p, text, re.I) for p in CLARIFY_PATTERNS):
        return "asked"
    if SKIP_WORD_RE.search(text):
        return "skipped"
    return "written"


def statuses_for_single(
    path: Path, case_count: int
) -> tuple[dict[int, tuple[str, str]], dict[int, list[str]]]:
    """One file holding all `case_count` commits; split it by its own 'Commit N (hash):' headers."""
    raw = path.read_text()
    parts = re.split(r"^##\s*Response.*$", raw, flags=re.M)
    text = parts[-1] if len(parts) > 1 else raw
    segments = parse_segments(text)
    aggregate_skips = parse_aggregate_skips(text, case_count)

    statuses = {}
    for k in range(1, case_count + 1):
        if k in segments:
            joined = " ".join(segments[k])
            statuses[k] = (classify_text(joined), joined)
        elif k in aggregate_skips:
            statuses[k] = ("skipped", "")
        else:
            statuses[k] = ("missing", "")
    return statuses, segments


def statuses_for_multi(
    dir_path: Path, case_count: int
) -> tuple[dict[int, tuple[str, str]], dict[int, list[str]]]:
    """One file per commit (case-NN.md); the filename is the ground truth for
    which commit a file belongs to, so no header regex or text-joining is
    needed. Joining all files into one blob and re-splitting by a header
    regex is fragile: a skip line's own "Skipped: commit N" phrasing can get
    matched as a false header and swallow the tail of the previous file's
    segment along with it.
    """
    by_case: dict[int, str] = {}
    for f in dir_path.glob("case-*.md"):
        m = CASE_FILENAME_RE.search(f.name)
        if m:
            by_case[int(m.group(1))] = f.read_text()

    statuses = {}
    segments: dict[int, list[str]] = {}
    for k in range(1, case_count + 1):
        if k in by_case:
            text = by_case[k]
            statuses[k] = (classify_text(text), text)
            segments[k] = [text]
        else:
            statuses[k] = ("missing", "")
    return statuses, segments


def release_note_portion(status: str, text: str) -> str | None:
    """The part of a commit's segment that's actually the release note.

    Only "written" and "asked" statuses ever contain a release note ("asked"
    can still have written one before hedging in the same segment); "skipped"
    and "missing" segments have no note to check tense on at all — their text
    is a skip/verification explanation, which is legitimately present tense.
    Within that portion, drop any trailing "Note: ..." verification
    disclaimer and any quoted spans (e.g. a quoted reference to the skill's
    own "what it does" section), neither of which are the note's own prose.
    """
    if status not in ("written", "asked"):
        return None
    m = NOTE_SPLIT_RE.search(text)
    note_text = text[: m.start()] if m else text
    note_text = DISCLAIMER_PAREN_RE.sub("", note_text)
    return QUOTED_SPAN_RE.sub("", note_text)


def check_case_criterion_1(status: str, text: str) -> tuple[str, str]:
    note_text = release_note_portion(status, text)
    if not note_text:
        return "Unverifiable", "no release note to check (skipped/missing)"
    flag = has_present_tense_flag(note_text)
    if flag:
        return "Fail", f'"{flag}"'
    return "Pass", ""


def check_case_criterion_2(case_num: int, status: str, segments: dict) -> tuple[str, str]:
    if len(segments.get(case_num, [])) > 1:
        return "Fail", "duplicate entries for this commit"
    if status == "missing":
        return "Unverifiable", "commit not addressed anywhere in the response"
    return "Pass", ""


def check_case_criterion_4(text: str) -> tuple[str, str]:
    found = sorted({name for name in INTERNAL_FILENAME_RE.findall(text)}, key=str.lower)
    if found:
        return "Fail", f"named internal file(s): {found}"
    return "Pass", ""


def check_case_criterion_8(status: str, text: str) -> tuple[str, str]:
    if status == "missing":
        return "Unverifiable", "commit not addressed anywhere in the response"
    if status == "asked":
        return "Fail", "asked user for clarification"
    if text and any(re.search(p, text, re.I) for p in RECONSIDER_PATTERNS):
        return "Fail", "reconsidered/hedged on a decision"
    return "Pass", ""


def check_case_gold_write(case_num: int, status: str, text: str, write_set: set[int]) -> tuple[str, str]:
    """A commit the gold file says gets a note must get one, so skipping everything can't pass.

    Judges only the first line of the commit's text. In a single-file run the last
    commit's segment runs to the end of the response and can include the closing
    "Skipped: ..." line, which says nothing about that commit.
    """
    if case_num not in write_set:
        return "Not applicable", ""
    if status == "missing":
        return "Fail", "gold file says this commit gets a note, but it was missing"
    first = text.strip().split("\n", 1)[0]
    if any(re.search(p, first, re.I) for p in CLARIFY_PATTERNS):
        return "Fail", "gold file says this commit gets a note, but it was asked about"
    if SKIP_WORD_RE.search(first):
        return "Fail", "gold file says this commit gets a note, but it was skipped"
    return "Pass", ""


def main() -> None:
    case_count = get_case_count()
    write_set = get_gold_write_set()
    runs = discover_runs()

    rows = []
    for name, (kind, path) in runs.items():
        if kind == "single":
            statuses, segments = statuses_for_single(path, case_count)
        else:
            statuses, segments = statuses_for_multi(path, case_count)

        run_pass_count = 0
        for case_num in range(1, case_count + 1):
            status, case_text = statuses[case_num]

            c1, n1 = check_case_criterion_1(status, case_text)
            c2, n2 = check_case_criterion_2(case_num, status, segments)
            c4, n4 = check_case_criterion_4(case_text)
            c8, n8 = check_case_criterion_8(status, case_text)
            cg, ng = check_case_gold_write(case_num, status, case_text, write_set)

            if status != "missing" and "Fail" not in (c1, c2, c4, c8, cg):
                run_pass_count += 1

            notes = "; ".join(f"C{c}: {n}" for c, n in [(1, n1), (2, n2), (4, n4), (8, n8), ("gold", ng)] if n)
            rows.append(
                {
                    "run": name,
                    "case": case_num,
                    "criterion_1_past_tense": c1,
                    "criterion_2_one_note_per_commit": c2,
                    "criterion_4_no_internal_filenames": c4,
                    "criterion_8_decided_every_commit": c8,
                    "gold_commit_written": cg,
                    "notes": notes,
                }
            )
        print(f"{name}: {run_pass_count} of {case_count} cases pass all mechanical criteria")

    with OUTPUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run",
                "case",
                "criterion_1_past_tense",
                "criterion_2_one_note_per_commit",
                "criterion_4_no_internal_filenames",
                "criterion_8_decided_every_commit",
                "gold_commit_written",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {OUTPUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
