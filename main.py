print("seq-qc-toolkit is starting...")
import os
import argparse
import json
import pandas
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
        #print(json.dumps(fastq_sequences, indent=4))
    return fastq_sequences


def seq_length_checker(full_sequence_data):
    full_seq_length = []
    for sequences in full_sequence_data:
        sequence_length = len(sequences["sequence"])
        full_seq_length.append(sequence_length)
    num_of_seq = len(full_seq_length)
    return full_seq_length, num_of_seq


def seq_length_stat(sequence_length):
    min_length = min(sequence_length)
    max_length = max(sequence_length)
    average_length = sum(sequence_length)/len(sequence_length)
    average_length = round(average_length, 2)
    return min_length, max_length, average_length

def seq_gc_content(full_sequence_data, sequence_length):
    num_of_gc_content = []
    individual_gc_content = []

    for sequences in full_sequence_data:
        sequence = sequences["sequence"]
        seq_length = len(sequence)
        num_of_g_content = 0
        num_of_c_content = 0
        for bases in sequence:
            if bases == "G" or bases == "C":
                if bases == "G":
                    num_of_g_content += 1
                else:
                    num_of_c_content += 1

        total_gc = num_of_g_content + num_of_c_content
        individual_gc_content.append(round(total_gc / seq_length) * 100)
        num_of_gc_content.append(total_gc)
    percent_gc_content = sum(num_of_gc_content)/sum(sequence_length) * 100
    percent_gc_content = round(percent_gc_content, 2)
    return percent_gc_content, individual_gc_content

def calc_n_content(full_sequence_data, sequence_length):
    n_content = []
    individual_seq_n_content = []
    for sequences in full_sequence_data:
        bases_n_content = 0
        sequence = sequences["sequence"]
        seq_length = len(sequence)
        for bases in sequence:
            if bases == "N":
                bases_n_content += 1
        individual_seq_n_content.append((bases_n_content/seq_length) * 100)
        n_content.append(bases_n_content)
    full_n_content = sum(n_content)
    percent_n_content = full_n_content/sum(sequence_length) * 100
    percent_n_content = round(percent_n_content, 2)
    return percent_n_content, individual_seq_n_content

def average_quality_score(full_sequence_data, full_seq_length):
    individual_quality_scores = []
    avg_qual_list_score = []
    for quality_scores in full_sequence_data:
        quality_score = quality_scores["quality"]
        avg_qual_list_score.append(sum(quality_score))
        individual_qual = sum(quality_score) / len(quality_scores["quality"])
        individual_quality_scores.append(individual_qual)
    total_avg_quality_score = sum(avg_qual_list_score)/sum(full_seq_length)
    total_avg_quality_score = round(total_avg_quality_score, 2)
    return total_avg_quality_score, individual_quality_scores

def save_summary(output_file, summary_data):
    df = pandas.DataFrame(summary_data)
    df.to_csv(output_file, index=False)
    return output_file



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
        full_seq_length, num_of_seq =  seq_length_checker(fasta_sequence)
        min_length, max_length, average_length = seq_length_stat(full_seq_length)
        percent_gc_content, individual_gc_content = seq_gc_content(fasta_sequence, full_seq_length)
        percent_n_content, individual_seq_n_content = calc_n_content(fasta_sequence, full_seq_length)
        summary_data = {
            "Metric": [
                "File Type",
                "Number of Sequence",
                "Total Bases",
                "Average Length",
                "Min Length",
                "Max Length",
                "GC Content (%)",
                "N Content (%)"
            ],
            "Value": [
                "FASTA",
                f"{num_of_seq}",
                f"{sum(full_seq_length)}",
                f"{average_length}",
                f"{min_length}",
                f"{max_length}",
                f"{percent_gc_content}",
                f"{percent_n_content}"
            ],
        }
        save_summary(args.output, summary_data)
        print(f"Your total N content percentage is: {percent_n_content} percent and the individual N percent is : {individual_seq_n_content}")
        print(f"Your total GC_content is: {percent_gc_content} percent and your Individual GC_content is: {individual_gc_content}")
        print(f"Your fasta length_stats are as follows: min = {min_length}, max = {max_length}, avg = {average_length}")
        print(f"Here is your fasta length: {full_seq_length}, number of sequences is : {num_of_seq}, and the Total sum of fasta length is {sum(full_seq_length)}")


    elif file_type == "fastq":
        fastq_sequence = fastq_sequence_type(args.input)
        full_seq_length, num_of_seq = seq_length_checker(fastq_sequence)
        min_length, max_length, average_length = seq_length_stat(full_seq_length)
        percent_gc_content, individual_gc_content = seq_gc_content(fastq_sequence, full_seq_length)
        percent_n_content, individual_seq_n_content = calc_n_content(fastq_sequence, full_seq_length)
        total_avg_quality_score, individual_quality_scores = average_quality_score(fastq_sequence, full_seq_length)
        summary_data = {
            "Metric": [
                "File Type",
                "Number of Sequence",
                "Total Bases",
                "Average Length",
                "Min Length",
                "Max Length",
                "GC Content (%)",
                "N Content (%)",
                "Average Quality Score"
            ],
            "Value": [
                "FASTQ",
                num_of_seq,
                sum(full_seq_length),
                average_length,
                min_length,
                max_length,
                percent_gc_content,
                percent_n_content,
                total_avg_quality_score
            ],
        }
        save_summary(args.output, summary_data)
        print(f"Your total Average quality score is : {total_avg_quality_score} and the individual Average quality score is: {individual_quality_scores}")
        print(f"Your total N content percentage is: {percent_n_content} percent and the individual N percent is : {individual_seq_n_content}")
        print(f"Your total GC_content is: {percent_gc_content} percent and your Individual GC_content is: {individual_gc_content}")
        print(f"Your fastq length_stats are as follows: min = {min_length}, max = {max_length}, avg = {average_length}")
        print(f"Here is your fastq length list: {full_seq_length}, number of sequences is : {num_of_seq}, and the Total sum of fastq length is {sum(full_seq_length)}")


    elif file_type == "unknown":
        print("The file is not a FASTA or FASTQ file. Cannot continue.")




if __name__ == "__main__":
    main()