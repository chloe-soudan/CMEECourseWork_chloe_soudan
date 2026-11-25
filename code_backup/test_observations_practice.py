#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: test_observations_practice.py
# Desc: Testing observations_practice.py
# Date: Oct 2026


from observations_practice import (load_observations,
                                   parse_count, 
                                   summarise_site_stage1,
                                   summarise_site_stage2,
                                   summarise_site_stage3,
                                   summarise_site)

# Check if parce_count() works as expected for normal case:
# ordinary count text becomes an integer.
assert parse_count("2") == 2

# Check if parce_count() works as expected for boundary case:
# zero is a valid known count.
assert parse_count("0") == 0

# Check if parce_count() works as expected for special valid case: 
# blank text represents a missing count.
assert parse_count("") is None

# Check if parce_count() works as expected for failure cases:
# each invalid value must raise ValueError.
for bad_count in ["-1", "many", 2]:
    try:
        parse_count(bad_count)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid count accepted: {bad_count!r}")

## Stage 1
# Importing data to test summarise_site function with 
unique_rows = [
    {"site": "A", "date": "2026-10-01", "count": "2"},
    {"site": "A", "date": "2026-10-02", "count": "3"},
    {"site": "B", "date": "2026-10-01", "count": "9"},
]


assert summarise_site_stage1(unique_rows, "A") == (5, 0)

## Stage 2

missing_rows = [
    {"site": "C", "date": "2026-10-01", "count": ""},
    {"site": "C", "date": "2026-10-02", "count": ""},
]
zero_rows = [{"site": "D", "date": "2026-10-01", "count": "0"}]

assert summarise_site_stage2(missing_rows, "C") == (None, 2)
assert summarise_site_stage2(zero_rows, "D") == (0, 0)
assert summarise_site_stage2([], "A") == (None, 0)
assert summarise_site_stage2(unique_rows, "Z") == (None, 0)

## Stage 3
assert summarise_site_stage3(unique_rows + [unique_rows[0]], "A") == (5, 0)
assert summarise_site_stage3(missing_rows + [missing_rows[0]], "C") == (None, 2)

# output: nothing, which means test has passed

## Stage 4

rows = load_observations("data/bootcamp_observations.csv")
assert summarise_site(rows, "A") == (2, 1)
assert summarise_site(rows, "B") == (0, 0)

boundary_rows = load_observations("data/bootcamp_observations_boundary.csv")
assert summarise_site(boundary_rows, "C") == (None, 2)
assert summarise_site(boundary_rows, "D") == (0, 0)
assert summarise_site(rows, "Z") == (None, 0)

# output: nothing, which means it passed all the test 

## Complete example of helper and failure checks
def expect_summary_error(rows, site="A"):
    try:
        summarise_site(rows, site)
    except ValueError:
        pass
    else:
     
        raise AssertionError("Expected ValueError, but the call succeeded")

invalid_rows = load_observations("data/bootcamp_observations_invalid.csv")
for invalid_row in invalid_rows:
    expect_summary_error([invalid_row])

expect_summary_error([{"site": "A", "count": "2"}])
expect_summary_error([{"site": "A", "date": "2026-10-01", "count": "2", "extra": "x"}])
expect_summary_error([{"site": "", "date": "2026-10-01", "count": "2"}])
expect_summary_error([{"site": "A", "date": "", "count": "2"}])
expect_summary_error([{"site": "A", "date": "2026-10-01", "count": 2}])
expect_summary_error(["not a row dictionary"])
expect_summary_error(None)
expect_summary_error(rows, "")
expect_summary_error(rows, 2)

# outputs: nothing, which means tests have passed
# note: checked the invalid_rows file: it had two rows (as expected)

# confirming that the input rows are unchanged
original_rows = [row.copy() for row in rows]
summarise_site(rows, "A")
assert rows == original_rows
# output: nothing, which means test has passed (rows are unchanged)