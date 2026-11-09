print("fasta_to_json converter is starting...")
import argparse
import os
import json
from Bio import SeqIO

def checking_if_exist(input_filepath):
    return os.path.isfile(input_filepath)

def sequence_parser(input_filepath):

    fasta_data = {}
    for record in SeqIO.parse(input_filepath, "fasta"):
        fasta_data[record.id] = {
            "description" : record.description,
            "sequence" : str(record.seq),
        }
    return fasta_data

def json_dump_file(output_filepath, fasta_data):

    with open(output_filepath, "w") as file1:
        json.dump(fasta_data, file1, indent=4)

def main():
    parser = argparse.ArgumentParser(description="FASTA to JSON converter")

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to input FASTA file",
    )

    parser.add_argument(
        "-o", "--output",
        default="output/summary.json",
        help="Path to save output JSON file",
    )

    args = parser.parse_args()

    if not checking_if_exist(args.input):
        print("File does not Exist")
        return


    fasta_data = sequence_parser(args.input)
    json_dump_file(args.output, fasta_data)



if __name__ == "__main__":
    main()

