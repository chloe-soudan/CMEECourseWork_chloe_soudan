 # BOOTCAMP 

Chloe Soudan - MSc CMEE - chloe.soudan26@imperial.ac.uk

Based on BOOK!!!!!!! XXXX

## Unix, Shell, and Git

### Aims 

Getting familiar with unix, shell scripting, and using GitHub repositories

### In-class scripts
> - variables.sh
> - MyExampleScript.sh
> - boilerplate.sh
> - CheckLabel.sh
> - CountLines.sh
> - ConcatenateTwoFiles.sh
> - tiff2_png.sh

### Assigment 1 

#### Aims
1. Using UNIX commands to inspect FASTA files and their contents. 
2. Using shell scripting to improve a script converting a tab-delimited file to a comma-delimited one (csv).
3. Using shell scripting to improve a script converting a comma-delimited file (csv)to a tab-delimited one. 

#### Software requirements 
VS Code (or equivalent environment that can run Unix and Bash terminal).

#### External sources
- https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
- https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements


#### 1. Fasta exercises 

**Filename**: unixPrac1.txt   
**File format**: text file  
**How to run**: from project root using ```bash code/unixPrac1.txt```   

##### Required data
FASTA folder from MQB repository (MQB/content/data/fasta). Data should be stored in the data folder of the project root. 

##### Workflow
1. Counting lines in three different FASTA files using: ``` wc -l ```
2. Displaying certain lines of a FASTA file using the ```tail``` command
3. Counting sequence length of FASTA file using the ```wc -c```
  - used ```-v "^>"``` and ```tr -d "\n"``` to remove lines starting with > and newline characters, respectively
4. Counting motif occurance in a FASTA file sequence using the ```grep -o``` command to set the desired motif, and ```wc -l``` to count the mathches
5. Calculating base rations in a FASTA file sequence using the 
``` ratio=$(echo "($a + $t) / ($c + $g)" | bc -l)``` command. 


Note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code.


#### 2. Shell practical 

**Filename**: tabtocsv.sh  
**File type**: shell script  
**How to run**: from project root using ```bash code/tabtocsv.sh "$shell_practice/test.txt"```  

Note: need to first run following lines in terminal:
```shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"
```


##### Required data 
- tabtocsv.sh - Shell Scripting chapter 

##### Workflow

Worked through provided scripts and removed redudancies, unnecessary steps, and optimized the provided script.

Final script workflow:
1. Terminating the script when input is more than one readable path
> if the number of inputs (```$~"```) is not equal to 1 (```-ne 1```); then an error message is printed to standard error (```>&2```) and the script is terminated with exit status 2.  

2. Terminating the script when input is unreadable or invalid
> if script is not valid (```! -f "$1"```) or (```|```) not readable (```! -r "$1"```); then an error message is printed to standard erroor and the script is terminated with exit status 2. 

3. Converting the text file to a CSV format

>Reading the input file (```cat "$1$```), converting its tabs with commas (```tr "\t" ","```), and writing it (```>```) as a .csv output file in the results folder.  
> Code:
```
cat "$1" | tr "\t" "," >  "results/$(basename "$1").csv"
```
  
4.  Printing a completion message at the end of the script to mark that it has been completed (```echo "done"```)


#### 3. New script practical 

**Filename**: csvtospace.sh  
**File type**: shell script  
**How to run**: from project root using ```bash code/csvtospace.sh data/temperatures/1800.csv```


##### Required data
- Any csv file (here used 1800.csv, stored in temperatures folder in the project root's data folder - acquired from from MQB repository (MQB/content/data/temperatures))

##### Workflow

Adapted tabtocsv.sh to convert csv to tab (other way around).
Workflow follows exact same steps as [Shell practical](#2-shell-practical) except for Step 3 (Converting the text file to a CSV format). Here,
(1) instead of replacing the tabs with commas (```tr "\t" ","```), commas were replaced with tabs (```tr "," "\t"```),
(2) the file was stored as a text filed (```.txt```) instead of a csv file ```.csv``` .
> Code:
```
cat "$1" | tr "," "\t" >  "results/$(basename "$1").txt"
```


##  Python

### Aims 

Getting familiar with coding in Python.

### In-class scripts
> - loops.py
> - cfexercises1.py
> - cfexercises2.py
> - MyExampleScript.py
> - boilerplate.py
> - using_name.py
> - sysargv.py
> - control_flow.py
> - test_control_flow.py
> - observations_practice.py
> - test_observations_practice.py
> - debugme.py

### Assignment 2

**Filenames**: clean_silwood_trees.py and test_silwood_trees.py
**File types**: python scripts 
**How to run**: XXXX

#### Aims 

Completing the clean_silwood_trees.py script (from MQB repository) functions so that running the script results in the creation of a cleaned record(csv file) of the trees data (stored locally in results folder of the project root, not on the GitHub repository), along with a record of invalid rows and their respective issues (csv file), and a file listing all the oak species encountered and their respective counts. 

#### Software requirements 
VS Code (or equivalent environment that can run Python)

#### Required data and scripts
From MQB repostiory into own repository: 
(1) from content/data to project root data folder
    - silwood_trees_raw
    - silwood_trees_metadata
(2) from content/code to project root code folder
    - clean_silwood_trees
(3) To create within project root code folder:
    - test_silwood_trees 

#### Workflow

(1) Creating a function (load_records) that reads the CSV input file 
(2) Creating a function (validate_records) that checks whether a row is valid, and if not, returns why it isn't (error message)  
(3) Creating a function (process_records) that repeats the validation step for the whole survey   
(4) Creating a function (summarise_oaks) that, using only the valid records, summarises the oak species encountered and their respective counts  
(5) Checking if the functions work correctly.  

##### 1. Load_records 

**Input**: path to a file (here INPUT_PATH)  
**Aims**: loading the CSV input, checking its field names, and returning one dictionary per row  
**Function**: function from MQB file, left untouched   
**Output**: list of dictionaries   
**Code**:

```
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
```

##### 2. Validated_records 

**Input**: 
- a dictionary of the data of one row (record, ```row:dict[str,str]```)
- the source row (```source_row:int```)
- set of accepted IDs (```accepted_ids:set[str]```)

**Aims**

- ordinary text cleaning
- Removing row if: 
  - missing or unrecognised values found
  - invalid record ID, location, genus, species, genus-species combination
  - measurements are outside allowed range
  - it is a duplicate
- Listing reasons for row rejection in specific order
- Returning accepted rows or reasons for rejection (if rejected)

**Function**  
Defining (```def```) validate_record() where:
> Checking for missing fields  

  for each field in INPUT_FIELDS:  
  ```if``` that row's field (```row[field]```) has no content (```None```) or just empty spaces (```row[field].strip() == ""```). if it does then:
  add as reason (```reason.append()```) for rejection of that row "missing <field>
  otherwise (```else```) remove whitespaces of the valid records (```row[field] = row[field].strip()```
    *sources:
   -https://stackoverflow.com/questions/1278749/- - -how-do-i-detect-missing-fields-in-a-csv-file-in-a-pythonic-way

> Checking for invalid record ID  
  
  ```if``` the format of ```row[field]``` does not fully match the format (```nor re.fullmatch```) "ST" followed by three integers [0-9]{3} (```(r"ST[0-9]{3}", row["record_id"])```), then:
  add as reason for rejection of that row (```reasons.append()```): "invalid record_id"
  *sources:
https://stackoverflow.com/questions/64644087/python-validate-if-column-entries-match-a-desired-format
https://zetcode.com/python/regex-fullmatch-function/ 

> Checking for invalid location  

setting ```locations``` to be (```=```) the following list: ```["silwood bottom", "nash's field", "manor house","reactor wood"]```

 ```if``` the row's location name (```row[location]```), regardless of casefold (```.casefold()```) is not in in the set list of locations (```not in locations```), then:  
 add as reason for rejection of that row (```reasons.append()```): "invalid location"
  *sources: 
  -https://www.geeksforgeeks.org/python/python-string-casefold-method


> Checking for invalid genas and species  

Repeat the same as in invalid record but for set list of valid genii and species.

> Checking for invalid genus-species combinations  

setting ```valid_combinations``` to be (```=```) a list (```[]```) of valid genus-species combinations,

  ```if``` ```row["genus"]``` and ```row["species"]```, regardless of casefold (```.casefold```) were considered valid individually, but that ```(row["genus"].casefold(), row["species"].casefold()```) combination is ```not in valid_combinations``` list, then:
  add as reason for rejection of that row (```reasons.append```()): "invalid genus/species combination"  

> Checking for invalid numerical fialds of range values  

setting ```NUMERIC_FIELDS```  to be (```=```)  ```"distance_m" and "angle_degrees"```

  creating a loop where ```for``` each ```field in NUMERIC_FIELDS:```
  ```if``` that ```row[field]``` is empty (```None```) or just made of empty spaces (```row[field].strip() == ""```): 
  skip the following chunk (```continue```) 
  if not, ```try``` to create a float string from row[field] and name it value (```value = float(row[field])```).

  ```if``` value is ```not``` mathematically finite (```math.isfinite```):
  add as reason for rejection of that row (```reasons.append()```): "invalid {field}"  

  otherwise (```else```, field is mathematically finite),  
    ```if``` field is (```==```) distance_m:  
          ```if``` value not greater than 0 or greater than 100 (```value <= 0 or value > 100```): 
        add as reason for rejection of the row (```reasons.append()```): "distance_m out of range"  
    ```if``` field is (```==``) angle_degrees:  
          ```if``` value not greater than 0 or larger than 90 (```value <= 0 or value >=90```):
        add as reason for rejection of the row (```reasons.append()```): "angle_degrees out of range"

  when converting to float fails (```except ValueError)```:
  add as reason for rejection of that row "invalid {field}

  *sources: 
  -AI to get a hint on how to tackle this (tried to find is.numeric (R) equivalent in python), and it suggested to use float 
  -https://www.geeksforgeeks.org/python/python-check-for-float-string/


> Checking for duplicate records  

  ```if``` the row's record ID  ```row["record_id"]``` is in accepted_ids (which means it was already passed during another iteration):
  add as reason for rejection (```reasons.append()```) "duplicate record_id"

> Listing rejectionreasons in specific order  

  setting ```REASONS_ORDER``` to be (```=```) [the order indicated in the instructions]

  setting ```reasons_sorted``` to be (```=```) all the rejection reasons obtained for each row (```reasons```), and putting them in the order of REASON_ORDER (```key = REASONS_ORDER.index```)

*sources:
  - https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
 -  wasn't working, asked AI why and itsuggested i add .index to the key 

> Returning the output 

  ```if``` there were reasons for rejection:  
    return ```None``` followed by the reasons for rejection (in order)

  otherwise, add the record ID to accepeted_ids and return the row


**Output**
a tuple with: 
if valid record: a dictionary of the record followed by an empty list
if unvalid reocrd: none, followed by a list of the reason(s) why
=> tuple[dict[str, str] | None, list[str]]

**Code**:
```
def validate_record( 
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Clean one record, or return the reasons it cannot be used."""
    reasons = [] #creating an empty list that will store reason for rejection
    #checking for missing fields 
    for field in INPUT_FIELDS:
        if row[field] is None or row[field].strip() == "":
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

```

##### 3. Process_records 

**Input**:  
Records (obtained from records = load(records)), format: rows: Iterable[dict[str, str]]

**Aims**:  

Validate every record of a file; stop and report an error for invalid input & identify exact duplicate records and keep one copy of each.

**Function**:  

Create empty ```accepted_records``` and ```invalid_records``` lists

Create an empty ```accepted_ids``` set. 

```for``` each record in rows, starting at the second row (```row in enumerate(rows, start = 2```):

  pass the current row, its row number, and ```accepted_ids```through the validate_record() function and store the returned record in ```cleaned_record``` and any rejection reasons in ```reasons```.
  
  ```if``` ```cleaned_record``` is valid (```not None```), append it to ```accepted_records``` (```accepted_records.append(cleaned_record)```)

  ```else``` (if it was rejected):
    append a dictionary to the invalid_records list, contaning its record_id and the reason of rejection

end of loop

  ```return``` ```accepted_records``` and ```invalid_records```
  * sources
  https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
  https://realpython.com/nested-loops-python/

**Output**:  
Valid and invalid records lists. Format: tuple[list[dict[str, str]], list[dict[str, str]]]

**Code**:  
``` 
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

```

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

SOFTWARE REQUIREMENTS: VS cde (or equivalent environment that can run R)

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

