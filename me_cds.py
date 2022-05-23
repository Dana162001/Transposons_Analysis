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

    # todo
    non_overlapping_me = mobile_elements
    interesting_sequences = []

    for cds in cds_list:
        cds_location = cds["location"]
        for mobile_element in non_overlapping_me:
            if mobile_element[1] > cds_location[0] > mobile_element[0] \
                    and mobile_element[0] < cds_location[1] < mobile_element[1]:
                interesting_sequences.append(cds["sequence"])

    print(f"Saving {len(interesting_sequences)} cds sequences  from {file_path.stem}")
    out_file = output_dir / (file_path.stem + ".fasta")

    with open(out_file, "w") as f:
        i = 0
        for seq in interesting_sequences:
            f.write(f">{i}.{file_path.stem}\n{seq}\n")
            i += 1


def main():
    args = parse_args()
    input_dir = pathlib.Path(args.input)
    output_dir = pathlib.Path(args.output)
    output_dir.mkdir(exist_ok=True, parents=True)

    Parallel(n_jobs=cpu_count())(delayed(me_cds)(path, output_dir) for path in input_dir.glob('*.gbff'))
    # merge output files
    os.system(f"cat {output_dir}/* > merged_cds_prot.fasta")


if __name__ == '__main__':
    main()
