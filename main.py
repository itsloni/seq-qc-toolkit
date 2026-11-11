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
    json_fasta_data = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        json_fasta_data[record.id] = {
            "description" : record.description,
            "sequence" : str(record.seq)
        }
        fasta_sequence = json_fasta_data[record.id]["sequence"]
        print(fasta_sequence)
    return fasta_sequence



def fastq_sequence_type(fastq_file):
    json_fastq_data = {}
    for record in SeqIO.parse(fastq_file, "fastq"):
        json_fastq_data[record.id] = {
            "description" : record.description,
            "sequence" : str(record.seq),
            "quality" : record.letter_annotations["phred_quality"]
        }
        fastq_sequence = json_fastq_data[record.id]["sequence"]
        fastq_id = record.id
        fastq_quality = json_fastq_data[record.id]["quality"]
        print(record.id)
        print(fastq_quality)
        print(fastq_sequence)
    return fastq_id, fastq_sequence, fastq_quality



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



if __name__ == "__main__":
    main()