 # BOOTCAMP 

Chloe Soudan - MSc CMEE - chloe.soudan26@imperial.ac.uk

**Handbook**: https://mulquabio.github.io/MQB/intro.html

**Requirements**
- All scripts to be run in Bash terminal from the project root (except otherwise specified)
- Project root must have a "code", "data", and "results" folder. "Sandbox" folder is not necessary but helpful for storing practice scripts, dtaa, ...




## 1. Unix, Shell, and Git

### Aims 
Getting familiar with unix, shell scripting, and using GitHub repositories

### In-class scripts

> - variables.sh  
  Run with: ```bash code/variables.sh "two words"```
> - MyExampleScript.sh  
  Run with: ```bash code/MyExampleScript.sh```
> - boilerplate.sh  
  Run with: ```bash boilerplate.sh```
> - CheckLabel.sh  
  Run with:  ```bash code/CheckLabel.sh oak```
> - CountLines.sh  
  Run with: ```bash code/CountLines.sh "data/field notes.csv"```
> - ConcatenateTwoFiles.sh  
  Run with ```shell_practice=$(mktemp -d)  
  printf 'oak\n' > "$shell_practice/first.txt"
  printf 'pine\n' > "$shell_practice/second.txt"
  bash code/ConcatenateTwoFiles.sh "$shell_practice/first.txt" "$shell_practice/second.txt" "$shell_practice/combined.txt"```
> - tiff2_png.sh  
  Run with: ```shell_practice=$(mktemp -d)
  mkdir "$shell_practice/images"
  convert -size 100x100 xc:blue "$shell_practice/images/test.tif"
  bash code/tiff2_png.sh "$shell_practice"```



### Assignment 1: Unix and Shell
**Sources**:
- https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
- https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements


#### 1.1 Fasta exercises 

**Filename**: unixPrac1.txt   
**File format**: text file  
**How to run**: from project root using ```bash code/unixPrac1.txt```   

##### Aims
Using UNIX commands to inspect FASTA files and their contents.

##### Requirements
- FASTA folder from MQB repository (MQB/content/data/fasta). Data should be stored in the data folder of the project root
- VS Code (or equivalent environment that can run Unix and Bash terminal)

##### Workflow
1. Counting lines in three different FASTA files using: ``` wc -l ```
2. Displaying certain lines of a FASTA file using the ```tail``` command
3. Counting sequence length of FASTA file using the ```wc -c```
  - used ```-v "^>"``` and ```tr -d "\n"``` to remove lines starting with > and newline characters, respectively
4. Counting motif occurance in a FASTA file sequence using the ```grep -o``` command to set the desired motif, and ```wc -l``` to count the mathches
5. Calculating base rations in a FASTA file sequence using the 
``` ratio=$(echo "($a + $t) / ($c + $g)" | bc -l)``` command. 

##### Outputs
No output files, just printed resuls from the command

Note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code.


#### 1.2 Shell practical 

**Filename**: tabtocsv.sh  
**File type**: shell script  
**How to run**: from project root using ```
shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"
bash code/tabtocsv.sh "$shell_practice/test.txt"```  

##### Aims
Using shell scripting to improve a script converting a tab-delimited file to a comma-delimited one (csv)

##### Requirements
- tabtocsv.sh - Shell Scripting chapter 
- VS Code (or equivalent environment that can run Unix and Bash terminal)

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

##### Outputs
test.txt.csv (in results folder), test text file converted to csv 


#### 1.3 New script practical 

**Filename**: csvtospace.sh  
**File type**: shell script  
**How to run**: from project root using ```bash code/csvtospace.sh data/temperatures/1800.csv```

##### Aims
Using shell scripting to improve a script converting a comma-delimited file (csv)to a tab-delimited one. 

##### Required data
- Any csv file (here used 1800.csv, stored in temperatures folder in the project root's data folder - acquired from from MQB repository (MQB/content/data/temperatures))
- VS Code (or equivalent environment that can run Unix and Bash terminal)

##### Workflow

Adapted tabtocsv.sh to convert csv to tab (other way around).
Workflow follows exact same steps as [Shell practical](#2-shell-practical) except for Step 3 (Converting the text file to a CSV format). Here,
(1) instead of replacing the tabs with commas (```tr "\t" ","```), commas were replaced with tabs (```tr "," "\t"```),
(2) the file was stored as a text filed (```.txt```) instead of a csv file ```.csv``` .
> Code:
```
cat "$1" | tr "," "\t" >  "results/$(basename "$1").txt"
```
##### Outputs
 1800.csv.txt (in results folder), csv file that was converted to text format. can also be run with 1801-1803.csv.

##  2. Python

### Aims 
Getting familiar with coding in Python.

### In-class scripts
> - loops.py  
  Run with: ```python3 code/loops.py```
> - cfexercises1.py  
  Run with: ```python3 cfexercises1.py```
> - cfexercises2.py  
  Run with:```python3 cfexercises2.py```
> - MyExampleScript.py  
  Run with: ```python3 MyExampleScript.py```
> - boilerplate.py    
  Run with: ```python3 code/boilerplate.py```
> - using_name.py  
  Run with: ```python3 code/using_name.py```
> - sysargv.py  
  Run with: ```python3 code/sysargv.py oak12```
> - control_flow.py  
  Run with: ```python3 code/control_flow.py```
> - test_control_flow.py  
  Run with: ```python3 code/test_control_flow.py```
> - observations_practice.py  
  Run with: ```python3 code/observations_practice.py```
> - test_observations_practice.py  
  Run with: ```python3 code/test_observations_practice.py```
> - debugme.py  
  Run with: ```python3 code/debugme.py```  
  Note: this script was designed to have an error, as it is a debugging practice script


### Assignment 2

**Filenames**: clean_silwood_trees.py and test_silwood_trees.py
**File types**: python scripts 
**How to run**: python3 code/clean_silwood_trees.py and python3 code/test_silwood_trees.py

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
(5) Checking if the functions work correctly (in test_silwood_trees.py)

N.B: more precise instruction in silwood_trees_metadata

#### 2.1 Load_records - clean_silwood_trees.py

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

#### 2.2 Validated_records - clean_silwood_trees.py

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

N.B.: Specific instructions in silwood_trees_metadata

**Function**  
Defining (```def```) validate_record() where:
> Checking for missing fields  

  for each field in INPUT_FIELDS:  
  ```if``` that row's field (```row[field]```) has no content (```None```) or just empty spaces (```row[field].strip() == ""```). if it does then:
  add as reason (```reason.append()```) for rejection of that row "missing <field>
  otherwise (```else```) remove whitespaces of the valid records (```row[field] = row[field].strip()```
    **Sources**:
   -https://stackoverflow.com/questions/1278749/- - -how-do-i-detect-missing-fields-in-a-csv-file-in-a-pythonic-way

> Checking for invalid record ID  
  
  ```if``` the format of ```row[field]``` does not fully match the format (```nor re.fullmatch```) "ST" followed by three integers [0-9]{3} (```(r"ST[0-9]{3}", row["record_id"])```), then:
  add as reason for rejection of that row (```reasons.append()```): "invalid record_id"
  **Sources**:
https://stackoverflow.com/questions/64644087/python-validate-if-column-entries-match-a-desired-format
https://zetcode.com/python/regex-fullmatch-function/ 

> Checking for invalid location  

setting ```locations``` to be (```=```) the following list: ```["silwood bottom", "nash's field", "manor house","reactor wood"]```

 ```if``` the row's location name (```row[location]```), regardless of casefold (```.casefold()```) is not in in the set list of locations (```not in locations```), then:  
 add as reason for rejection of that row (```reasons.append()```): "invalid location"
  **Sources**:
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

  **Sources**: 
  -AI to get a hint on how to tackle this (tried to find is.numeric (R) equivalent in python), and it suggested to use float 
  -https://www.geeksforgeeks.org/python/python-check-for-float-string/


> Checking for duplicate records  

  ```if``` the row's record ID  ```row["record_id"]``` is in accepted_ids (which means it was already passed during another iteration):
  add as reason for rejection (```reasons.append()```) "duplicate record_id"

> Listing rejectionreasons in specific order  

  setting ```REASONS_ORDER``` to be (```=```) [the order indicated in the instructions]

  setting ```reasons_sorted``` to be (```=```) all the rejection reasons obtained for each row (```reasons```), and putting them in the order of REASON_ORDER (```key = REASONS_ORDER.index```)

**Sources**:
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

#### 2.3 Process_records - clean_silwood_trees.py

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
  **Sources**:
  https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
  https://realpython.com/nested-loops-python/

**Output**:  
Valid and invalid records lists. Format: tuple[list[dict[str, str]], list[dict[str, str]]]


#### 2.4 Summarise_oaks - clean_silwood_trees.py

**Input**:  
The validated records obtained through process_records (clean_records) 
Format: (Iterable[dict[str, str]]) 

**Aims**:  
Identifying all the oak species in the accepted records, counting the frequency of each species, and putting this into a list,

**Function**:

Creating an empty list ```oak_species``` (which will store the different oak species)

```for``` each row in ```clean_records```: 
  ```if``` that row's genus (```row[genus]```), regardless of trailing whitespaces and casefold (.strip.casefold()), is (```==```) "quercus", then:
   append that row's species (removing casefold and stripping withespaces) to the oak_species list

  Creating ```oak_counts```, a list listing all the oak_species pseices and their respective counts (using the ```Counter``` command)
  
  Returning a list of dictionaries with each species (in the species dictionary) and its respective frequenncy (in the count dictionary) usig ```.items()```

**Output**: list of dictionaries of oak species and respective counts. Format: list[dict[str, str]]  
 

**Sources**
- https://introcs-python.cs.luc.edu/dict_algorithms/overview.html
- https://www.geeksforgeeks.org/python/python-counter-items-counter-keys-and-counter-values/
- https://realpython.com/python-counter/
- https://www.geeksforgeeks.org/python/counters-in-python-set-1/
- https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
- Asked AI for help with structurin my function's return
- Asked AI to help with correcting indents

#### 2.5 Functions check - test_silwood_trees.py

- Importing the functions from clean_silwood_trees.py
- Testing validate_record() function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. Missing record_id | Created a record with an empty record_id, ran the validate_record on the record | (None, ['invalid record_id`]) | Output matched expectations, check successful. |
| 3. Invalid genus | Created a record with an invalid genus ran the validate_record on the record | (None, ['invalid genus`]) | Output matched expectations, check successful. |
| 4. Invalid species | Created a record with an invalid species, ran the validate_record on the record | (None, ['invalid species`]) | Output matched expectations, check successful. |
| 5. Invalid genus-species combination | Created a record with an invalid genus-species combination, ran the validate_record on the record | (None, ['invalid genus/species combination`]) | Output matched expectations, check successful. |
| 6. Distance out of range | Created records with out of range distances (at the boundaries: 0, 101). Also checked some valid distances (at the boundaries:1, 100). Ran the validate_record function on the records. | (None, ['distance_m out of range`]) (for invalid distances) and the printed record (for valid distances)| Output matched expectations, check successful. |
| 7. Angle out of range | Created records with out of range angles(at the boundaries: 0, 90). Also checked some valid distances (at the boundaries:1, 89). Ran the validate_record function on the records.| (None, ['angle_degrees out of range`]) (for invalid angles) and the printed record (for valid angles)| Output matched expectations, check successful. |
| 8. Order of error messages | Created record which should generate an error for each field, ran the validate_record function on the record | (None, ['missing record_id, 'invalid record_id', 'duplicate record_id', 'invalid location', 'invalid genus', 'invalid species', 'distance_m out of range', 'angle_degrees out of range']| Output matched expectations, check successful. |
| 9. Trailing spaces and case sensitivity | Created a record with added spaces and abnormal casing in the field inputs, ran the validate_record function on the record | The printed record (valid record)| Output matched expectations, check successful. 
| 10. Valid data | Created a record with valid field inputs, ran the validate_record function on the record | The printed record (valid record)| Output matched expectations, check successful.

- Testing process_records function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. Duplicate records | Created a data set with duplicate records, ran the process_records function on the record |Printed record of the first one, followed by 'reasons':'duplicate record' (accepted first record but not the duplicate| Output matched expectations, check successful. |
| 2. Outputs | Ran process_records on records data set |Accepted records as a list of discitonaries, invalid records printed as a list of dictionaries  with the record_id and the reasons for rejection| Output matched expectations, check successful. |

- Testing summaries_oaks function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. No oaks | Created a data set with no records having 'Quercus' genus, ran the summarise_oaks function on the data| [] (an empty list as there are no oaks)| Output matched expectations, check successful. |
| 2. Exact oak names | Created a data set with two  records having the exact same scientific oak names (Quercus robur). Ran process_records on the data set |[{species:'robur', count:2}] (list of dictionaries with oak species and count of the species)| Output matched expectations, check successful. |
| 3. Near match with oak names | Created a data set with a record having Quercus genus  (robur species) and another having typo in genus name (Quercuss)). Ran process_records on the data set|[{species:'robur', count:1}] (list of dictionaries with oak species and count of the species where the reocrd with the typo is not included)| Output matched expectations, check successful. |

## 3. R 
Getting familiar with coding in R.

### In-class scripts

**Required package**: tidyverse, reshape2

>- basic_io.R  
  Run with: ```Rscript code/basic_io.R```
>- boilerplate.R  
  Run script: ```Rscript code/boilerplate.R```
>- control_flow.R  
  Run with: ```Rscript code/control_flow.R```
>- r_conditionals.R  
  Run with: ```Rscript code/r_conditionals.R```
>- break.R  
  Run with: ```Rscript code/break.R```
>- next.R  
  Run with: ```Rscript code/next.R```
>- try.R  
  Run with: ```Rscript code/try.R```
>- browse.R  
  Run with: ```Rscript code/browse.R```
>- observations_practice.R  
  Run with: ```Rscript code/observations_practice.R```
>- data_wrang.R  
  Run with: ```Rscript code/data_wrang.R```
>- data_wrang_tidy.R  
  Run with: ```Rscript code/data_wrang_tidy.R```


### Assignment 3

#### 3.1 Tree height practical

**Filenames**: TreeHeight.R, get_TreeHeight.R, run_get_TreeHeight.sh
**File types**: R scripts and shell script
**How to run**: in bash terminal from project root: Rscript code/TreeHeight.R, Rscript code/get_TreeHeight.R data/trees.csv data/trees.csv, bash code/run_get_TreeHeight.sh

AIMS
getting familiar with data wrangling and plotting in R. 

SOFTWARE REQUIREMENTS
**Software**: VS code, or equivalent environment that can run **R**
**R Packages**: tidyverse

REQUIRED DATA AND SCRIPTS
trees.csv from MQB/content/data

SCRIPTS OVERVIEW
(1) Creating an R script (TreeHeight.R) containing functions that calculate tree height based on distance and angle and validate the input data, and that runs checks on these functions
(2) Creating a generalised TreeHeight script (get_TreeHeight.R) that uses the functions from TreeHeight.R to calculate tree height, and where the inptu csv can be specified upon running the script from the terminal
(3) Creating a shell script that runs the generalised R script with the trees.csv data as input

##### Part 1 - TreeHeight.R

**How to run**: Rscript code/TreeHeight.R

**Workflow**
- Loading the required libraries and data (```read.csv("data/trees.csv```)
- Inspecting the data 
- Creating a functions (```TreeHeight```) that calculates tree height using tree distance and angle as inputs
- Creating a function (```check_trees()```) that wrangles the data and calculates tree height for the contents of a data frames 
- Testing the functions using toy measurements and deliberately invalid data
- Conducted some debugging (when building the script) before calculating tree height in check_trees function (manual check of outputs)
- Running the check_trees function (```check_trees(trees)```) 
- Writing the outputs from the function into a csv file (```write.csv```)
- Running the code in Bash terminal from root project  (```Rscript code/TreeHeight.R```)


**TreeHeight() function**
>**Inputs**:  
 Angle.degrees (angle in degrees) and Distance_m  (distance in meters))
**Aims**:  
Calculating tree height using tree distance and angle as inputs  
**Function**: 
Converting  the angle from degrees to radians (```Angle.degrees * pi / 180```), computing the height (in meters, ```Distance_m * tan(angle_radians)```), and returning the computed tree height (```height_m```).  
**Outputs**:  
height_m

**check_trees() function**
>**Inputs**:  
data frame  
**Aims**:
validates measurements from tree data and calculates tree height using and already entered distance and angle data.    
**Function**:  
create a function ```check_trees``` where {
  the ```col_order``` is ```c("Species", "Distance_m", "Angle.degrees")```
  ```if``` the column names from trees are not identical (```!identical```) to col_order {
    ```stop``` the task and state as a reason "wrong/headers/ header order"
  }

  Distance_m and Angle.degrees columns from the data frame are converted to be numeric (```as.numeric```)

  A vector ```num_col``` containing (```<-```) ```c("Distance_m", "Angle.degrees")``` is created 

   ```for``` each col ```in num_col```
    ```if``` the are any NA values (```any(is.na())```) ```{```
      ```stop``` the command and state as a reason ```"Missing or non-numeric valus in", col}```
    ```if``` any col values are not finite (```!is.finite```) ```{```
    ```stop``` the command and state as a reason ```"invalid", col}```
  ```if``` any ```trees$Distance_m``` value is outside of its range ```{```
    ```stop``` the command and state as a reason ```"Distance_m out of range"}```
  repeat last statement but for Angle.degrees range
  
  set ```trees``` to be (```<-```) ```trees``` where (```%>%``)
    a new column is created (```mutate```), called ```height_m``` and is equal to ```height_m``` obtained from running the ```TreeHeight``` function on ```(Angle.degrees, Distance_m)```
    and reorder (```select```) the columns to be: ```(Species, Distance.m, Angle.degrees, height_m)```

  state the ```message``` "done!" after having done all this
  ```return``` output data frame```}```  
**Outputs**:  
data frame with height_m column and values  


**Testing the functions**
- Testing the TreeHeight() function 

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| TreeHeight() function | Created a toy_measurement with a distance of 8 metres and an angle of 45 degrees, calculated the expected tree height manually, then passed the same distance and angle to the TreeHeight() function and compared the results. | Both calculations should return a tree height of 8 metres. | Both returned a height of 8 metres, check successful. |


- Testing the check_trees() function


| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. Column order | Created a trees data frame but with wrong column order, ran the check_trees function on the data frame. | Error: "wrong headers/header order" | Output matched expectations, check successful. |
| 2. Column names | Created a trees data frame with wrong column names, ran the check_trees function on the data frame. | Error: "wrong headers/header order" | Output matched expectations, check successful. |
| 3. Missing values | Created a data frame with missing Distance_m values, ran the check_trees function on the data frame. | Error: "Missing or non-numeric values in Distance_m" | Output matched expectations, check successful. |
| 4. Infinite values | Created a data frame with Inf as Distance_m, ran the check_trees function on the data frame. | Error: "invalid Distance_m" | Output matched expectations, check successful. |
| 5. Non-numeric values | Created a data frame with "abc" as Distance_m input, ran the check_trees function on the data frame. | Error: "Missing or non-numeric values in Distance_m" | Output matched expectations, check successful. |
| 6. Out of range Distance_m | Created data frames with out of range Distance_m values (at the edges of the boundaries: 0 and 101), ran the check_trees function on the data frame. Also checked some valid Distance_m values. | Error: "Distance_m out of range" for invalid values. (for invalid distance)Valid values accepted (for valid distances). | Output matched expectations, check successful. |
| 7. Out of range Angle.degrees | Repeated the same as out of range Distance_m check but with edge angle.degrees boundaries (0 and 90). | Error: "Angle.degrees out of range" | Output matched expectations, check successful. |
| 8. Running check_trees | Ran check_trees on the trees data set and inspected results using dim(). | Output should contain 120 rows and 4 columns. | Output matched expectations, check successful. |
| 9. Checking calculated height | Compared manually calculated Populus tremula height with height calculated using TreeHeight (rounded values). | Expected values to match and print "correct height". | Output matched expectations, "correct height" printed, check successful. |

**Outputs**:
(1) script named TreeHeight.R stored in code
(2) csv with the checked and modified data in results named TreeHts.csv

*Sources:
-  https://www.statology.org/r-filter-between-two-values/
- https://dplyr.tidyverse.org/reference/filter.html
- if row missing https://www.geeksforgeeks.org/r-language/address-errors-in-if-statements-in-r/
- ordering columns: https://www.geeksforgeeks.org/r-language/reorder-the-column-of-dataframe-in-r-using-dplyr/
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/
-  https://www.w3schools.com/r/r_for_loop.asp


##### Part 2 - get_TreeHeight.R
**How to run**: Rscript code/get_TreeHeight.R data/trees.csv  

**Aims**
Checking trees data and calculating tree height, using tidyverse and already inputted distance and angle data and by passing trees.csv as an argument.

**Workflow**
- Load the required libraries
- Import functions from TreeHeight.R using ```source()```
- Creating an args() function that verifies that exactly one valid argument is being passed 
- Reading the argument as a CSV file and storing it as ```trees1```
- Running the ```check_trees()``` function (from TreeHeight.R) on trees1
- Inspecting the results
- Writing the results into a CSV file  by first creating a results folder (if it doesn't exist already), naming the file based on its ```basename```, and then writing it as a CSV (```write.csv```) in the results folder and name 'basename'_treeheights.csv
- Running the script in Bash terminal from the project root, using trees.csv as the argument, using the following command: ```Rscript code/get_TreeHeight.R data/trees.csv

**args() function**
>**Inputs**:
one argument (path to CSV file)  
**Aims**: checking that the amount of valid arguments being passed is exactly 1  
**Function**:
get command line arguments (```commandArgs```) and store them in args
  ```if``` the number of arguments is (```==```) 0:
    ```stop``` the task and print "No argument provided"
  ```if``` the number of arguments is larger than 1:
    ```stop``` the task and print "Too many arguments provided"
  ```if``` the file does not exist:
    ```stop``` the task and print "Missing file"
  ```if``` file is not readable:
    ```stop``` the task and print "File is not readable"  
**Outputs**:  
if argument is valid, CSV is accepted and can be used    
if argument is not valid, error message gets printed and task gets terminated 

**Testing the function**

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. No argument provided | Ran the fucntion without adding an argument with the following command: ```Rscript code/get_TreeHeight.R``` | Error: "No argument provided", termination of the task | Output matched expectations, check successful. |
| 2. Too many arguments provided | Ran the function inputting two arguments with following command: ```Rscript code/get_TreeHeight.R data/trees.csv data/trees.csv``` | Error: "too many arguments provided", termination of the task | Output matched expectations, check succesful. |
| 3. Missing file | Ran the function with as argument a file that doesnt exist using the following command: ```Rscript code/get_TreeHeight.R  data/doesnotexist.csv``` | Error: "Missing file", termination of the task | Output matched expectations, check succesful. |
| 4. Directory instead of file | Ran the function with as argument a directory instead of a file that doesnt exist using the following command: ```Rscript code/get_TreeHeight.R  data/``` | Error: "Missing file", termination of the task | Output matched expectations, check succesful. |
| 5. Unreadable file | Created an unreadble file and ran the function with as argument the unerable file, using the following commands: ```touch data/unreadable.csv```,  ```chmod 000 data/unreadable.csv```, ```Rscript code/get_TreeHeight.R data/unreadable.csv``` | Error: "File is not readable, termination of the task | Output matched expectations, check succesful. |



**Outputs**
(1) script named get_TreeHeight.R stored in code
(2) csv file named 'basename'_treeheights.csv


##### Part 3 - run_get_TreeHeight.R
**How to run**:bash code/run_get_TreeHeight.sh

Shell script(file: run_get_TreeHeights.sh) with code to run the command in Bash, and terminate execution if the script fails. 

**Outputs**:

(1) get_TreeHeight.R, script file that checks the argument, has the function,...
(2) run_get_TreeHeight.sh: a shell script has the command to run the get_TreeHeight.R script, and makes sure the command gets terminated if the script fails
(3) csv file with the checked and modified data, stored in results as <input-basename-without-.csv>_treeheights.csv

*Sources:
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/
- asked AI to give me hint on how to tackle this, which led me to this website: https://maple60.github.io/en/posts/2026-02-06-r-extract-filename/
- asked AI for hint to remove.csv after basename, it suggested tools::file_path_sans_ext
- for terminating command if script fails: https://www.statology.org/reorder-columns-r/


#### 3.2 Pound hill practical 

**Filenames**: pount_hill_analysis.R  
**File types**: R scripts  
**How to run**: Rscript code/pound_hill_analysis.R (from project root in Bash terminal)

AIMS
Wrangling pound hill data, calculating mean species richness at plots, blocks, and cultivation combinations, and plotting it.

SOFTWARE REQUIREMENTS
VS cde (or equivalent environment that can run R)

REQUIRED DATA AND SCRIPTS
From MQB repostiory into own repository: 
from content/data to project root data folder
    - pound_hill_data.csv
    - pound_hill_metadata.csv
 
 *Files are now in GitHub repository data folder
  
WORKFLOW
(1) Loading the required libraries  
(2) Loading the data and metadata  
(3) Inspecting the data using ```head```, ```str```, and ```dim``` commands to investigate first lines of the data, its structure, and its dimensions respectively.  
(4) Wrangling the data:  
- Converting blank spaces to observed 0s (```data[data==""]=0```)
- Transposing the data (```data <- t(data)```)
- Converting data matrix to data frame (```as.data.frame```) and converting the obtained table from wide format to long formate (```pivot_longer()```)
- Setting fields as class factor (```as.factor```), except for Count that was set to class integer (```as.integer```)

(5) Validating that the counts are   
- not missing and numeric (```if(any(is.na(){}```)
- non-negative  (```if(any(COUNTDATA <0) {}```)
N.B.: when count data was non-numeric, as.integer would have coerced it into NA. Thus, non-numeric counts will get flagged by ```is.na``` check.
(6) Testing the data validation checks by creating fake counts and passing them through the checks:  


| Test | Input | Workflow | Expected outputs | Succesful output |
|---|---|---|---|---|
| a. Missing counts | `c("1", "2", "")` | Created vector with a missing count, converted it to class integer, ran `if (any(is.na(na_count))) {print("Error: Missing or non-numeric count detected")}` | Error: Missing or non-numeric count detected | Outputs matched expectations, check succesful. |
| b. Non-numeric counts | `c("1", "2", "abc")` | Created vector with a non-numeric count, converted it to class integer, ran `if (any(is.na(non_numeric_count))) {print("Error: Missing or non-numeric count detected")}` | Error: Missing or non-numeric count detected | Outputs matched expectations, check succesful. |
| c.Negative counts | `c("1", "2", "-1")` | Created vector with a negative count, converted it to class integer, ran `if (any(negative_count < 0)) {print("Error: Negative counts detected")}` | Error: Negative counts detected | Outputs matched expectations, check succesful. |
| d. Valid counts | `c("1", "2", "1")` | Created vector with valid counts, converted it to class integer, ran the if statements on them | Return nothing (meaning counts passed the validation check) | Outputs matched expectations, check succesful. |

(7) Reinspecting the data with the ```head```, ```str```, and ```dim``` commands  
(8) Calculating mean species richness by using ```%>%``` pipeline to modify it into a table that shows Cultivation, Plot, Quadrat, and Block
and calculate richness at each of these combinations (richness here refers to number of species detected)  
(9) Creating a figure, using ```ggplot```, showing the mean species richness at each plot, in relation to cultivation  
(10) Saving the results using as "pound_hill_plot_richness.csv" (```write.csv()```) and the figure as "pound_hill_plot_richness.pdf"  (```pdf()```)  
(11) Interpretating of the plot.  

N.B. Ran the script twice to make sure it was reproducible.  

OUTPUTS
 
(1) pound_hill_analysis.R: R script stored in project root codes folder  
(2) pound_hill_plot_richness.csv: csv with the mean richness data at each cultivation, block, and plot combination. File stored in project root results folder.  
(3) pound_hill_plot_richness.pdf: figure of the mean species richness at each plot, in relation to cultivation. File stored in the project root results folder.  

SOURCES
- https://www.geeksforgeeks.org/r-language/pivot-longer-in-r/
- https://gist.github.com/ramhiser/93fe37be439c480dc26c4bed8aab03dd
- https://ggplot2.tidyverse.org/reference/scale_manual.html
- https://www.r-bloggers.com/2025/03/how-to-center-ggplot-title-subtitle-and-caption-in-ggplot2-with-r/

## AI use
For these assignemts, I used ChatGPT and copilot to understand error messages, debug scripts, and get hints on how to go further.




