########### BOOTCAMP ##########

## Chloe Soudan - MSc CMEE
## chloe.soudan26@imperial.ac.uk

##### ASSIGNMENT 1: UNIX, SHELL, AND GIT ########

###  Aims ###
# getting familiar with unix, shell scripting, and using GitHub repositories

### SOFTWARE REQUIREMENTS
# VS Code (or equivalent environment that can run Unix and Bash terminal)

### Fasta exercises ###
# aims: getting familiar with coding in FASTA files
# workflow: counting lines, displaying certain lines, counting sequence length, counting motif occurences, calculating base ratios 
# files needed: FASTA folder from MQB repository (MQB/content/data/fasta)
# note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code


### Shell practical ###
# aims: improving a script that converts tab-delimimted files into comma-delimited (csv) files
# workflow: working throuhg a provided script and removing redundancies, unnecessary steps, and optimizing the provided script 
# files needed: tabtocsv.sh - Shell Scripting chapter

### New script practical ###
## aims: based on previous practical, creating a script that converts csv files to tab-delimited ones
## workflow: adapting csvtotab.sh to current aims and optimizing it
## files needed: temperatures folder from MQB repository (MQB/content/data/temperatures)


##### ASSIGNMENT 2:PYTHON ########

### Aims ###

Adapting functions in clean_silwood_trees.py so that the script produices three files in results folder: silwood_trees_clean.csv, silwood_trees_issues.csv (rejected rows), oak_species_counts.csv (oak summary)

### Software requirements ###
Vs Code (or equivalent environment that can run Python)

### Required data and scripts ###
From MQB repostiory into own repository 
(1) from content/data to project root data folder
    - silwood_trees_raw
    - silwood_trees_metadata
(2) from content/code to project root code folder
    - clean_silwood_trees
(3) To create within project root code folder:
    - test_silwood_trees 

### Adapting the functions ###

## 1. Validated_records
INPUT: a record from records (records = load_records()). Format: row: dict[str, str], source_row: int, accepted_ids: set[str]
AIMS: validating if a record is valid or not, and if unvalid, print the reason why
FUNCTION:
Defining validate_record() where:
  for each field in INPUT_FIELDS: 
  we check if that row[field] has no content (None) or just empty spaces "". if it does then:
  add as reason (reason.append) for rejection of that row "missing <field>
    #sources:
   -https://stackoverflow.com/questions/1278749/- - -how-do-i-detect-missing-fields-in-a-csv-file-in-a-pythonic-way

  if the format of row[field] does not have the format (not re.fullmatc) "ST" followed by three integers [0-9]{3} then:
  add as reason for rejection of that row: "invalid record_id"
# sources:
https://stackoverflow.com/questions/64644087/python-validate-if-column-entries-match-a-desired-format
https://zetcode.com/python/regex-fullmatch-function/ 

  if location names (regardless of casing) are not in locations list, then:
  add as reason for rejection of that row: "invalid location"
    # sources: 
  -https://www.geeksforgeeks.org/python/python-string-casefold-method

  repeat the same for genus and species

  if row["genus"] and row["species"] were considered valid individually, but that (row["genus"], row["species"]) combination is not in valid_combinations list, then:
  add as reason for rejection of that row: "invalid genus/species combination"

  setting NUMERIC_FIELDS  to be (=) "distance_m", "angle_degrees"

  creating a loop where for each field in NUMERIC_FIELDS:
  if that row[field] is empty (None) or just made of empty spaces "": 
  skip the following chunk (continue) 
  if not though try to create a float string from row[field] and name it value. 
  if value is not mathematically finite :
  add as reason for rejection of that row: "invalid {field}"
  if field mathematically finite: 
    if field is distance_m:
      if value not greater than 0 or greater than 100: 
        add as reason for rejection of the row: "distance_m out of range"
    if filed is angle_degrees:
      if value smaller not greater than 0 or larger than 90:
        add as reason for rejection of the row: "angle_degrees out of range"
  when converting to float fails (except ValueError):
  add as reason for rejection of that row "invalid {field}
    # sources: 
  -AI to get a hint on how to tackle this (tried to find is.numeric (R) equivalent in python), and it suggested to use float 
  -https://www.geeksforgeeks.org/python/python-check-for-float-string/

  if row["record_id"] is in accepted_ids (which means it was already passed during another iteration):
  add as reason for rejection "duplicate record_id"

  setting REASONS_ORDER to be [to order indicated in the instructions]

  creating reasons_sorted, all the rejection reasons obtained for each row in the order of REASON_ORDER

  # source
  - https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
 -  wasn't working, asked AI why and itsuggested i add .index to the key 

OUTPUT: a tuple with: 
if valid record: a dictionary of the record followed by an empty list
if unvalid reocrd: none, followed by a list of the reason(s) why
=> tuple[dict[str, str] | None, list[str]]


# 2. Process_records
INPUT: records (obtained from records = load(records)), format: rows: Iterable[dict[str, str]]
AIMS: Validate every record; stop and report an error for invalid input & identify exact duplicate records and keep one copy of each.
FUNCTION
For each site:
    count the observations with missing counts
    if at least one count is known:
        add the known counts and report their total
    otherwise:
        report that no known total is available
OUTPUT: known-count total (or unavailable) and missing-count number per site. Format: tuple[list[dict[str, str]], list[dict[str, str]]]

# 3. Summarise_oaks
INPUT: the validated records obtained through process_records. Format: (Iterable[dict[str, str]])
AIMS: Identifying all the oak species in the accepted records, counting the frequency of each species, and putting this into a list
FUNCTION:
for each row in clean_records 
  if the genus of that row (row[genus]), regardless of trailing whitespaces and casefold (.strip.casefold()), equals "quercus", then:
   append that row's species (removing casefold and stripping withespaces) to the oak_species list

  then, using Counter, create oak_counts which is a list where all the species of oak_species are listed with their respective counts 

then, return a list of dict with each species (in the species dict) and its respective freqeuncy (in the count dict) usig .items() 

OUTPUT: list of dictionaries of oak species and respective counts. Format: list[dict[str, str]]
# sources
- https://introcs-python.cs.luc.edu/dict_algorithms/overview.html?utm_source=chatgpt.com
- https://www.geeksforgeeks.org/python/python-counter-items-counter-keys-and-counter-values/
- https://realpython.com/python-counter/
- https://www.geeksforgeeks.org/python/counters-in-python-set-1/
- https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
- Asked AI for help with structurin my function's return