import argparse
import pathlib

from utils.fasta_file_io import load_fasta_file, write_fasta_file


def parse_args():
    parser = argparse.ArgumentParser(description="cluster filter and representative seq extraction")
    parser.add_argument("-i", "--input", required=True,
                        help=f".clstr file")
    parser.add_argument("-n", "--number_of_hits", required=True, default=20,
                        help=f"number of hist in cluster threshold")
    parser.add_argument("-o", "--output", required=True,
                        help=f".fasta file with rep seq")
    return parser.parse_args()


def cluster_id(path_to_file, num_of_hits):
    counts = []
    rep_seq = []
    with open(path_to_file) as f:
        # omit first line
        lines = f.readlines()[1:]
        counter = 0
        for line in lines:
            if line.endswith("*\n"):
                rep_seq.append(line)
            if line.startswith(">Cluster"):
                counts.append(counter)
                counter = 0
            else:
                counter += 1
    counts.append(counter)

    output_ids = []
    output_counts = []
    for i in range(len(counts)):
        if counts[i] > num_of_hits:
            output_ids.append(rep_seq[i].split(" ")[1].replace("...", "")[1:])
            output_counts.append(counts[i])
    return output_ids, output_counts


def main():
    args = parse_args()
    input_file = args.input
    threshold = int(args.number_of_hits)

    if not args.output.endswith(".fasta"):
        raise ValueError("Output should end with .fasta")

    output_file = pathlib.Path(args.output)

    output_file.parent.mkdir(exist_ok=True, parents=True)

    extracted_rep_seqs_ids, _ = cluster_id(input_file, threshold)
    representative_sequences = load_fasta_file(input_file.replace(".clstr", ""))

    representative_sequences_output = []
    for rep_seq in representative_sequences:
        for extracted_rep_seqs_id in extracted_rep_seqs_ids:
            if rep_seq.id.startswith(extracted_rep_seqs_id):
                representative_sequences_output.append(rep_seq)
                continue

    write_fasta_file(representative_sequences_output, output_file)


if __name__ == '__main__':
    main()
