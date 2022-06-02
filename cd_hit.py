import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="cd-hit clustering")
    parser.add_argument("-i", "--input", required=True,
                        help=f"")
    parser.add_argument("-o", "--output", required=True,
                        help=f"")
    return parser.parse_args()


def run_cd_hit(input_path, output_path):
    os.system(f"cd-hit -i {input_path} -o {output_path} -c 0.6 -aS 0.8 -n 4 -M 4000")


def main():
    args = parse_args()
    run_cd_hit(args.input, args.output)


if __name__ == '__main__':
    main()
