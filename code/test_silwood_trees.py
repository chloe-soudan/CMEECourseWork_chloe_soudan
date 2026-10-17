#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# Practical: validating tree-survey records 

"""Validate and clean the synthetic Silwood tree survey."""

from __future__ import annotations

import csv
import re
import math
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



def validate_record(
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Clean one record, or return the reasons it cannot be used."""

    reasons = []
    #checking for missing fields 
    for field in INPUT_FIELDS:
        if row[field] is None or row[field].strip() == "":
            reasons.append(f"missing {field}") 
        else: #removing whitspaces and casefld sensitivity
            row[field] = row[field].strip()

    # checking for invalid record_id
    if not re.fullmatch(r"ST[0-9]{3}", row["record_id"]):
        reasons.append("invalid record_id")

    # checking for invalid location
    locations = ["silwood bottom", "nash's field", "manor house","reactor wood"]

    if row["location"].casefold() not in locations: 
        reasons.append("invalid location")

    # checking for invalid genus 
    valid_genus = ["quercus", "acer", "betula", "fagus", "fraxinus"]

    if row["genus"].casefold() not in valid_genus:
        reasons.append("invalid genus") 

    # checking for invalid species
    valid_species = ["robur", "petraea","pseudoplatanus","pendula","sylvatica","excelsior"]

    if row["species"].casefold() not in valid_species:
     reasons.append("invalid species")

    # checking for invalid genus-species combinations
    # checking for invalid genus/species combination
    valid_combinations = [("quercus", "robur"), ("quercus", "petraea"), ("acer", "pseudoplatanus"), ("betula", "pendula"),
                   ("fagus", "sylvatica"), ("fraxinus", "excelsior")]

    if row["genus"].casefold() in valid_genus and row["species"].casefold() in valid_species:
        if (row["genus"].casefold(), row["species"].casefold()) not in valid_combinations:
            reasons.append("invalid genus/species combination")

    # checking for invalid numerical fields

    NUMERIC_FIELDS = ["distance_m", "angle_degrees"]

    for field in NUMERIC_FIELDS:
        if row[field] is None or row[field].strip() == "":
            continue

        try:
            value = float(row[field])

            if not math.isfinite(value):
                reasons.append(f"invalid {field}")
        except ValueError:
            reasons.append(f"invalid {field}")

    # checking the range of numerical fields

    # checking for duplicata record_id
    if row["record_id"] in accepted_ids:
        reasons.append("duplicate record_id")


    REASONS_ORDER = ["missing record_id", "invalid record_id", "duplicate record_id", "missing location", "invalid location", "missing genus",
                 "invalid genus", "missing species", "invalid species", "invalid genus/species combination", "missing distance_m",
                 "invalid distance_m", "distance_m out of range", "missing angle_degrees", "invalid angle_degrees", "angle_degrees out of range"]

    reasons_sorted = sorted(reasons, key=REASONS_ORDER.index)

    if reasons_sorted:
        return None, reasons_sorted

    accepted_ids.add(row["record_id"]
                 )
    return row, []
# source: https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
# wasn't working, asked ai why and itsuggested i add .index to the key 


def process_records(
    rows: Iterable[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Sort records into accepted rows and issue reports."""
    accepted_records = []
    invalid_records = []
    accepted_ids = set()

    for record, row in enumerate(rows, start =2):
        cleaned_record, reasons = validate_record(row, record, accepted_ids)
        
        if cleaned_record is not None:
            accepted_records.append(cleaned_record)
        else:
            invalid_records.append({
                "record_id": row["record_id"],
                "reasons":",".join(reasons)})
    return accepted_records, invalid_records


# sources
# https://stackoverflow.com/questions/61063965/in-python-can-a-loop-be-used-within-a-function

test_rows = [
    {
        "record_id": "ST001",
        "location": "Silwood Bottom",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "12.5",
        "angle_degrees": "45",
    },
    {
        "record_id": "ST002",
        "location": "Unknown Place",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "10",
        "angle_degrees": "90",
    },
    {
        "record_id": "ST003",
        "location": "Manor House",
        "genus": "Acer",
        "species": "pseudoplatanus",
        "distance_m": "8.2",
        "angle_degrees": "30",
    },
]

accepted, rejected = process_records(test_rows)

print("Accepted records:", accepted)
print("Rejected records:", rejected)