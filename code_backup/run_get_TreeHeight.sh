# !/bin/bash 
# chloe.soudan26@imperial.ac.uk
# RUNNING THE TREE-HEIGHT SCRIPT

# code to run get_TreeHeight.R with trees.csv data from project root 

Rscript code/get_TreeHeight.R data/trees.csv

# if script fails, terminate the command
if [ $? -ne 0 ]; then
    exit 1
fi

