import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

class FastNearestNeighbor:
    def __init__(self):
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y

    def get_nearest(self, x):
        # Eliminating the for loop and compute Euclidean distance
        distances_squared = np.sum((self.X - x) ** 2, axis=1)
        nearest_index = np.argmin(distances_squared)
        return nearest_index

    def predict(self, X_test):
        # return:  an array of predictions for X_test
        y_pred = [self.y[self.get_nearest(x)] for x in X_test]
        return np.array(y_pred)

X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                          n_redundant=0, n_repeated=0, n_classes=2,
                          n_clusters_per_class=1, class_sep=0.35,
                          random_state=1)

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.3, shuffle=True, random_state=1)

faster_nn = FastNearestNeighbor()
faster_nn.fit(X_train, y_train)
