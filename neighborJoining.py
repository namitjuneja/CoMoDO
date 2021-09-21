from matplotlib import pyplot as plt
import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import linkage, average, dendrogram, fcluster

def plot_fancy_dendogram(distance_matrix):
    condensed_distance_matrix = get_condensed_array(distance_matrix)
    clusters = get_clusters(condensed_distance_matrix)
    dendrogram = fancy_dendrogram(clusters)


def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    plt.savefig("./clustering.jpg")
    return ddata

def get_condensed_array(redundant_array):
    # convert the redundant n*n square matrix form into a condensed nC2 array
    condensed_distances = ssd.squareform(redundant_array) 
    # distArray[{n choose 2}-{n-i choose 2} + (j-i-1)] is the distance between points i and j
    return condensed_distances

def get_clusters(condensed_distances):
    clusters = linkage(condensed_distances, method='average', metric='euclidean')
    return clusters