# Protein Sequence Toolkit 🧬

A bioinformatics toolkit designed to simplify plasmid sequencing analysis for researchers.

## Main Tool: `seq_translation_docx.py`

Converts `.seq` files from plasmid sequencing into organized DNA and protein sequences, outputting results as a Word (`.docx`) file.

### Features

- Reads `.seq` files and performs frame-shifted translations (+1, +2, +3, -1, -2, -3).
- Saves translated sequences to `seq_translated.docx`.

### Usage

```bash
python seq_translation_docx.py
```
### Dependency
- python-docx (Install via pip install python-docx)

## Other Tools (For Publication Figures)
- perfect_patchy_sequence.py: Generates "perfect" and "patchy" YF sequences.
- generate_plot.r & generate_plot_for_YF.r: Visualize amino acid distributions using R.

### Installation
Requirements
- Python 3.x
- python-docx
- R (for visualization scripts)

### Install the Python Dependency

```bash
pip install python-docx
```

### Contribution
Found a bug or have a suggestion? Submit an issue or pull request!
