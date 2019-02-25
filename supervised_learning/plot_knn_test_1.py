from sklearn.neighbors import KDTree
import numpy as np
from sklearn.neighbors import NearestNeighbors

def nn():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)
    print(distances)
    print(indices)

def kd():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    kdt = KDTree(X, leaf_size=30, metric='euclidean')
    res = kdt.query(X, k=2, return_distance=False)
    print(res)


nn()