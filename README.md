 # BOOTCAMP #

Chloe Soudan - MSc CMEE - chloe.soudan26@imperial.ac.uk

## ASSIGNMENT 1: UNIX, SHELL, AND GIT ##

###  Aims ###
Getting familiar with unix, shell scripting, and using GitHub repositories

### Software requirements ###

VS Code (or equivalent environment that can run Unix and Bash terminal)

### Fasta exercises ###
Aims: getting familiar with coding in FASTA files
Workflow: counting lines, displaying certain lines, counting sequence length, counting motif occurences, calculating base ratios 
Files needed: FASTA folder from MQB repository (MQB/content/data/fasta)
Note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code


### Shell practical ###
Aims: improving a script that converts tab-delimimted files into comma-delimited (csv) files
Workflow: working throuhg a provided script and removing redundancies, unnecessary steps, and optimizing the provided script 
Files needed: tabtocsv.sh - Shell Scripting chapter

### New script practical ###
Aims: based on previous practical, creating a script that converts csv files to tab-delimited ones
Workflow: adapting csvtotab.sh to current aims and optimizing it
Files needed: temperatures folder from MQB repository (MQB/content/data/temperatures)


## ASSIGNMENT 2:PYTHON ## 

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

#### 1. Validated_records ####
INPUT: a record from records (records = load_records()). Format: row: dict[str, str], source_row: int, accepted_ids: set[str]
AIMS: validating if a record is valid or not, and if unvalid, print the reason why
FUNCTION:
Defining validate_record() where:
  for each field in INPUT_FIELDS: 
  we check if that row[field] has no content (None) or just empty spaces "". if it does then:
  add as reason (reason.append) for rejection of that row "missing <field>
  *sources:
   -https://stackoverflow.com/questions/1278749/- - -how-do-i-detect-missing-fields-in-a-csv-file-in-a-pythonic-way

  if the format of row[field] does not have the format (not re.fullmatc) "ST" followed by three integers [0-9]{3} then:
  add as reason for rejection of that row: "invalid record_id"
  *sources:
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
  *sources: 
  -AI to get a hint on how to tackle this (tried to find is.numeric (R) equivalent in python), and it suggested to use float 
  -https://www.geeksforgeeks.org/python/python-check-for-float-string/

  if row["record_id"] is in accepted_ids (which means it was already passed during another iteration):
  add as reason for rejection "duplicate record_id"

  setting REASONS_ORDER to be [to order indicated in the instructions]

  creating reasons_sorted, all the rejection reasons obtained for each row in the order of REASON_ORDER

*source
  - https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
 -  wasn't working, asked AI why and itsuggested i add .index to the key 

OUTPUT: a tuple with: 
if valid record: a dictionary of the record followed by an empty list
if unvalid reocrd: none, followed by a list of the reason(s) why
=> tuple[dict[str, str] | None, list[str]]


#### 2. Process_records ####
INPUT: records (obtained from records = load(records)), format: rows: Iterable[dict[str, str]]
AIMS: Validate every record; stop and report an error for invalid input & identify exact duplicate records and keep one copy of each.
FUNCTION

Create accepted_records and invalid_records lists, and an accepted_ids set
For each record row, going through each row and starting at the second one:
  got through the cleaned record and pass it through the validate_records function (calling the output of this reasons)

  if cleaned_record was not rejected (is not None):
    then append this cleaned_record to the accepted_records list 

  else (if it was rejected):
    append this record to the invalid_records list, and put its record_id and the reason of rejection in dictionaries
  * sources
  https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
  https://realpython.com/nested-loops-python/
  
OUTPUT: Valid and invalid records lists. Format: tuple[list[dict[str, str]], list[dict[str, str]]]


#### 3. Summarise_oaks ####
INPUT: the validated records obtained through process_records. Format: (Iterable[dict[str, str]])
AIMS: Identifying all the oak species in the accepted records, counting the frequency of each species, and putting this into a list
FUNCTION:
for each row in clean_records 
  if the genus of that row (row[genus]), regardless of trailing whitespaces and casefold (.strip.casefold()), equals "quercus", then:
   append that row's species (removing casefold and stripping withespaces) to the oak_species list

  then, using Counter, create oak_counts which is a list where all the species of oak_species are listed with their respective counts 

then, return a list of dict with each species (in the species dict) and its respective freqeuncy (in the count dict) usig .items() 

OUTPUT: list of dictionaries of oak species and respective counts. Format: list[dict[str, str]]
*sources
- https://introcs-python.cs.luc.edu/dict_algorithms/overview.html
- https://www.geeksforgeeks.org/python/python-counter-items-counter-keys-and-counter-values/
- https://realpython.com/python-counter/
- https://www.geeksforgeeks.org/python/counters-in-python-set-1/
- https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
- Asked AI for help with structurin my function's return
- Asked AI to help with correcting indents


## ASSIGNMENT 3: R ##

AIMS: getting familiar with data wrangling and plotting in R. 

### Tree height practical ###

#### Part 1 ####

AIMS: checking trees data and calculating tree height, using tidyverse and already entered distance and angle data.

DETAILS: importing trees data and checking its formatting (missing values, NAs, if numeric values are finite, ranges of angles and distances,...). Then, using already inputted distances and angles, calculate tree height and adding it as a new column in the table (height_m). Checking that calculations were correct and saving the file in results as a cv.

INPUT: trees.csv from MQB/content/data

PSEUDOCODE FOR FUNCTION:
create a function check_trees where {
  the col_order is c("Species", "Distance.m", "Angle.degrees")
  if the column names from trees are not identical (!identical) to col_order {
    stop the command and state as a reason "wrong/headers/ header order"
  }
   for each col in num_col (num_col = Distance.m and Angle.degrees)
    if the are any NA values or (|) any empty strings {
      stop the command and state as a reason "missing", col}
    if any col values are not finite (!finite) {
    stop the command and state as a reason "invalid", col}
  if any trees$Distance_m value is outside of its range {
    stop the command and state as a reason "Distance_m out of range"}
  repeat last statement but for Angle.degrees range
  
  set trees to be trees where (%>%)
    a new column is created (mutate), called height_m and is equal to 
    Distance.m *tan(Angle.degrees * pi /180)) %>%
    and reorder (select) the columns to be: Species, Distance.m, Angle.degrees, height_m

  state the message "done!" after having done all this
  return trees}

Run command was: Rscript code/TreeHeight.R (from porject root Bash terminal)

OUTPUT: 
(1) script named TreeHeight.R stored in codes
(2) csv with the checked and modified data in results named TreeHts.csv
SOURCES:
-  https://www.statology.org/r-filter-between-two-values/
- https://dplyr.tidyverse.org/reference/filter.html
- if row missing https://www.geeksforgeeks.org/r-language/address-errors-in-if-statements-in-r/
- ordering columns: https://www.geeksforgeeks.org/r-language/reorder-the-column-of-dataframe-in-r-using-dplyr/
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/

#### Part 2 ####

AIMS: checking trees data and calculating tree height, using tidyverse and already inputted distance and angle data and by passing trees.csv as an argument.

DETAILS:running a similar code than in part 1 (file: get_treeHeight.R) ). However, this time passing the input data as an argument when running the code from the Bash terminal. Thus, the code first ensures that exactly one argument gets passed, and that that argument actually exists. It then goes through the function and some checks for the calculations. Lastly, the output gets saved in results as a csv, and its name is set to be the basename of the argument that was passed. 

Then, we created a shell script(file: run_get_TreeHeights.sh) with code to run the command in Bash, and terminate execution if the script fails. 

INPUT: trees.csv from MQB/content/data, passed as an argument

OUTPUT: 
(1) get_TreeHeight.R, script file that checks the argument, has the function,...
(2) run_get_TreeHeight.sh: a shell script has the command to run the get_TreeHeight.R script, and makes sure the command gets terminated if the script fails
(3) csv file with the checked and modified data, stored in results as <input-basename-without-.csv>_treeheights.csv

SOURCES:
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/
- asked AI to give me hint on how to tackle this, which led me to this website: https://maple60.github.io/en/posts/2026-02-06-r-extract-filename/
- asked AI for hint to remove.csv after basename, it suggested tools::file_path_sans_ext
- for terminating command if script fails: https://www.statology.org/reorder-columns-r/


### Pound hill practical ###

AIMS: wrangling pound hill data, calculating mean species richness at plots, blocks, and cultivation combinations, and plotting it.

DETAILS:  wrangling pound to convert blank spaces to observed zeros,transpose the data, convert table from wide to long format, and check counts (numeric, non-zero). Once data has been wrangled and coverted to a tibble, use %>% pipeline to modify it into a table that shows Cultivation, Plot, Quadrat, and Block and calculate richness at each of these combinations (richness here refers to number of species detected). Then use this table to find mean richness at each Cultivation, Block, and Plot combination. We then stored this table as a csv in the results folder, and used ggplot to create a figure of the mean species richness at each plot, in relation to cultivation. This plot was then saved as a pdf in the results folder of the root project. 

INPUT: pound_hill_data.csv and pound_hill_meta_data.csv from MQB/content/data

OUTPUT: 
(1) pound_hill_analysis.R: R script stored in project root codes folder
(2) pound_hill_plot_richness.csv: csv with the mean richness data at each cultivation, block, and plot combination. File stored in project root results folder.
(3) pound_hill_richness.pdf: figure of the mean species richness at each plot, in relation to cultivation. File stored in the project root results folder.

SOURCES: 
- https://www.geeksforgeeks.org/r-language/pivot-longer-in-r/
- https://gist.github.com/ramhiser/93fe37be439c480dc26c4bed8aab03dd
- https://ggplot2.tidyverse.org/reference/scale_manual.html
- https://www.r-bloggers.com/2025/03/how-to-center-ggplot-title-subtitle-and-caption-in-ggplot2-with-r/

