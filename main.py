print("seq-qc-toolkit is starting...")
import os
import argparse
from Bio import SeqIO

def checking_if_exist(filepath):
    return os.path.isfile(filepath)

def checking_sequence_type(filepath):
    with open(filepath, "r") as f:
        content_check = f.readline()

        if content_check.startswith(">"):
            file_type = "fasta"
        elif content_check.startswith("@"):
            file_type = "fastq"
        else:
            file_type = "Unknown"

        return file_type

def fasta_sequence_type(fasta_file):
    pass

def fastq_sequence_type(fastq_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="seq-qc-toolkit: Quality control for FASTA and FASTQ files")

    parser.add_argument("-i", "--input",
                        required=True,
                        help="input fasta file")

    parser.add_argument("-o",
                        "--output",
                        default="output/summary.csv",
                        help="output fasta file")

    args = parser.parse_args()

    if not checking_if_exist(args.input):
        print("Input file does not Exist")
        return

    file_type = checking_sequence_type(args.input)
    if file_type == "fasta":
        fasta_sequence_type(args.input)
        # will drop next steps later
    elif file_type == "fastq":
        fastq_sequence_type(args.input)
        # will drop next steps later
    elif file_type == "unknown":
        print("The file is not a FASTA or FASTQ file. Cannot continue.")









