 # BOOTCAMP 

Chloe Soudan - MSc CMEE - chloe.soudan26@imperial.ac.uk

**Handbook**: MulQuaBio handbook (https://mulquabio.github.io/MQB/intro.html)

## Contents  
1. [Unix, Shell, and Git](#1-unix-shell-and-git)
2. [Python](#2-python)
3. [R](#3-r)

## Project structure
CMEECourseWork  
├── code/      # folder with the in-class and assignment scripts  
├── data/      # folder with the data files needed to run code scripts  
├── results/  # contents are not tracked, will contain output files from code scripts after running them  
├── Feedback/  # assignment feedbacks  
├── README.md  
└── sandbox/   # not committed, practice data, codes, etc  

All scripts to be run in Bash terminal from the project root (except otherwise specified).



# 1. Unix, Shell, and Git
Getting familiar with unix, shell scripting, and using GitHub repositories

## In-class scripts
> - variables.sh  
  Run with: ```bash code/variables.sh "two words"```
> - MyExampleScript.sh  
  Run with: ```bash code/MyExampleScript.sh```
> - boilerplate.sh  
  Run with: ```bash code/boilerplate.sh```
> - CheckLabel.sh  
  Run with:  ```bash code/CheckLabel.sh oak```
> - CountLines.sh  
  Run with: ```bash code/CountLines.sh data/"field notes.csv"```
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


## Assignment 1: Unix and Shell

### 1.1 Fasta exercises 
**Filename**: unixPrac1.txt   
**File format**: text file  
**How to run**: from project root using ```bash code/unixPrac1.txt```   

#### Aims
Using UNIX commands to inspect FASTA files and their contents.

#### Requirements
- FASTA folder from MQB repository (MQB/content/data/fasta). Data should be stored in the data folder of the project root
- VS Code (or equivalent environment that can run Unix and Bash terminal)

#### Workflow
(1) Counting lines in three different FASTA files using: ``` wc -l ```
(2) Displaying certain lines of a FASTA file using the ```tail``` command
(3) Counting sequence length of FASTA file using the ```wc -c```
   used ```-v "^>"``` and ```tr -d "\n"``` to remove lines starting with > and newline characters, respectively
(4) Counting motif occurence in a FASTA file sequence using the ```grep -o``` command to set the desired motif, and ```wc -l``` to count the matches
(5) Calculating base ratios in a FASTA file sequence using the 
``` ratio=$(echo "($a + $t) / ($c + $g)" | bc -l)``` command. 

#### Outputs
No output files, just printed results from the command

Note: used AI for help on assembling parts of tasks (like wc -l, grep -v,...) into one line of code.


### 1.2 Shell practical 
**Filename**: tabtocsv.sh  
**File type**: shell script  
**How to run**: from project root with ```shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"```
and then ```bash code/tabtocsv.sh "$shell_practice/test.txt"```  

#### Aims
Using shell scripting to improve a script converting a tab-delimited file to a comma-delimited one (csv)

#### Requirements
- tabtocsv.sh - Shell Scripting chapter 
- VS Code (or equivalent environment that can run Unix and Bash terminal)

#### Workflow
Worked through provided scripts and removed redundancies, unnecessary steps, and optimized the provided script.
(1)Terminating the script when input is more than one readable path
> if the number of inputs (```$~"```) is not equal to 1 (```-ne 1```); then an error message is printed to standard error (```>&2```) and the script is terminated with exit status 2.  
(2) Terminating the script when input is unreadable or invalid
> if script is not valid (```! -f "$1"```) or (```|```) not readable (```! -r "$1"```); then an error message is printed to standard error and the script is terminated with exit status 2. 
(3)Converting the text file to a CSV format
>Reading the input file (```cat "$1$```), converting its tabs with commas (```tr "\t" ","```), and writing it (```>```) as a .csv output file in the results folder.  
(4) Printing a completion message at the end of the script to mark that it has been completed (```echo "done"```)

#### Outputs
test.txt.csv (in results folder), test text file converted to csv 


### 1.3 New script practical 
**Filename**: csvtospace.sh  
**File type**: shell script  
**How to run**: from project root using ```bash code/csvtospace.sh data/temperatures/1800.csv``` (input file can be any csv file, so could replace with data/temperature/1901.csv etc)

#### Aims
Using shell scripting to improve a script converting a comma-delimited file (csv) to a tab-delimited one. 

#### Required data
- Any csv file (here used 1800.csv, stored in temperatures folder in the project root's data folder - acquired from MQB repository (MQB/content/data/temperatures))
- VS Code (or equivalent environment that can run Unix and Bash terminal)

#### Workflow
Adapted tabtocsv.sh to convert csv to tab (other way around).
Workflow follows exact same steps as [Shell practical](#2-shell-practical) except for Step 3 (Converting the text file to a CSV format). Here,
(1) instead of replacing the tabs with commas (```tr "\t" ","```), commas were replaced with tabs (```tr "," "\t"```),
(2) the file was stored as a text file (```.txt```) instead of a csv file ```.csv``` .

#### Outputs
 1800.csv.txt (in results folder), csv file that was converted to text format. can also be run with 1801-1803.csv.

#  2. Python

**Aims**
Getting familiar with coding in Python.

## In-class scripts - python
> - loops.py  
  Run with: ```python3 code/loops.py```
> - cfexercises1.py  
  Run with: ```python3 code/cfexercises1.py```
> - cfexercises2.py  
  Run with:```python3 code/cfexercises2.py```
> - MyExampleScript.py  
  Run with: ```python3 code/MyExampleScript.py```
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
  Note: this script was designed to have an error, as it is a debugging practice script. Practiced with debugger in ipython3 and added breakpoint() before error to explore these tools.


## Assignment 2

**Filenames**: clean_silwood_trees.py and test_silwood_trees.py  
**File types**: python scripts   
**How to run**: ```python3 code/clean_silwood_trees.py``` and ```python3 code/test_silwood_trees.py```  

### Aims 
Completing the clean_silwood_trees.py script (from MQB repository) functions so that running the script results in the creation of a cleaned record(csv file) of the trees data (stored locally in results folder of the project root, not on the GitHub repository), along with a record of invalid rows and their respective issues (csv file), and a file listing all the oak species encountered and their respective counts. 

### Software requirements 
VS Code (or equivalent environment that can run Python)


### Required data and scripts
From MQB repository into own repository: 
(1) from content/data to project root data folder
    - silwood_trees_raw
    - silwood_trees_metadata
(2) from content/code to project root code folder
    - clean_silwood_trees
(3) To create within project root code folder:
    - test_silwood_trees 
  

### Workflow
(1) Creating a function (load_records) that reads the CSV input file 
(2) Creating a function (validate_records) that checks whether a row is valid, and if not, returns why it isn't (error message)  
(3) Creating a function (process_records) that repeats the validation step for the whole survey   
(4) Creating a function (summarise_oaks) that, using only the valid records, summarises the oak species encountered and their respective counts  
(5) Checking if the functions work correctly (in test_silwood_trees.py)

N.B: more precise instruction in silwood_trees_metadata

### 2.1 load_records - clean_silwood_trees.py

**Input**: path to a file (here INPUT_PATH)  
**Aims**: loading the CSV input, checking its field names, and returning one dictionary per row  
**Function**: function from MQB file, left untouched   
**Output**: list of dictionaries   

### 2.2 validate_record - clean_silwood_trees.py
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
  Defining validate_record() where:
  > Checking for missing fields  
  - looping through INPUT_FIELDS 
  - ```if``` ```row[field]``` is ```None``` or empty (```row[field].strip() == ""```), appending "missing <field>" to reasons
  - otherwise, stripping surrounding from the field 
  > Checking for invalid record ID  
  - checking ```if``` row["record_id"] matches r"ST[0-9]{3}" format using ```not re.fullmatch```  
  - if it doesn't, appending "invalid_record_id" to reasons for rejection
  > Checking for invalid location  
  - setting a list of valid locations
  - checking ```if``` row[location], regardless of casefold, doesn't belong (```not in``` to the set list of locations
  - if not, appending "invalid location" to reasons for rejection
  > Checking for invalid genus and species  
  - Repeating the same as in invalid record but for set list of valid genera and species.
  > Checking for invalid genus-species combinations  
  - setting a list of valid genus-species combinations
  - ```if``` genus and species were previously accepted, checking    if the combination doesn't belong (```not in```) to the set   list of combinations 
  - if it doesn't appending "invalid genus/species combination"to reasons for rejection 
  > Checking for invalid numerical fields of range values 
  - looping through numeric fields (distance_m and angle_degrees)
  - ```if``` that row[field] is empty or empty, skip to the following statement
  - if it isn't, ```try``` to create a float string from row[field] and name it value (```value = float(row[field])```)
  - if float is non-finite (```not math.isfinite```), appending "invalid {field}" to reasons for rejection
  - otherwise (field is mathematically finite) checking the ranges (distance_m greater than 0 but no greater than 100, angle_degrees greater than 0 but less than 90)
  - if values are outside of the range, appending "invalid {field} to reasons for rejection
  - Failed float conversions handled with except ValueError
  > Checking for duplicate records  
  -  ```if```  ```row["record_id"]``` is in accepted_ids (which means it was already passed during another iteration), appending "duplicate record_id" to reasons for rejection
  > Listing rejection reasons in specific order  
  - setting REASONS_ORDER (the order in which rejection reasons should be printed according to the instructions)
  - using ```key = REASONS_ORDER.index```) to order each row's reasons for rejection
  > Returning the output 
  - ```if``` there were reasons for rejection, return ```None``` followed by the reasons for rejection (in order)
  - otherwise, add the record ID to accepted_ids and return the row

**Output**
a tuple with: 
if valid record: a dictionary of the record followed by an empty list
if invalid record: none, followed by a list of the reason(s) why
=> tuple[dict[str, str] | None, list[str]]

### 2.3 Process_records - clean_silwood_trees.py

**Input**:  
Records (obtained from records = load(records)), format: rows: Iterable[dict[str, str]]  
**Aims**:  
Validate every record of a file; stop and report an error for invalid input & identify exact duplicate records and keep one copy of each.  
**Function**:  
- Creating empty  ```accepted_records``` and ```invalid_records``` lists
- Creating an empty ```accepted_ids``` set. 
- Looping through each row, starting at the second row (```row in enumerate(rows, start = 2```) and
  -  pass the current row, its row number, and ```accepted_ids```through the validate_record() function and store the returned record in ```cleaned_record``` and any rejection reasons in ```reasons```.
  - ```if``` ```cleaned_record``` is valid, append it to ```accepted_records``` 
  - otherwise, append a dictionary to the invalid_records list, containing its record_id and the reason of rejection
- Ending loop
- Returning ```accepted_records``` and ```invalid_records```
**Output**:  
Valid and invalid records lists. Format: tuple[list[dict[str, str]], list[dict[str, str]]]


### 2.4 Summarise_oaks - clean_silwood_trees.py

**Input**:  
The validated records obtained through process_records (clean_records) 
Format: (Iterable[dict[str, str]]) 
**Aims**:  
Identifying all the oak species in the accepted records, counting the frequency of each species, and putting this into a list.  
**Function**:  
- Creating an empty list ```oak_species``` (which will store the different oak species)
- Looping through each row in ```clean_records``` and
  - ```if```that row's genus, regardless of trailing white spaces and casefold (.strip.casefold()), is "quercus", 
   append that row's species (removing casefold and stripping withespaces) to the oak_species list
   - Ending loop
- Creating ```oak_counts```, a list of all the oak_species species and their respective counts (using the ```Counter``` command)
- Returning a list of dictionaries with each species (in the species dictionary) and its respective frequency (in the count dictionary) using ```.items()```

**Output**: list of dictionaries of oak species and respective counts. Format: list[dict[str, str]]  
 

### 2.5 Functions check - test_silwood_trees.py

- Importing the functions from clean_silwood_trees.py
- Testing validate_record() function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. Missing record_id | Created a record with an empty record_id, ran the validate_record on the record | (None, ['missing record_id`, `invalid record_id`]) | Output matched expectations, check successful. |
| 2. Invalid record_id | Created a record with an invalid record_id, ran the validate_record on the record | (None, ['invalid record_id`]) | Output matched expectations, check successful. |
| 3. Invalid location | Created a record with an invalid location ran the validate_record on the record | (None, ['invalid location`]) | Output matched expectations, check successful. |
| 4. Invalid genus | Created a record with an invalid genus ran the validate_record on the record | (None, ['invalid genus`]) | Output matched expectations, check successful. |
| 5. Invalid species | Created a record with an invalid species, ran the validate_record on the record | (None, ['invalid species`]) | Output matched expectations, check successful. |
| 6. Invalid genus-species combination | Created a record with an invalid genus-species combination, ran the validate_record on the record | (None, ['invalid genus/species combination`]) | Output matched expectations, check successful. |
| 7. Distance out of range | Created records with out of range distances (at the boundaries: 0, 101). Also checked some valid distances (at the boundaries:1, 100). Ran the validate_record function on the records. | (None, ['distance_m out of range`]) (for invalid distances) and the printed record (for valid distances)| Output matched expectations, check successful. |
| 8. Angle out of range | Created records with out of range angles(at the boundaries: 0, 90). Also checked some valid distances (at the boundaries:1, 89). Ran the validate_record function on the records.| (None, ['angle_degrees out of range`]) (for invalid angles) and the printed record (for valid angles)| Output matched expectations, check successful. |
| 9. Order of error messages | Created record which should generate an error for each field, ran the validate_record function on the record | (None, ['missing record_id, 'invalid record_id', 'duplicate record_id', 'invalid location', 'invalid genus', 'invalid species', 'distance_m out of range', 'angle_degrees out of range']| Output matched expectations, check successful. |
| 10. Trailing spaces and case sensitivity | Created a record with added spaces and abnormal casing in the field inputs, ran the validate_record function on the record | The printed record (valid record)| Output matched expectations, check successful. 
| 11. Valid data | Created a record with valid field inputs, ran the validate_record function on the record | The printed record (valid record)| Output matched expectations, check successful.

- Testing process_records function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. Duplicate records | Created a data set with duplicate records, ran the process_records function on the record |Printed record of the first one, followed by 'reasons':'duplicate record' (accepted first record but not the duplicate| Output matched expectations, check successful. |
| 2. Outputs | Ran process_records on records data set |Accepted records as a list of dictionaries, invalid records printed as a list of dictionaries  with the record_id and the reasons for rejection| Output matched expectations, check successful. |

- Testing summarise_oaks function

| Test | Workflow | Expected outputs | Successful output |
|---|---|---|---|
| 1. No oaks | Created a data set with no records having 'Quercus' genus, ran the summarise_oaks function on the data| [] (an empty list as there are no oaks)| Output matched expectations, check successful. |
| 2. Exact oak names | Created a data set with two  records having the exact same scientific oak names (Quercus robur). Ran process_records on the data set |[{species:'robur', count:2}] (list of dictionaries with oak species and count of the species)| Output matched expectations, check successful. |
| 3. Near match with oak names | Created a data set with a record having Quercus genus  (robur species) and another having typo in genus name (Quercuss)). Ran process_records on the data set|[{species:'robur', count:1}] (list of dictionaries with oak species and count of the species where the record with the typo is not included)| Output matched expectations, check successful. |

# 3. R 
Getting familiar with coding in R.

**Required packages**: tidyverse, reshape2
## In-class scripts

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
  Note: ran source("code/browse.R") from R console, which opened the Browser() tool. Examined the variables using n, c, Q, and ls(). ls() returned "generations", "N", "N0", "r", and "t"
>- observations_practice.R  
  Run with: ```Rscript code/observations_practice.R```
>- data_wrang.R  
  Run with: ```Rscript code/data_wrang.R```
>- data_wrang_tidy.R  
  Run with: ```Rscript code/data_wrang_tidy.R```


## Assignment 3

### 3.1 Tree height practical

**Filenames**: TreeHeight.R, get_TreeHeight.R, run_get_TreeHeight.sh
**File types**: R scripts and shell script
**How to run**: in bash terminal from project root: ```Rscript code/TreeHeight.R```, ```Rscript code/get_TreeHeight.R data/trees.csv```, ```bash code/run_get_TreeHeight.sh```

#### Aims
getting familiar with data wrangling and plotting in R. 

#### Software requirements
**Software**: VS code, or equivalent environment that can run **R**
**R Packages**: tidyverse

#### Required data and scripts
trees.csv from MQB/content/data

#### Script overview
(1) Creating an R script (TreeHeight.R) containing functions that calculate tree height based on distance and angle and validate the input data, and that runs checks on these functions
(2) Creating a generalised TreeHeight script (get_TreeHeight.R) that uses the functions from TreeHeight.R to calculate tree height, and where the input csv can be specified upon running the script from the terminal
(3) Creating a shell script that runs the generalised R script with the trees.csv data as input

#### Part 1 - TreeHeight.R

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
 Angle.degrees (angle in degrees) and Distance.m  (distance in meters))
**Aims**:  
Calculating tree height using tree distance and angle as inputs  
**Function**: 
Converting  the angle from degrees to radians (```Angle.degrees * pi / 180```), computing the height (in meters, ```Distance.m * tan(angle_radians)```), and returning the computed tree height (```height_m```).  
**Outputs**:  
height_m

**check_trees() function**
>**Inputs**:  
data frame  
**Aims**:
validates measurements from tree data and calculates tree height using and already entered distance and angle data.    
**Function**:  
create a function ```check_trees``` where {
  the ```col_order``` is ```c("Species", "Distance.m", "Angle.degrees")```
  ```if``` the column names from trees are not identical (```!identical```) to col_order {
    ```stop``` the task and state as a reason "wrong/headers/ header order"
  }

  Distance.m and Angle.degrees columns from the data frame are converted to be numeric (```as.numeric```)

  A vector ```num_col``` containing (```<-```) ```c("Distance.m", "Angle.degrees")``` is created 

   ```for``` each col ```in num_col```
    ```if``` the are any NA values (```any(is.na())```) ```{```
      ```stop``` the command and state as a reason ```"Missing or non-numeric values in", col}```
    ```if``` any col values are not finite (```!is.finite```) ```{```
    ```stop``` the command and state as a reason ```"invalid", col}```
  ```if``` any ```trees$Distance.m``` value is outside of its range ```{```
    ```stop``` the command and state as a reason ```"Distance.m out of range"}```
  repeat last statement but for Angle.degrees range
  
  set ```trees``` to be (```<-```) ```trees``` where (```%>%``)
    a new column is created (```mutate```), called ```height_m``` and is equal to ```height_m``` obtained from running the ```TreeHeight``` function on ```(Angle.degrees, Distance.m)```
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




#### Part 2 - get_TreeHeight.R
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
| 1. No argument provided | Ran the function without adding an argument with the following command: ```Rscript code/get_TreeHeight.R``` | Error: "No argument provided", termination of the task | Output matched expectations, check successful. |
| 2. Too many arguments provided | Ran the function inputting two arguments with following command: ```Rscript code/get_TreeHeight.R data/trees.csv data/trees.csv``` | Error: "too many arguments provided", termination of the task | Output matched expectations, check successful. |
| 3. Missing file | Ran the function with as argument a file that doesnt exist using the following command: ```Rscript code/get_TreeHeight.R  data/doesnotexist.csv``` | Error: "Missing file", termination of the task | Output matched expectations, check successful. |
| 4. Directory instead of file | Ran the function with as argument a directory instead of a file that doesnt exist using the following command: ```Rscript code/get_TreeHeight.R  data/``` | Error: "Missing file", termination of the task | Output matched expectations, check successful. |
| 5. Unreadable file | Created an unreadble file and ran the function with as argument the unreadable file, using the following commands: ```touch data/unreadable.csv```,  ```chmod 000 data/unreadable.csv```, ```Rscript code/get_TreeHeight.R data/unreadable.csv``` | Error: "File is not readable, termination of the task | Output matched expectations, check successful. |



**Outputs**
(1) script named get_TreeHeight.R stored in code
(2) csv file named 'basename'_treeheights.csv


##### Part 3 - run_get_TreeHeight.R
**How to run**:bash code/run_get_TreeHeight.sh

Shell script(file: run_get_TreeHeight.sh) with code to run the command in Bash, and terminate execution if the script fails. 

**Outputs**:
csv file with the checked and modified data, stored in results as <input-basename-without-.csv>_treeheights.csv

### 3.2 Pound hill practical 

**Filenames**: pound_hill_analysis.R  
**File types**: R scripts  
**How to run**: Rscript code/pound_hill_analysis.R (from project root in Bash terminal)

#### Aims
Wrangling pound hill data, calculating mean species richness at plots, blocks, and cultivation combinations, and plotting it.

#### Software requirements
VS code (or equivalent environment that can run R)

#### Required data and scripts
From MQB repository into own repository: 
from content/data to project root data folder
    - pound_hill_data.csv
    - pound_hill_meta_data.csv
 
 *Files are now in GitHub repository data folder
  
#### Workflow
(1) Loading the required libraries  
(2) Loading the data and metadata  
(3) Inspecting the data using ```head```, ```str```, and ```dim``` commands to investigate first lines of the data, its structure, and its dimensions respectively.  
(4) Wrangling the data:  
- Converting blank spaces to observed 0s (```data[data==""]=0```)
- Transposing the data (```data <- t(data)```)
- Converting data matrix to data frame (```as.data.frame```) and converting the obtained table from wide format to long format (```pivot_longer()```)
- Setting fields as class factor (```as.factor```), except for Count that was set to class integer (```as.integer```)
(5) Validating that the counts are   
- not missing and numeric (```if(any(is.na(){}```)
- non-negative  (```if(any(COUNTDATA <0) {}```)
N.B.: when count data was non-numeric, as.integer would have coerced it into NA. Thus, non-numeric counts will get flagged by ```is.na``` check.
(6) Testing the data validation checks by creating fake counts and passing them through the checks:  


| Test | Input | Workflow | Expected outputs | Successful output |
|---|---|---|---|---|
| a. Missing counts | `c("1", "2", "")` | Created vector with a missing count, converted it to class integer, ran `if (any(is.na(na_count))) {print("Error: Missing or non-numeric count detected")}` | Error: Missing or non-numeric count detected | Outputs matched expectations, check successful. |
| b. Non-numeric counts | `c("1", "2", "abc")` | Created vector with a non-numeric count, converted it to class integer, ran `if (any(is.na(non_numeric_count))) {print("Error: Missing or non-numeric count detected")}` | Error: Missing or non-numeric count detected | Outputs matched expectations, check successful. |
| c.Negative counts | `c("1", "2", "-1")` | Created vector with a negative count, converted it to class integer, ran `if (any(negative_count < 0)) {print("Error: Negative counts detected")}` | Error: Negative counts detected | Outputs matched expectations, check successful. |
| d. Valid counts | `c("1", "2", "1")` | Created vector with valid counts, converted it to class integer, ran the if statements on them | Return nothing (meaning counts passed the validation check) | Outputs matched expectations, check successful. |

(7) Reinspecting the data with the ```head```, ```str```, and ```dim``` commands  
(8) Calculating mean species richness by using ```%>%``` pipeline to modify it into a table that shows Cultivation, Plot, Quadrat, and Block
and calculate richness at each of these combinations (richness here refers to number of species detected)  
(9) Creating a figure, using ```ggplot```, showing the mean species richness at each plot, in relation to cultivation  
(10) Saving the results using as "pound_hill_plot_richness.csv" (```write.csv()```) and the figure as "pound_hill_plot_richness.pdf"  (```pdf()```)  
(11) Interpreting the plot.  

N.B. Ran the script twice to make sure it was reproducible.  

#### Outputs
(1) pound_hill_analysis.R: R script stored in project root codes folder  
(2) pound_hill_plot_richness.csv: csv with the mean richness data at each cultivation, block, and plot combination. File stored in project root results folder.  
(3) pound_hill_plot_richness.pdf: figure of the mean species richness at each plot, in relation to cultivation. File stored in the project root results folder.  


## External Sources 

### AI use
For these assignments and in-class scripts, I used ChatGPT and copilot in GitHub to understand error messages and given scripts, debug scripts, and get hints on how to go further. Additionaly, I prompted Chat with Copilot to help me create a structure for the README file.


### Websites and blogs

- https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
- https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements
- https://stackoverflow.com/questions/64644087/python-validate-if-column-entries-match-a-desired-format
- https://zetcode.com/python/regex-fullmatch-function/ 
- https://www.geeksforgeeks.org/python/python-check-for-float-string/
- https://www.geeksforgeeks.org/python/python-string-casefold-method
- https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
- https://stackoverflow.com/questions/1278749/-how-do-i-detect-missing-fields-in-a-csv-file-in-a-pythonic-way
- https://www.geeksforgeeks.org/python/return-dictionary-from-a-function-in-python/#returning-a-dictionary-using-a-dictionary-constructor
- https://realpython.com/nested-loops-python/
- https://www.statology.org/r-filter-between-two-values/
- https://dplyr.tidyverse.org/reference/filter.html
- https://www.geeksforgeeks.org/r-language/address-errors-in-if-statements-in-r/
- https://www.geeksforgeeks.org/r-language/reorder-the-column-of-dataframe-in-r-using-dplyr/
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/
-  https://www.w3schools.com/r/r_for_loop.asp
- https://introcs-python.cs.luc.edu/dict_algorithms/overview.html
- https://www.geeksforgeeks.org/python/python-counter-items-counter-keys-and-counter-values/
- https://realpython.com/python-counter/
- https://www.geeksforgeeks.org/python/counters-in-python-set-1/
- https://www.geeksforgeeks.org/r-language/how-to-read-command-line-parameters-from-an-r-script/
- https://maple60.github.io/en/posts/2026-02-06-r-extract-filename/
-  https://www.statology.org/reorder-columns-r/
- https://www.geeksforgeeks.org/r-language/pivot-longer-in-r/
- https://gist.github.com/ramhiser/93fe37be439c480dc26c4bed8aab03dd
- https://ggplot2.tidyverse.org/reference/scale_manual.html
- https://www.r-bloggers.com/2025/03/how-to-center-ggplot-title-subtitle-and-caption-in-ggplot2-with-r/
