import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="run blastp")
    parser.add_argument("-query", "--input", required=True,
                        help=f"Path to the merged query sequences in protein fasta format")
    parser.add_argument("-db", "--data_base", required=True,
                        help=f"Path to the database (CARD)")
    parser.add_argument("-o", "--output", required=True,
                        help=f"Path to the output file")
    parser.add_argument("-outfmt", "--outfmt", required=False,
                        help=f"Outfmt parameters of the table file that contains: qseqid qstart qend sseqid sstart send evalue ppos ")
    return parser.parse_args()


def run_blastp(input_path, output_path, db_path, out_fmt_parameters='qseqid qstart qend sseqid sstart send evalue ppos'):
    os.system(f"blastp -query {input_path} -db {db_path} -o {output_path} -outfmt {out_fmt_parameters}")


def main():
    args = parse_args()
    run_blastp(args.input, args.db, args.output, args.outfmt)


if __name__ == '__main__':
    main()
