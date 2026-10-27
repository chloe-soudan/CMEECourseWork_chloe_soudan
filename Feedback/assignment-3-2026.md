# Assignment 3 formative feedback

This feedback is organised using the [Computing Bootcamp rubric](https://mulquabio.github.io/MQB/rubrics/Computing_Bootcamp_Rubric.html). It does not award a mark; use it to decide what to revise and check before final submission.

## Criterion 1: Repository organisation & workflow discipline

- Before final submission, **Align reproducibility, filenames and Git tracking.** The PDF command creates `results/pound_hill_richness.pdf`, whereas the required path is `results/pound_hill_plot_richness.pdf`. Compare the script and README with that exact path and the required table path, `results/pound_hill_plot_richness.csv`; a spelling difference can make a required output appear missing. Generated files are tracked under `results/`, while `.gitignore` covers only temporary files. Stop tracking generated results without deleting your local copies, add an appropriate ignore rule, and ensure scripts create the output directory when needed. Document R/package requirements and install packages separately from analysis execution. Add exact generalised and Pound Hill commands, correct filename inconsistencies, and make future commit messages more specific than “small tweaks”.

## Criterion 2: Code completeness & functional correctness

Before final submission, run the fixed tree-height route, the generalised route and the Pound Hill analysis separately; check the exact files each one creates.

## Criterion 3: Code quality & style

As you revise, keep names descriptive, use comments to explain decisions rather than restating code, and avoid repeating the same calculation in several places.

## Criterion 4: Documentation

- Your root README explains the tasks and includes pseudocode and a fixed-route command. Your tree-height source includes the degrees-to-radians conversion and a toy measurement check; comments also describe a manual comparison and debugger use. These document your checking approach, rather than independently verifying the reported comparisons.

## Criterion 5: Version-control practice

Commit each functional revision with a short message that says what changed; this makes your development easier to follow than one large final commit.

## Criterion 8: Basic error-handling & input validation

- Both the fixed and generalised tree-height programs completed their normal runs and created CSV files. The invalid-input runs stopped with relevant angle/distance errors. These are useful execution results, although the CSV structure still needs correction.
- Before final submission, **Make validation stop processing, not merely assign text.** Your code shows that excess arguments and missing-file branches in the generalised script assign to `message`; they neither display that text nor stop execution. The Pound Hill negative/non-numeric checks use the same pattern. This can allow processing to continue or produce a less useful downstream error. Use informative stopping behaviour and test it. For counts, check whether conversion introduced missing values: testing the column's numeric type after conversion cannot show that every original value was valid. These source concerns are separate from the angle and distance tests that did stop correctly.

## Criterion 9: Problem-solving approach & method implementation

- The Pound Hill source explains why blank counts represent observed zeros and builds a quadrat-level richness table: useful foundations for connecting the measurements to a biological summary.
- Before final submission, **Restore the required tree-height interface and check both exports.** The interface run stopped with `object 'TreeHeight' not found`; the table-checking functions do not provide that required function. Its first input should be the angle in degrees and its second the horizontal distance. Try the taught example call and compare it with a direct calculation. Separately, comparison with the expected output found invalid headers in both `results/TreeHts.csv` and `results/trees_treeheights.csv`, despite successful execution. Inspect each exported first line for an extra row-name column from `write.csv`, and compare the names and order with the required four-column layout. Test both routes after the fix.
- Before final submission, **Complete and verify the Pound Hill route.** Both `data/pound_hill_data.csv` and `data/pound_hill_meta_data.csv` are confirmed missing from your latest commit, so the analysis was not executed; its outputs have not been validated. Restore the supplied inputs. In the code, the plot summary counts distinct species across a whole plot and then takes the mean of that single count—not the mean of quadrat richness. Use your quadrat-level table to trace one plot by hand, retaining zero-richness quadrats where appropriate. Compare the result with the summary and revise the caption to describe the calculation actually used.

## Criterion 10: Learning progression demonstration

Use this feedback as a revision checklist. Make the changes in small, descriptive commits, then add a short README note explaining what you changed and how you checked it. This will make your development from this formative checkpoint visible in the final portfolio.

## Priorities before final submission

- Run from the directory containing `code/`, `data/` and the root `README.md`. Rerun one ordinary and one invalid case for each tree-height route, checking errors and whether fresh outputs were written. Inspect the CSV headers and independently compare one calculated height. Then rerun Pound Hill, check one plot's summary against its quadrats, and open the PDF to review labels, values and biological meaning.
