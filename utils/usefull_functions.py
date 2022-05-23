# Function to open files (with closing)
import pathlib
import shutil


def read_num_from_lines(filename, mode):
    with open(filename, mode) as file:
        lines = [int(line.strip('\n')) for line in file.readlines()]
    return lines


def merge_files_binary(file_paths: list, output_path: pathlib.Path):
    with open(output_path, 'wb') as writer:
        for input_file in file_paths:
            with open(input_file, 'rb') as reader:
                shutil.copyfileobj(reader, writer)
