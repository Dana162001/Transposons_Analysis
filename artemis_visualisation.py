import argparse
import multiprocessing
import pathlib


import pandas as pd
from Bio import SeqIO

from Bio.SeqFeature import FeatureLocation
from Bio.SeqFeature import SeqFeature

from utils.parse_gbff_files import load_gb_file


def parse_args():
    parser = argparse.ArgumentParser(description="directory containing ISEscan results in .csv files")
    parser.add_argument("-i", "--input", required=True,
                        help=f"directory containing modified .csv files")
    parser.add_argument("-u", "--unmodified", required=True,
                        help=f"Unmodified .gb files")
    parser.add_argument("-m", "--modified", required=True,
                        help=f"Modified .gb files")
    return parser.parse_args()


def new_features_list(starts, ends, mge_type, qualifiers):
    new_features = []
    for start, end in zip(starts, ends):
        feature = SeqFeature(FeatureLocation(start, end), type=mge_type, qualifiers=qualifiers)
        new_features.append(feature)
    return new_features


# add ISEscan results to gbk file
def add_data_to_gbk(csv_path, unmodified_gb, modified_gb):
    df = pd.read_csv(csv_path)

    mge_type = 'mobile element'
    qualifiers = {'color': '0 0 255', "notes": "ISEscan"}

    record = load_gb_file(unmodified_gb)
    new_features = new_features_list(df["isBegin"], df["isEnd"], mge_type, qualifiers)
    record.features = record.features + new_features
    SeqIO.write(record, modified_gb, 'genbank')


def main():
    args = parse_args()
    csv_input_dir = pathlib.Path(args.input)
    unmodified_gb_dir = pathlib.Path(args.unmodified)
    modified_gb_output_path = pathlib.Path(args.modified)

    modified_gb_output_path.mkdir(exist_ok=True, parents=True)

    args_list = []

    for csv_file_path in csv_input_dir.glob("*.csv"):
        gb_file_name = ".".join(csv_file_path.name.split(".")[:-2])
        unmodified_gb_file = unmodified_gb_dir / gb_file_name
        modified_gb_file = modified_gb_output_path / gb_file_name
        args_list.append([csv_file_path, unmodified_gb_file, modified_gb_file])

    with multiprocessing.Pool() as p:
        p.starmap(add_data_to_gbk, args_list)


if __name__ == '__main__':
    main()
