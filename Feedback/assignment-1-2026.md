# Assignment 1 feedback - Chloe Soudan

**Formative feedback | Rubric 2026.2**

The Unix notes contain useful explanations of header removal and sequence joining, and the history records coursework activity. There is also a tab converter under week1/code. This is therefore partly a repository-layout problem, not a claim that you attempted no conversion work.

Begin by bringing the assessed work into the required root code/ and data/ layout. The required converters and supplied inputs are not all available there, so no student command was launched in this assessment. Complete csvtospace.sh and add the FASTA files, all four temperature CSVs and your own TSV at the specified locations. Do not treat these missing-input checks as measured failures of code that was never run.

Then finish the Unix answers. Q1 needs one command covering all three files. Q2 currently confuses head and tail: head -n +2 does not mean print everything from line 2, and the alternative tail command has no input path. Q3-Q4 have recognisable counting ideas, but Q5 is unfinished. Make each answer one self-contained line with a short explanation, and check it independently rather than relying on prior shell state.

Turn the README's general aim into a usable guide: what the files do, exact commands, required tools, a few small tests and any assistance used. Ignore generated results, and make the next commit messages name the task changed. Complete the basic layout and commands first; there is no need to add more complexity before someone else can reproduce them.

---

## Project structure

Relevant tracked layout (simplified; missing required paths are marked):

```text
README.md
.gitignore
code/  unixPrac1.txt; missing: tabtocsv.sh, csvtospace.sh
data/fasta/  missing here: 407228326.fasta, 407228412.fasta, e_coli.fasta
data/temperatures/  missing here: 1800.csv, 1801.csv, 1802.csv, 1803.csv
data/tab-example.tsv [missing]
results/  no files tracked; generated on run
sandbox/  no files tracked; optional
Also: week1/code/tabtocsv.sh
Also: week1/data/
```

The project is split between the new root and the old week1/ layout. unixPrac1.txt is under root code/, but tabtocsv.sh remains under week1/code/. The required root CSV converter and data paths are missing. FASTA files are present under week1/data/, including a numbered file with a changed filename.

Bring assessed scripts and supplied inputs into the released root code/ and data/ layout, with the required filenames and unchanged contents. Keep useful classroom scripts, but separate them from scratch files and generated material in week1/. Complete the own TSV and temperature inputs, and document one clear project root rather than two competing arrangements.

**Assessed snapshot:** `f831ecc182554b25a32764a78e5f0d45326e3430`
