import matplotlib.pyplot as plt
import numpy as np


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


# def plot_clusters_histogram(file_path):
#     hits_in_cluster = count_lines_between_clusters(file_path)
#
#     plt.hist(hits_in_cluster, bins=100)
#
#     plt.title('Distribution of hits in a cluster (all)')
#     plt.xlabel('Number of hits')
#     plt.ylabel('Number of clusters')
#
#     # plt.show()
#
#
# file_path = "/home/dana/Desktop/p_sa/results/ISEscan/cd_hit.clstr"
# plot_clusters_histogram("/home/dana/Desktop/p_sa/results/ISEscan/cd_hit.clstr")
#
#
# x, y = np.unique(hits_in_cluster, return_counts=True)
#
# fig = px.bar(
#     x=x,
#     y=y,
#     labels={"x": "Number of hits", "y": "Number of clusters"},
#     log_y=True,
# )
# fig.update_xaxes(type="category")
# fig.update_layout(
#     showlegend=False,
#     width=800,
#     height=500,
#     title={
#         "text": "Distribution of the hits in clusters",
#         "y": 0.95,
#         "x": 0.5,
#         "xanchor": "center",
#         "yanchor": "top",
#     },
# )
# fig.write_html('first_figure.html', auto_open=True)
#
#
# def save_and_show_fig(fig, filename, scale=1):
#     fig.write_image(filename, scale=scale)
#     display(Image(filename=filename))


import plotly.express as px

file_path = '/home/dana/Desktop/p_sa/results/ISEscan/cd_hit.clstr'
hits_in_cluster = count_lines_between_clusters(file_path)

df = px.hits_in_cluster()
fig2 = px.histogram(df, x="total_bill")
fig2.show()
fig2.write_html('second_figure.html', auto_open=True)




#Works in Jupyter notebook
import matplotlib.pyplot as plt

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

file_path = '/home/dana/Desktop/p_sa/results/ISEscan/cd_hit.clstr'
hits_in_cluster = count_lines_between_clusters(file_path)

plt.hist(hits_in_cluster, bins = 100)

plt.title('Distribution of hits in a cluster')
plt.xlabel('Number of hits')
plt.ylabel('Number of clusters')

plt.show()