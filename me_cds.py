import argparse
import os
import pathlib

from joblib import Parallel, delayed, cpu_count

from utils.parse_gbff_files import parse_gbff_file


def parse_args():
    parser = argparse.ArgumentParser(description="CDS extraxtion")
    parser.add_argument("-i", "--input", required=True,
                        help=f"directory containing modified .gbff files")
    parser.add_argument("-o", "--output", required=True,
                        help=f"")
    return parser.parse_args()


def me_cds(file_path, output_dir):
    _, mobile_elements, cds_list = parse_gbff_file(file_path)

    num_transposons = [0]*len(mobile_elements)
    interesting_sequences = []

    for cds in cds_list:
        cds_location = cds["location"]
        for i, mobile_element in enumerate(mobile_elements):
            if mobile_element[1] > cds_location[0] > mobile_element[0] \
                    and mobile_element[0] < cds_location[1] < mobile_element[1]:
                interesting_sequences.append(cds["sequence"])
                num_transposons[i] += 1

    print(f"Saving {len(interesting_sequences)} cds sequences  from {file_path.stem}")
    out_file = output_dir / (file_path.stem + ".fasta")
    with open(out_file, "w") as f:
        i = 0
        for seq in interesting_sequences:
            f.write(f">{i}.{file_path.stem}\n{seq}\n")
            i += 1

    num_transposons_output_file = output_dir / (file_path.stem + ".count")
    with open(num_transposons_output_file, "w") as f:
        for num in num_transposons:
            f.write(f"{num}\n")


def main():
    args = parse_args()
    input_dir = pathlib.Path(args.input)
    output_dir = pathlib.Path(args.output)
    output_dir.mkdir(exist_ok=True, parents=True)

    Parallel(n_jobs=cpu_count())(delayed(me_cds)(path, output_dir) for path in input_dir.glob('*.gbff'))
    # merge output files
    os.system(f"cat {output_dir}/*.fasta > merged_cds_prot.fasta")
    os.system(f"cat {output_dir}/*count > merged_num_transposons.count")


if __name__ == '__main__':
    main()
