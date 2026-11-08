print("seq-qc-toolkit is starting...")
import argparse
def main():
    parser = argparse.ArgumentParser(description="seq-qc-toolkit: Quality control for FASTA and FASTQ files")

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input FASTQ file",
    )

    parser.add_argument()