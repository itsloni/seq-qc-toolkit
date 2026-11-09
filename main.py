print("seq-qc-toolkit is starting...")
import argparse
import os

def checking_if_exist(filepath):
    return os.path.isfile(filepath)

def read_sequence_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        return content


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

    content = read_sequence_file(args.input)
    return content


if __name__ == "__main__":
    main()

