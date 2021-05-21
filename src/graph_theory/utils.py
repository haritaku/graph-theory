from copy import deepcopy

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_graph(graph, seed=0):

    if type(graph) is not nx.classes.multigraph.MultiGraph:
        raise ValueError('Graph must be "MultiGraph" object.')

    fig, ax = plt.subplots(facecolor='white')
    pos = nx.spring_layout(graph, seed=seed)
    nx.draw_networkx_nodes(graph, pos, node_color='#03AF7A', ax=ax)
    nx.draw_networkx_labels(graph, pos, ax=ax)
    for i, e in enumerate(graph.edges):
        start_v, end_v, n_edge = pos[e[0]], pos[e[1]], e[2]
        arrowprops = {
            'arrowstyle': '-',
            'color': '0.5',
            'shrinkA': 8,
            'shrinkB': 8,
            'connectionstyle': f'arc3,rad={0.3 * n_edge}'
        }
        ax.annotate(
            '',
            xy=start_v,
            xytext=end_v,
            arrowprops=arrowprops)
    plt.axis('off')


def incicence2adjacency(inc_arr):

    if np.isin(inc_arr, [0, 1], invert=True).sum():
        raise ValueError('Incidence matrix has values except for 0 or 1.')

    if (inc_arr.sum(axis=0) != 2).sum():
        raise ValueError('Incidence matrix doesn\'t satisfy handshaking lemma.')

    x, y = np.where(inc_arr == 1)
    x_sort = x[y.argsort()]
    n_vertex = inc_arr.shape[0]

    adj_arr = np.zeros((n_vertex, n_vertex))
    for i in range(0, len(x_sort), 2):
        x_idx, y_idx = x_sort[i:i + 2]
        adj_arr[x_idx, y_idx] += 1
        adj_arr[y_idx, x_idx] += 1

    return adj_arr


def exists_graph(degs):
    degs = deepcopy(degs)
    degs.sort(reverse=True)

    # Handshaking Lemma.
    if sum(degs) % 2 != 0:
        return False

    for k in range(1, len(degs) + 1):
        sum_k_degs = sum(degs[:k])
        k_km1 = k * (k - 1)
        sum_min = sum([min(deg, k) for deg in degs[k:]])

        if sum_k_degs > k_km1 + sum_min:
            print(f'When k={k}, false [{sum_k_degs} > {k_km1} + {sum_min}].')
            return False

    return True
