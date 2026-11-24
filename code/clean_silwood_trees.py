#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Descr: validating and summarising Silwood tree survey data 
# Script: clean_silwood_trees.py
# Date: Oct 2026
"""Validate and clean the synthetic Silwood tree survey."""

from __future__ import annotations
from collections import Counter

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

## Loading the records

def load_records(path: Path = INPUT_PATH) -> list[dict[str, str]]: # function returns a list of dictionaries 
    """Read the survey and check its column names."""
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source) # reading the input file row by row
        # checking that the input file fieldnames are different than expected INPUT_FIELDS
        if reader.fieldnames != INPUT_FIELDS:
            raise ValueError(
                f"Expected columns {INPUT_FIELDS}, found {reader.fieldnames}"
            )
        return list(reader) # return a list of dictionaries 


##  Validating each row

def validate_record( 
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Clean one record, or return the reasons it cannot be used."""
    reasons = [] #creating an empty list that will store reason for rejection
    #checking for missing fields 
    for field in INPUT_FIELDS:
        if row.get(field) is None or row[field].strip() == "":
            reasons.append(f"missing {field}") 
        else: #removing whitspaces 
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
    valid_combinations = [("quercus", "robur"), ("quercus", "petraea"), ("acer", "pseudoplatanus"), ("betula", "pendula"),
                   ("fagus", "sylvatica"), ("fraxinus", "excelsior")]

    if row["genus"].casefold() in valid_genus and row["species"].casefold() in valid_species:
        if (row["genus"].casefold(), row["species"].casefold()) not in valid_combinations:
            reasons.append("invalid genus/species combination")

  
    # checking for invalid numerical fields  (out of range values)
    NUMERIC_FIELDS = ["distance_m", "angle_degrees"]

    for field in NUMERIC_FIELDS:
        if row[field] is None or row[field].strip() == "":
            continue

        try:
            value = float(row[field])

            if not math.isfinite(value):
                reasons.append(f"invalid {field}")

            else:
                if field == "distance_m":
                    if value <= 0 or value > 100:
                        reasons.append("distance_m out of range")

                if field == "angle_degrees":
                    if value <= 0 or value >=90:
                        reasons.append("angle_degrees out of range")

        except ValueError:
            reasons.append(f"invalid {field}")

    # checking for duplicate record_id
    if row["record_id"] in accepted_ids:
        reasons.append("duplicate record_id")

    # ordering reasons for unvalid record

    REASONS_ORDER = ["missing record_id", "invalid record_id", "duplicate record_id", "missing location", "invalid location", "missing genus",
                 "invalid genus", "missing species", "invalid species", "invalid genus/species combination", "missing distance_m",
                 "invalid distance_m", "distance_m out of range", "missing angle_degrees", "invalid angle_degrees", "angle_degrees out of range"]

    reasons_sorted = sorted(reasons, key=REASONS_ORDER.index)

    if reasons_sorted:
        return None, reasons_sorted

    accepted_ids.add(row["record_id"]
                 )
    return row, []

## Processing all records - validating each record, or rejecting it and stating reasons for rejection 

def process_records(
    rows: Iterable[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Sort records into accepted rows and issue reports."""
    # Creating empty lists and set that will store 
    # the accepted records, the invalid records and 
    # the accepted record_ids
    accepted_records = [] 
    invalid_records = []
    accepted_ids = set()

    for record, row in enumerate(rows, start =2): # looping through eahc record, starting at the second row
        # running the validate_record function on each row,
        # and storing the cleaned record and reasons for rejection
        cleaned_record, reasons = validate_record(row, record, accepted_ids) 
        # appending the record to accepted_records, if it was valid
        if cleaned_record is not None:
            accepted_records.append(cleaned_record)
        # appending the record to invalid_records, if it was invalid
        # and storing the reaasons for rejection in a dictionary of record_id and reasons 
        else:
            invalid_records.append({
                "record_id": row["record_id"],
                "reasons":",".join(reasons)})
    # returning the accepted and invalid records
    return accepted_records, invalid_records

## Summarising oak records

def summarise_oaks(clean_records: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Count accepted oak records by species."""

    oak_species = [] # creating an empty list that will store the oak species' names 
    # adding species names to oak_species when genus is quercus
    for row in clean_records:
        if row["genus"].casefold().strip() == "quercus":
            oak_species.append(row["species"].casefold().strip())

    # counting the occurrences of each oak species
    oak_counts = Counter (oak_species)

    # returning the species names and respectives counts as a list of dictionaries 
    return [{"species": species, "count": count}
            for species, count in oak_counts.items()]

## Writing the output files into csv files 

def write_csv(
    path: Path,
    fieldnames: list[str],
    rows: Iterable[dict[str, str]],
) -> None:
    """Write rows to a CSV file, replacing an older copy."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Clean the survey and write the three result files."""
    clean_records, issues = process_records(load_records())
    oak_counts = summarise_oaks(clean_records)

    write_csv(
        RESULTS_DIR / "silwood_trees_clean.csv",
        INPUT_FIELDS,
        clean_records,
    )
    write_csv(
        RESULTS_DIR / "silwood_tree_issues.csv",
        ISSUE_FIELDS,
        issues,
    )
    write_csv(
        RESULTS_DIR / "oak_species_counts.csv",
        OAK_COUNT_FIELDS,
        oak_counts,
    )


if __name__ == "__main__":
    main()


