print("seq-qc-toolkit is starting...")
import argparse
import os

def checking_if_exist(pathfile):
    return os.path.isfile(pathfile)


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

    if not checking_if_exist(args.input):
        print("File does not Exist")
        return

