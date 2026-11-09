print("seq-qc-toolkit is starting...")
import argparse


def main():
    parser = argparse.ArgumentParser(description="seq-qc-toolkit: Quality control for FASTA and FASTQ files")

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to input FASTQ file",
    )

    parser.add_argument(
        "-o", "--output",
        default="output/summary.csv",
        help="Path to save output file",
    )

    args = parser.parse_args()
