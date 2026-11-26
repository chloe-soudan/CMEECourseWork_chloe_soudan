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
