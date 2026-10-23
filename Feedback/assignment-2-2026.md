# Assignment 2 formative feedback

This feedback is organised by the relevant computing bootcamp criteria. Use it to decide what is already working, what you need to investigate, and what to revise before the cumulative submission.

The full criteria are in the [Computing Bootcamp assessment rubric](https://github.com/MulQuaBio/MQB/blob/main/content/rubrics/Computing_Bootcamp_Rubric.md).

## 1. Repository organisation and workflow discipline

- Your root README, `.gitignore`, cleaning script, test script and supplied data files are in the expected locations. The supplied CSV and metadata are unchanged, giving you a reproducible starting point.

## 2. Code completeness and functional correctness

- **Check output generation independently of existing files.** Because `results/silwood_trees_clean.csv` is already committed, I could not verify that the script creates it when no output file already exists. Your code shows three writer calls, but does not show that the output-writing step works correctly. Make a separate copy of your repository in a new folder using `git clone` and confirm that the generated CSV files are not already present. Run the script there and inspect all three newly generated tables. Keep generated results out of commits and check that `.gitignore` covers them; adding an ignore rule alone will not untrack an existing file.
- The generated tables were not available in the saved run, so their contents still need checking—this does not mean they were missing or incorrect.

## 3. Code quality and style

- Your `main()` function gives the program a clear overall structure by connecting loading, processing, summarising and writing. Keep these stages distinct as you revise; use descriptive names and add short comments where the reason for a validation check or data-cleaning step is not obvious.

## 4. Documentation

- Your root README is in place. Make it useful to someone opening the repository for the first time: explain what the cleaner does, how to run the script and tests from the repository root, and which three files it creates. Test the instructions in a newly cloned copy of your repository (a separate folder created with `git clone`): enter that folder and run each README command exactly as written. If something fails, correct the command or add the missing step.

## 5. Version-control practice

- Since the previous formative feedback was added, the saved history contains 11 non-merge commits. There are several recent commits, but messages such as `progress assignment 2`, `changes to second function`, and `changes readme` do not say what behaviour changed or whether the repository worked at that point.
- Before each commit, run `git diff --staged` to see exactly what will be recorded. Keep one coherent, working change per commit and write a concise message that names what changed—for example, the validation rule added, the failing test fixed or the README instruction clarified.
- `results/silwood_trees_clean.csv` is currently tracked by Git. After confirming that it is a generated file, run `git rm --cached results/silwood_trees_clean.csv`; this removes it from Git without deleting your local copy. Keep the results path in `.gitignore`, commit the change, and use `git status` to confirm that generated CSVs will not be included again.

## 8. Basic error handling and input validation

- Your supplied raw CSV and metadata are unchanged, and the required script, separate test file, root README and `.gitignore` are present.
- Your test file exercises record validation, the accepted/rejected partition and the oak summary. It ran without errors, but printed output alone cannot tell you whether every result is correct.
- **Make your tests detect incorrect results.** Your test file contains no assertion-style checks, so printed results alone cannot automatically flag a regression. Add explicit checks for a valid record, an invalid record, their routing into the appropriate collections, and a small oak summary whose result you can calculate by hand.
- Add and run the small assertion-based tests above. Check that a deliberately incorrect expected result causes a test to fail, then restore the correct expectation.
- Check that your root README gives working run and test commands, explains the three outputs, and lets another person reproduce them in a newly cloned copy of the repository.

## 9. Problem-solving approach and method implementation

- Your code shows a connected workflow: `main()` calls `load_records()`, passes rows to `process_records()`, which uses `validate_record()` and returns accepted and invalid collections. The cleaned collection then feeds `summarise_oaks()`, followed by three calls to `write_csv()`. The flow from input to outputs is easy to follow.
- Before final submission, add or refine a small assertion-based test in `code/test_silwood_trees.py` using one valid and one invalid record. Check that `process_records()` places them in the cleaned and issues collections respectively, then pass the cleaned collection to `summarise_oaks()` and check that the invalid record does not contribute. Run the complete cleaner and inspect the three output files. Briefly explain this flow in your root README.
