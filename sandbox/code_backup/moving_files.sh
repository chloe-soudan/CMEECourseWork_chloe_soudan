#!/bin/bash

# Files that should remain in code/
keep=(
    variables.sh
    MyExampleScript.sh
    boilerplate.sh
    CheckLabel.sh
    CountLines.sh
    ConcatenateTwoFiles.sh
    tiff2_png.sh
    loops.py
    cfexercises1.py
    cfexercises2.py
    MyExampleScript.py
    boilerplate.py
    using_name.py
    sysargv.py
    control_flow.py
    test_control_flow.py
    observations_practice.py
    test_observations_practice.py
    debugme.py
    basic_io.R
    boilerplate.R
    control_flow.R
    r_conditionals.R
    break.R
    next.R
    try.R
    browse.R
    observations_practice.R
    data_wrang.R
    data_wrang_tidy.R
        unixPrac1.txt
    tabtocsv.sh
    csvtospace.sh
    clean_silwood_trees.py
    test_silwood_trees.py
    TreeHeight.R
    get_TreeHeight.R
    run_get_TreeHeight.sh
    pound_hill_analysis.R

)

# Move everything else from code/ to sandbox/
for file in code/*; do

    [ -f "$file" ] || continue

    filename=$(basename "$file")

    if [[ ! " ${keep[*]} " =~ " ${filename} " ]]; then

        if [ -e "sandbox/$filename" ]; then
            echo "SKIPPING: $filename already exists in sandbox"
        else
            echo "Moving $filename to sandbox/"
            git mv "$file" sandbox/
        fi

    fi
done

echo "Finished organising code folder."
