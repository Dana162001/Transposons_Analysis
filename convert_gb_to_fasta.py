import argparse
import os

from Bio import SeqIO


def parse_args():
    parser = argparse.ArgumentParser(description="Iteration over files in directory and convert from genbank to fasta")
    parser.add_argument("-i", "--input", required=True,
                        help=f"directory containing .gbff files")
    parser.add_argument("-o", "--output", required=True,
                        help=f"")
    return parser.parse_args()


# Iteration over files in directory and convert from genbank to fasta
def convert_gb_to_fasta(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith(".gbff"):
            SeqIO.convert(f"{input_path}/{filename}", "genbank", f"{output_path}/{filename}.fasta", "fasta")
            continue
        else:
            continue


if __name__ == '__main__':
    args = parse_args()
    input_dir = args.input
    output_dir = args.output
    convert_gb_to_fasta(args.input, args.output)
