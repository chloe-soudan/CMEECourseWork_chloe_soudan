#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# Practical: validating tree-survey records 

"""Validate and clean the synthetic Silwood tree survey."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1] 
INPUT_PATH = PROJECT_ROOT / "data" / "silwood_trees_raw.csv"
RESULTS_DIR = PROJECT_ROOT / "results"

INPUT_FIELDS = [
    "record_id",
    "location",
    "genus",
    "species",
    "distance_m",
    "angle_degrees",
]
ISSUE_FIELDS = ["source_row", "record_id", "reasons"]
OAK_COUNT_FIELDS = ["species", "count"]


def load_records(path: Path = INPUT_PATH) -> list[dict[str, str]]:
    """Read the survey and check its column names."""
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != INPUT_FIELDS:
            raise ValueError(
                f"Expected columns {INPUT_FIELDS}, found {reader.fieldnames}"
            )
        return list(reader)



if __name__ == "__main__":
    records = load_records()
    print(records[:5])
    print(f"Loaded {len(records)} records.")