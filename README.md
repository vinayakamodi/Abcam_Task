# Abcam AI Engineer - Python Coding Task

## Overview

Welcome to my solution for the AI Engineer coding task at Abcam. This project involves processing a CSV file named `uniprot_sequences.csv`, which contains simulated protein sequence data.

## Task Requirements

The coding task involves extracting two key features from each protein sequence in the dataset:
1. **One Hot Encoded Letter Vector**: Each amino acid in a sequence is represented as a one-hot encoded vector. To ensure uniform vector lengths across all sequences, shorter sequences are padded with a representation of 'X', which stands for a missing or ambiguous amino acid.
2. **Letter Composition**: This feature calculates the frequency of each amino acid in a sequence, resulting in a 21-element vector that sums the occurrences of each amino acid.

## Repository Structure

- `main.py`: Contains all functions necessary for processing the sequence data.
- `test.py`: Provides a suite of tests to ensure the functionality of the main processing module.
- `README.md`: A guide to understanding and navigating this repository.

## Setup and Installation

Before you start, make sure you have Python 3.8 or higher installed. To install the necessary dependencies, run the following command:

```bash
pip install pandas numpy
```

## Usage

Run the following command to process the sequence data and see the output:

```bash
python main.py
```

This will process the data in `uniprot_sequences.csv` and display the first few rows of the output DataFrame.

## Testing

The CSV file `uniprot_sequences.csv` was randomly generated to provide a controlled set of data for testing the code. The test suite in `test.py` is designed to ensure that all parts of the code function as expected.

### What the Test Cases Cover

- **Loading Data**: Tests that the CSV data loads correctly into a pandas DataFrame.
- **Maximum Sequence Length**: Ensures the function accurately finds the longest sequence in the dataset.
- **One Hot Encoding**: Confirms that sequences are encoded correctly and that padding for shorter sequences works as expected.
- **Letter Composition**: Checks that the amino acid frequency is calculated correctly, even in edge cases like empty sequences.
- **End-to-End Processing**: An integration test that confirms the entire processing pipeline works from start to finish, producing a DataFrame with the expected features.

To run the tests, use this command:

```bash
python -m unittest test
```
## LaTeX Source and PDF Output

The files related to the LaTeX document are structured as follows:

- `report.tex`: This file contains the LaTeX source code for the comprehensive report on the Python coding task. It includes detailed descriptions of the algorithms, software design principles, testing procedures, and potential future enhancements related to the project. The `.tex` format is editable and can be compiled to generate a PDF using any LaTeX editor that supports compiling documents.

- `report.pdf`: This file is the compiled output of `report.tex`. It presents the formatted and typeset version of the report, which is ready for viewing and distribution. This document includes all sections described in the LaTeX source code, rendered into a professional-looking report format.

To compile `report.tex` to `report.pdf`:
1. Ensure you have a LaTeX editor like TeXShop (for Mac), TeXworks (cross-platform), or an online editor like Overleaf.
2. Open `report.tex` in your LaTeX editor.
3. Compile the document using the appropriate command in your editor, typically found in the build or compile menu.

The `report.pdf` is useful for reviewing the project's documentation in a format that is easy to share and present during meetings or audits.

