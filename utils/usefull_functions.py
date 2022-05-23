# Function to open files (with closing)
def read_num_from_lines(filename, mode):
    with open(filename, mode) as file:
        lines = [int(line.strip('\n')) for line in file.readlines()]
    return lines
