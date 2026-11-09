print("seq-qc-toolkit is starting...")
import argparse
import os
import json
from Bio import SeqIO

def checking_if_exist(input_filepath):
    return os.path.isfile(input_filepath)

def read_sequence_file(input_filepath):
    with open(input_filepath, "r") as f:
        content = f.read()
        return content

    # with open()

def sequence_parser(input_filepath):

    fasta_data = {}
    for records in SeqIO.parse(input_filepath, "fasta"):
        fasta_data[records.id] = {
            "description" : records.description,
            "sequence" : str(records.seq),
        }
    print(fasta_data)
    return fasta_data

def json_dump_file(output_filepath, fasta_data):

    with open(output_filepath, "w") as file1:
        json.dump(fasta_data, file1, indent=4)
        return file1


def main():
    parser = argparse.ArgumentParser(description="seq-qc-toolkit: Quality control for FASTA and FASTQ files")

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to input FASTQ file",
    )

    parser.add_argument(
        "-o", "--output",
        default="output/summary.json",
        help="Path to save output file",
    )

    args = parser.parse_args()

    if not checking_if_exist(args.input):
        print("File does not Exist")
        return

    content = read_sequence_file(args.input)
    fasta_data = sequence_parser(args.input)
    file1 = json_dump_file(args.output, fasta_data)
    return content, fasta_data, file1

    # output_filepath = json_dump_file(args.output)
    # return output_filepath


if __name__ == "__main__":
    main()

