import argparse
import pathlib

from utils.parse_gbff_files import parse_gbff_file


def parse_args():
    parser = argparse.ArgumentParser(description="WRITE SCRIPT DESCRIPTION HERE")
    parser.add_argument("-i", "--input", nargs='+', required=True,
                        default='C:/Users/daryn/Desktop/p_SA/results/modified_all/',
                        help=f"")
    parser.add_argument("-o", "--output", nargs='+', required=True,
                        default='C:/Users/daryn/Desktop/p_SA/results/cds_sequences/',
                        help=f"")
    return parser.parse_args()


def main():
    # args = parse_args()
    # input_dir = pathlib.Path(args.input)
    # output_dir = pathlib.Path(args.output)
    input_dir = pathlib.Path('C:/Users/daryn/Desktop/p_SA/results/modified_all/')
    output_dir = pathlib.Path('C:/Users/daryn/Desktop/p_SA/results/cds_sequences/')
    output_dir.mkdir(exist_ok=True, parents=True)

    for file_path in input_dir.glob('*'):
        sequence, mobile_elements, cds = parse_gbff_file(file_path)

        # todo
        non_overlapping_me = mobile_elements
        # non_overlapping_me = []
        # for i in range(len(mobile_elements)):
        # for j in range(len())

        interesting_sequences = []

        for cds_location in cds:
            for mobile_element in non_overlapping_me:
                if mobile_element[1] > cds_location[0] > mobile_element[0] \
                        and mobile_element[0] < cds_location[1] < mobile_element[1]:
                    interesting_sequences.append(sequence[cds_location[0]:cds_location[1]])

        print(f"Saving {len(interesting_sequences)} cds sequences  from {file_path.stem}")

        out_file = output_dir / (file_path.stem + ".fasta")

        with open(out_file, "w") as f:
            i = 0
            for seq in interesting_sequences:
                f.write(f">{i}\n{seq}\n")
                i += 1


if __name__ == '__main__':
    main()
