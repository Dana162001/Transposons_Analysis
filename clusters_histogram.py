import argparse

import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description="Histogram of sequences distribution in the clusters")
    parser.add_argument("-i", "--input", required=True,
                        default="/data",
                        help=f"path to .clstr file from CD-HIT output")
    return parser.parse_args()


# Counts number of hits in the cluster
def count_lines_between_clusters(file_path):
    counts = []
    with open(file_path) as f:
        # omit first line
        lines = f.readlines()[1:]
        counter = 0
        for line in lines:
            if line.startswith(">Cluster"):
                counts.append(counter)
                counter = 0
            else:
                counter += 1
    counts.append(counter)

    return counts


# Histogram of counted hits
def plot_clusters_histogram(file_path):
    hits_in_cluster = count_lines_between_clusters(file_path)

    plt.hist(hits_in_cluster, bins = 100, log = True, color='deepskyblue', edgecolor='black')

    plt.title('Distribution of hits in a clusters')
    plt.xlabel('Number of hits')
    plt.ylabel('Number of clusters')

    plt.show()


def main():
    args = parse_args()
    plot_clusters_histogram(args.input)


if __name__ == '__main__':
    main()
