########### BOOTCAMP ASSIGNMENT 1: UNIX, SHELL AND GIT ############

## Chloe Soudan - MSc CMEE
## chloe.soudan26@imperial.ac.uk


### AIMS ###
# getting familiar with unix, shell scripting, and using GitHub repositories

### SOFTWARE REQUIREMENTS ###
# VS Code (or equivalent environment that can run Unix and Bash terminal)

### FASTA EXERCISE ###
## aims: getting familiar with coding in FASTA files
## workflow: counting lines, displaying certain lines, counting sequence length, counting motif occurences, calculating base ratios 
## files needed: FASTA folder from MQB repository (MQB/content/data/fasta)
# note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code


### SHELL PRACTICAL ###
## aims: improving a script that converts tab-delimimted files into comma-delimited (csv) files
## workflow: working throuhg a provided script and removing redundancies, unnecessary steps, and optimizing the provided script 
## files needed: tabtocsv.sh - Shell Scripting chapter

### NEW SCRIPT PRACTICAL ###
## aims: based on previous practical, creating a script that converts csv files to tab-delimited ones
## workflow: adapting csvtotab.sh to current aims and optimizing it
## files needed: temperatures folder from MQB repository (MQB/content/data/temperatures)


######### ASSIGNMENT 2 ##############

# AIMS: running clean_silwood_trees.py should create three files in results folder: silwood_trees_clean.csv, silwood_trees_issues.csv (rejected rows), oak_species_counts.csv (oak summary)

# pseudocode for validate_record function
# used the following websites: 
- https://realpython.com/what-does-arrow-mean-in-python/

INPUT: row (disct[str,str]), source_row (int), accepted_ids (set(str))

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
  if value is not mathematically finite (outsie of range):
  add as reason for rejection of that row: "{field} out of range"
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


# pseudocode for process_records
INPUT: observations with site, date and count
Validate every record; stop and report an error for invalid input
Identify exact duplicate records and keep one copy of each
For each site:
    count the observations with missing counts
    if at least one count is known:
        add the known counts and report their total
    otherwise:
        report that no known total is available
OUTPUT: known-count total (or unavailable) and missing-count number per site

# pseudocode for summarise_oaks
creating an oaks_count list 

for each row in cleaned_records:
  if the genus of that row (row[genus]), regardless of trailing whitrespaces and casefold (.strip.casefold()), equlas "quercus", then:

  find the species of that row:
  if that species is not already in oak_counts:
  add the species to the species column of oak_counts (oak_counts[species]) and set the count to 1
  if else add 1 (+= 1) to that species count

return a lsit of each species and its respective counts 

# sources
- https://introcs-python.cs.luc.edu/dict_algorithms/overview.html?utm_source=chatgpt.com
- Asked AI for help with strcutring my function's return 