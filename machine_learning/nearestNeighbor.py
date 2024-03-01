import numpy as np
from matplotlib import pylab as plt

def distance(x1, x2):
    return np.linalg.norm(x1-x2)

class NearestNeighbor:
    def __init__(self):
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y

    def get_nearest(self, x):
        distances = [distance(x, self.X[i]) for i in range(len(self.X))]
        return np.argmin(distances)

    def predict(self, x):
        return self.y[self.get_nearest(x)]