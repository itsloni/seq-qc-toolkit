print("seq-qc-toolkit is starting...")
import os
import argparse
import json
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
    fasta_sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        fasta_dict = {
            "description" : record.description,
            "sequence" : str(record.seq),
        }
        fasta_sequences.append(fasta_dict)
        print(fasta_sequences)
    return fasta_sequences



def fastq_sequence_type(fastq_file):
    fastq_sequences = []
    for record in SeqIO.parse(fastq_file, "fastq"):
        fastq_dict = {
            "description" : record.description,
            "sequence" : str(record.seq),
            "quality" : record.letter_annotations["phred_quality"],
        }
        fastq_sequences.append(fastq_dict)
        print(json.dumps(fastq_sequences, indent=4))
    return fastq_sequences


def seq_length_checker(seq_length):
    full_seq_length = []
    for sequences in seq_length:
        sequence_length = len(sequences["sequence"])
        full_seq_length.append(sequence_length)
    return full_seq_length


def seq_length_stat(sequence_length):
    min_length = min(sequence_length)
    max_length = max(sequence_length)
    average_length = sum(sequence_length)/len(sequence_length)

    return min_length, max_length, average_length


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
        fasta_sequence = fasta_sequence_type(args.input)
        full_seq_length =  seq_length_checker(fasta_sequence)
        min_length, max_length, average_length = seq_length_stat(full_seq_length)
        print(f"Your fasta length_stats are as follows: min = {min_length}, max = {max_length}, avg = {average_length}")
        print(f"Here is your fasta length: {full_seq_length}")

        # will drop next steps later
    elif file_type == "fastq":
        fastq_sequence = fastq_sequence_type(args.input)
        full_seq_length = seq_length_checker(fastq_sequence)
        min_length, max_length, average_length = seq_length_stat(full_seq_length)
        print(f"Your fastq length_stats are as follows: min = {min_length}, max = {max_length}, avg = {average_length}")
        print(f"Here is your fastq length: {full_seq_length}")
        # seq_length_checker(fastq_sequence)

        # will drop next steps later
    elif file_type == "unknown":
        print("The file is not a FASTA or FASTQ file. Cannot continue.")


    # fasta_seq_length, fastq_seq_length = fasta_seq_length_checker(fasta_sequence, fastq_sequence)
    # print(f"The length for your fasta sequence file is {fasta_seq_length}")
    # print(f"The length for your fasta sequence file is {fastq_seq_length}")
    # fastq_seq_length = seq_length_checker(fastq_sequence)
    # print(f"The length for your fasta sequence file is {fastq_seq_length}")



if __name__ == "__main__":
    main()