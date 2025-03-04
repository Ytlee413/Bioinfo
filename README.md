# Protein Sequence Toolkit

## Overview

This repository contains Python and R scripts for bioinformatics analysis, primarily focused on protein sequence analysis and visualization.

## Contents

- `perfect_patchy_sequence.py`: Generates "perfect" and "patchy" versions of YF sequences.
- `seq_translation_docx.py`: Translates DNA sequences into protein sequences and saves the output as a Word (`.docx`) file.
- `generate_plot.r`: Uses R to visualize amino acid distribution in a protein sequence.
- `generate_plot_for_YF.r`: Uses R to visualize the distribution of a specific amino acid (X) in a protein sequence.

## Detailed Descriptions

### 1. `perfect_patchy_sequence.py`

**Functionality:**

- Extracts Y (tyrosine) and F (phenylalanine) residues from the input protein sequence.
- Generates a "perfect" YF sequence with evenly distributed Y and F residues.
- Generates a "patchy" YF sequence where Y and F residues appear in clusters.

**Usage:**

```python
from perfect_patchy_sequence import generate_perfect_yf, generate_patchy_yf

seq = "SLENSSNKNEKEKSAPSRTK..."  # Input protein sequence
patch = 5  # Define the number of patchy blocks

perfect_seq = generate_perfect_yf(seq)
patchy_seq = generate_patchy_yf(seq, patch)

print("Perfect YF Sequence:", perfect_seq)
print("Patchy YF Sequence:", patchy_seq)
```

### 2. `seq_translation_docx.py`

**Functionality:**

- Reads `.seq` format DNA sequence files.
- Performs frame-shifted translations (+1, +2, +3, -1, -2, -3).
- Outputs the translated sequences to a Word (`.docx`) file.

**Usage:**

```bash
python seq_translation_docx.py
```

Output: `seq_translated.docx`

**Dependencies:**

- `python-docx` (Install via `pip install python-docx`)

### 3. `generate_plot.r`

**Functionality:**

- Visualizes amino acid distribution in a protein sequence.

**Usage:**

```r
source("generate_plot.r")
```

### 4. `generate_plot_for_YF.r`

**Functionality:**

- Visualizes the distribution of a specific amino acid (X) in a protein sequence.

**Usage:**

```r
source("generate_plot_for_YF.r")
```

This script highlights the positions of X residues in the sequence and plots their distribution.

## Dependencies & Installation

This repository requires the following Python and R packages:

- Python 3.x
- `python-docx`
- R with base plotting functions

## Contribution

If you have suggestions for improvements or find any bugs, feel free to submit an issue or a pull request!

