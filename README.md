# seq-qc-toolkit

A lightweight command-line tool for quality control of FASTA and FASTQ sequence files.

This tool calculates essential sequence statistics and generates a clean summary report in both the terminal and a CSV file.

## Features

- Supports both **FASTA** and **FASTQ** files
- Automatic file type detection
- Calculates the following metrics:

# seq-qc-toolkit

A lightweight command-line tool for quality control of FASTA and FASTQ sequence files.

This tool calculates essential sequence statistics and generates a clean summary report in both the terminal and a CSV file.

## Features

- Supports both **FASTA** and **FASTQ** files
- Automatic file type detection
- Calculates the following metrics:

| Metric                    | FASTA | FASTQ |
|--------------------------|-------|-------|
| Number of sequences      | ✅    | ✅    |
| Total bases              | ✅    | ✅    |
| Average sequence length  | ✅    | ✅    |
| Minimum sequence length  | ✅    | ✅    |
| Maximum sequence length  | ✅    | ✅    |
| GC content (%)           | ✅    | ✅    |
| N content (%)            | ✅    | ✅    |
| Average quality score    | ❌    | ✅    |

- Clean terminal summary
- Exports results to a CSV file

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/seq-qc-toolkit.git
cd seq-qc-toolkit

- Clean terminal summary
- Exports results to a CSV file

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/seq-qc-toolkit.git
cd seq-qc-toolkit
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install biopython pandas
```

## Usage

```bash
python main.py -i <input_file> [-o <output_file>]
```

### Arguments

| Flag | Description | Required | Default |
| --- | --- | --- | --- |
| -i, --input | Path to input FASTA or FASTQ file | Yes | — |
| -o, --output | Path to save the summary CSV | No | output/summary.csv |

### Examples

```bash
# Analyze a FASTA file
python main.py -i data/sample.fasta

# Analyze a FASTQ file and specify output
python main.py -i data/sample.fastq -o results/qc_report.csv
```

## Example Output

```text
seq-qc-toolkit is starting...
===== Sequence Quality Control Summary =====
File Type             : FASTQ
Number of Sequences   : 3
Total Bases           : 72
Average Length        : 24.00
Min Length            : 18
Max Length            : 30
GC Content (%)        : 48.61
N Content (%)         : 5.56
Average Quality Score : 36.42
Summary saved to      : output/summary.csv
```

## Project Structure

```text
seq-qc-toolkit/
├── main.py
├── data/
├── output/
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+
- biopython
- pandas

## Author

Built as a bioinformatics portfolio project focused on sequence data quality control and clean command-line tool design.
