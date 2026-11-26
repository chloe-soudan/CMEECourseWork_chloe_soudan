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

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "code"))

from clean_silwood_trees import (
    load_records,
    validate_record,
    process_records,
    summarise_oaks,
    INPUT_FIELDS,
    ISSUE_FIELDS,
    OAK_COUNT_FIELDS,
    PROJECT_ROOT,
    INPUT_PATH,
    RESULTS_DIR)

records = load_records(INPUT_PATH)

####  Testing ####

#################################
### Missing record id  and invalid record id
#################################
missing_record_id = { 
    'record_id': '  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0' }


validate_record(missing_record_id, source_row=1, accepted_ids=set())
# returns (None, ['missing record_id', 'invalid record_id']), as expected
# check succesful 

#################################
### Invalid record_id
#################################

invalid_record_id = { 
    'record_id': 'SA010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0' }

validate_record(invalid_record_id, source_row=1, accepted_ids=set())
# returns (None, ['invalid record_id']), as expected
# check succesful

#################################
###Checking for invalid location
#################################

invalid_location = { 
    'record_id': 'ST010  ',
    'location': "manor",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0' }

validate_record(invalid_location, source_row=1, accepted_ids=set())
# returns (None, ['invalid location']), as expected
# check succesful

#################################
### Invalid genus 
#################################
invalid_genus = { 
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercuz',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0' }

validate_record(invalid_genus, source_row=1, accepted_ids=set())
# returns (None, ['invalid genus']), as expected
# check succesful

#################################
### Invalid species
#################################
invalid_species = { 
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraeaa',
    'distance_m': '8.2',
    'angle_degrees': '45.0' }

validate_record(invalid_species, source_row=1, accepted_ids=set())
# returns (None, ['invalid species']), as expected
# check succesful

#################################
### Invalid genus-species combination
#################################

invalid_combination = { 
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'sylvatica',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}

validate_record(invalid_combination, source_row=1, accepted_ids=set())
# returns (None, ['invalid genus/species combination']), as expected
# check succesful

#################################
### Distance out of range
#################################

## a. just under the lower range limit
distance_out_of_range1 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '0',
    'angle_degrees': '45.0'}
validate_record(distance_out_of_range1, source_row=1, accepted_ids=set())
# returns (None, ['distance_m out of range']), as expected

## b. just within the lower range limit 
distance_out_of_range2 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '1',
    'angle_degrees': '45.0'}
validate_record(distance_out_of_range2, source_row=1, accepted_ids=set())
# return the record, meaning it is valid, as expected

## c. just within the upper range limit
distance_out_of_range3 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '100',
    'angle_degrees': '45.0'}
validate_record(distance_out_of_range3, source_row=1, accepted_ids=set())
# returns the record, meaning it is valid, as expected

## d. just over the upper range limit
distance_out_of_range4 = { 
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '101',
    'angle_degrees': '45.0'}
validate_record(distance_out_of_range4, source_row=1, accepted_ids=set())
# returns (None, ['distance_m out of range']), as expected

# distance check was succesful 

#################################
### Out of range angle_degrees
#################################

## a. just under the lower range limit
angle_out_of_range1 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '0'}
validate_record(angle_out_of_range1, source_row=1, accepted_ids=set())
#returns (None, ['angle_degrees out of range']), as expected

## b. just within the lower range limit
angle_out_of_range2 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '1'}
validate_record(angle_out_of_range2, source_row=1, accepted_ids=set())
# returns the record, meaning it is valid, as expected

## c. just withing the upper range limit 
angle_out_of_range3 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '90'}
validate_record(angle_out_of_range3, source_row=1, accepted_ids=set())
# returns the record, meaning it is valid, as expected

## d. just over the upper range limit
angle_out_of_range4 = {
    'record_id': 'ST010  ',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '91'}
validate_record(angle_out_of_range4, source_row=1, accepted_ids=set())
# returns (None, ['angle_degrees out of range']), as expected

# out of range angle_degrees check was succesful

#################################
### Checking for order of error messages
#################################

invalid_record = {
    'record_id': '  ',
    'location': "manor",
    'genus': 'Quercuz',
    'species': 'petraeaa',
    'distance_m': '-1',
    'angle_degrees': '91'}
validate_record(invalid_record, source_row=1, accepted_ids=set())
# returns (None, ['missing record_id', 'invalid record_id', 'invalid location', 'invalid genus', 'invalid species', 'distance_m out of range', 'angle_degrees out of range']), as expected
# check succesful

#################################
### Checking for trailing spaces and case sensitivity (text cleaning)
#################################

sens_record = {
    'record_id': 'ST010 ',
    'location': "nash's field",
    'genus': 'Quercus',
    'species': ' Petraea',
    'distance_m': '8.2 ',
    'angle_degrees': '89'}
validate_record(sens_record, source_row=1, accepted_ids=set())
# returns the record, meaning it is valid, as expected
# check succesful


###############################
## Checking validate_record  for valid data 
###############################

valid_record = {
    'record_id': 'ST010',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}    

validate_record(valid_record, source_row=1, accepted_ids=set())
# returns the record, meaning it is valid, as expected
# check succesful

#################################
### Checking for duplicate (using process_records function)
#################################

duplicate_records = [
    {'record_id': 'ST001',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0'},
    {'record_id': 'ST001',
    'location': "Nash's Field",
    'genus': 'Quercus', 
    'species': 'petraea',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}] 

process_records(duplicate_records)

# returns ([{'record_id': 'ST001', 'location': "Nash's Field", 'genus': 'Quercus', 'species': 'petraea',
# 'distance_m': '8.2', 'angle_degrees': '45.0'}], [{'record_id': 'ST001', 'reasons': 'duplicate record_id'}])
# This means that the first record was accepted, but not the second (as it was a duplicate), as expected.

# check succesful

#################################
### Checking the outputs of process records
#################################
accepted_records, invalid_records = process_records(records)

print(accepted_records)
print(invalid_records)

# Accepted records were printed as a list of dictionaries, as expected. 
# Invalid records were printed as a list of dictionaries, with the record_id and reasons for rejection, as expected.
# Check succesful

#################################
### Checking summarise_oaks function
#################################

## Outputs
summarise_oaks(accepted_records)

# Returns a list of dictionaries with the species and count of accepted oak records, as expected.


## If no oaks
no_oaks = [
    {'record_id': 'ST001',
    'location': "Nash's Field",
    'genus': 'Betula',
    'species': 'pendula',
    'distance_m': '8.2',
    'angle_degrees': '45.0'},
    {'record_id': 'ST002',
    'location': "Manor house",
    'genus': 'Fagus', 
    'species': 'sylvatica',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}] 
print(summarise_oaks(no_oaks))

# Returns [] (empty list), as expected 

## Checking exact oak name
exact_oak_name = [
    {'record_id': 'ST001',
    'location': "Nash's Field",
    'genus': 'Quercus',
    'species': 'robur',
    'distance_m': '8.2',
    'angle_degrees': '45.0'},
    {'record_id': 'ST002',
    'location': "Manor house",
    'genus': 'Quercus', 
    'species': 'robur',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}] 
print(summarise_oaks(exact_oak_name))
# returns [{species: 'robur', count: 2}], as expected 

## Near match oak name
near_oak = [
    {'record_id': 'ST001',
    'location': "Nash's Field",
    'genus': 'Quercuss',
    'species': 'robur',
    'distance_m': '8.2',
    'angle_degrees': '45.0'},
    {'record_id': 'ST002',
    'location': "Manor house",
    'genus': 'Quercus', 
    'species': 'robur',
    'distance_m': '8.2',
    'angle_degrees': '45.0'}] 
print(summarise_oaks(near_oak))
# returns [{species: 'robur', count: 1}], as expected it only counts the exact match and not the near match

###############################
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

    # checking for invalid numerical fields and our of range values

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


    REASONS_ORDER = ["missing record_id", "invalid record_id", "duplicate record_id", "missing location", "invalid location", "missing genus",
                 "invalid genus", "missing species", "invalid species", "invalid genus/species combination", "missing distance_m",
                 "invalid distance_m", "distance_m out of range", "missing angle_degrees", "invalid angle_degrees", "angle_degrees out of range"]

    reasons_sorted = sorted(reasons, key=REASONS_ORDER.index)

    if reasons_sorted:
        return None, reasons_sorted

    accepted_ids.add(row["record_id"]
                 )
    return row, []


validated_records =validate_record(records[3], source_row=1, accepted_ids = set())
print(validated_records)
# record[3] was validated 

# trying again with other records to see if they get errors

validated_records =validate_record(records[2], source_row=1, accepted_ids = set())
print(validated_records)
# no error

validated_records =validate_record(records[7], source_row=1, accepted_ids = set())
print(validated_records)
validated_records =validate_record(records[8], source_row=1, accepted_ids = set())
print(validated_records)
validated_records =validate_record(records[13], source_row=1, accepted_ids = set())
print(validated_records)
validated_records =validate_record(records[14], source_row=1, accepted_ids = set())
print(validated_records)
# note: all valid, returns the rows

validated_records =validate_record(records[27], source_row=1, accepted_ids = set())
print(validated_records)
# Error message: invalid location
validated_records =validate_record(records[28], source_row=1, accepted_ids = set())
print(validated_records)
# Error message: invalid location

############# TESTING PROCESS_RECORDS ##########

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


accepted_records, invalid_records = process_records(records)
print(accepted_records, invalid_records)

# note: prints a list of dict of the accepted records and their data

##### TESTING SUMMARY_OAKS ######

from collections import Counter 

def summarise_oaks(clean_records: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Count accepted oak records by species."""

    oak_species = []

    for row in clean_records:
        if row["genus"].casefold().strip() == "quercus":
            oak_species.append(row["species"].casefold().strip())

    oak_counts = Counter (oak_species)

    return [{"species": species, "count": count}
            for species, count in oak_counts.items()]


oak_summary = summarise_oaks(accepted_records)