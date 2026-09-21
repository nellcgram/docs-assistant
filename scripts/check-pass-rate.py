#!/usr/bin/env python3
"""Fail (exit 1) if the mechanical pass rate is below a minimum.

Reads evals/runs/mechanical-results.csv, written by check-mechanical.py. A case
passes under the same rule check-mechanical.py uses for its own per-run tally:
the response addressed the commit, and none of the four criteria is "Fail".
"Unverifiable" doesn't count against a case.

The CSV holds every scripted run in the repo's history, so pass --run to score
only the run this job just produced (for example --run v4). Without it, old
runs would dilute the rate and a real regression could go unnoticed.

The nonzero exit code is what makes a GitHub Actions step, and so the check,
show as failed.
"""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = ROOT / "evals/runs/mechanical-results.csv"

CRITERION_COLUMNS = [
    "criterion_1_past_tense",
    "criterion_2_one_note_per_commit",
    "criterion_4_no_internal_filenames",
    "criterion_8_decided_every_commit",
]

# check-mechanical.py doesn't write a separate "missing" column; it shows up as
# this note text on criteria 2 and 8.
MISSING_NOTE = "commit not addressed anywhere"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--minimum",
        type=float,
        required=True,
        help="lowest acceptable pass fraction, from 0 to 1 (e.g. 0.75)",
    )
    parser.add_argument(
        "--run",
        help="only score this run and its -rep-NN repeats (e.g. v4); default: every run",
    )
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="results file to read")
    return parser.parse_args()


def in_run(row_run: str, run: str | None) -> bool:
    return run is None or row_run == run or row_run.startswith(f"{run}-rep-")


def case_passes(row: dict) -> bool:
    if MISSING_NOTE in row["notes"]:
        return False
    return "Fail" not in (row[c] for c in CRITERION_COLUMNS)


def main() -> None:
    args = parse_args()

    if not args.csv.exists():
        sys.exit(f"{args.csv} not found; run check-mechanical.py first")

    with args.csv.open(newline="") as f:
        rows = [r for r in csv.DictReader(f) if in_run(r["run"], args.run)]

    # An empty selection must fail, not pass: it means the eval produced nothing.
    if not rows:
        scope = f"run '{args.run}'" if args.run else "any run"
        sys.exit(f"No rows in {args.csv.name} for {scope}")

    passed = sum(case_passes(r) for r in rows)
    rate = passed / len(rows)
    print(f"{passed} of {len(rows)} cases pass all mechanical criteria ({rate:.2f})")

    if rate < args.minimum:
        sys.exit(f"FAIL: pass rate {rate:.2f} is below the minimum {args.minimum:.2f}")
    print(f"OK: pass rate {rate:.2f} meets the minimum {args.minimum:.2f}")


if __name__ == "__main__":
    main()
