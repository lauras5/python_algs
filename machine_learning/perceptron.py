import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


class Perceptron:
    """An implementation of the perceptron algorithm.
    Note that this implementation does not include a bias term"""

    def __init__(self, iterations=100, learning_rate=0.2,
                 plot_data=False, random_w=False, seed=42):
        self.converged = None
        self.wold = None
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.plot_data = plot_data
        self.random_w = random_w
        self.seed = seed

    def fit(self, X, y):
        """
        Train a classifier using the perceptron training algorithm.
        After training the attribute 'w' will contain the perceptron weight vector.

        Parameters
        ----------
        X : ndarray, shape (num_examples, n_features)
        Training data.
        y : ndarray, shape (n_examples,)
        Array of labels.
        """

        if self.random_w:
            rng = np.random.default_rng(self.seed)
            self.w = rng.uniform(-1, 1, len(X[0]))
            print("initialized with random weight vector")
        else:
            self.w = np.zeros(len(X[0]))
            print("initialized with a zeros weight vector")
        self.wold = self.w
        converged = False
        iteration = 0
        while not converged and iteration <= self.iterations:
            converged = True
            for i in range(len(X)):
                if y[i] * self.decision_function(X[i]) <= 0:
                    self.wold = self.w
                    self.w = self.w + y[i] * self.learning_rate * X[i]
                    converged = False
                    if self.plot_data:
                        self.plot_update(X, y, i)
            iteration += 1
        self.converged = converged
        if converged:
            print('converged in %d iterations ' % iteration)

    def decision_function(self, x):
        return np.dot(x, self.w)

    def predict(self, X):
        """
        make predictions using a trained linear classifier

        Parameters
        ----------
        X : ndarray, shape (num_examples, n_features)
        Training data.
        """

        scores = np.dot(X, self.w)
        return np.sign(scores)

    def plot_update(self, X, y, ipt):
        fig = plt.figure(figsize=(4, 4))
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.arrow(0, 0, self.w[0], self.w[1],
                  width=0.001, head_width=0.05,
                  length_includes_head=True, alpha=1,
                  linestyle='-', color='darkred')
        plt.arrow(0, 0, self.wold[0], self.wold[1],
                  width=0.001, head_width=0.05,
                  length_includes_head=True, alpha=1,
                  linestyle='-', color='orange')
        anew = -self.w[0] / self.w[1]
        aold = -self.wold[0] / self.wold[1]
        pts = np.linspace(-1, 1)
        plt.plot(pts, anew * pts, color='darkred')
        plt.plot(pts, aold * pts, color='orange')
        plt.title("in orange:  old w; in red:  new w")
        cols = {1: 'g', -1: 'b'}
        for i in range(len(X)):
            plt.plot(X[i][0], X[i][1], cols[y[i]] + 'o', alpha=0.6, markersize=5)
        plt.plot(X[ipt][0], X[ipt][1], 'ro', alpha=0.2, markersize=20)


# load data
data = load_breast_cancer()

X = data.data
y = data.target

# transform from (0, 1) -> (-1, 1)
y = y * 2 - 1

# add column of ones to feature matrix for bias term
X = np.hstack([X, np.ones((len(X), 1))])

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=5)

train_accuracy_list = []
test_accuracy_list = []

# number of epochs to explore
num_epochs = [2, 5, 10, 20, 40, 100, 200, 500, 1000, 2000, 4000]

for epochs in num_epochs:
    # train and evaluate perceptron
    p = Perceptron(iterations=epochs, learning_rate=0.1)
    p.fit(X_train, y_train)

    # train accuracy
    y_pred_train = p.predict(X_train)
    train_acc = np.mean(y_train == y_pred_train)
    train_accuracy_list.append(train_acc)

    # test accuracy
    y_pred_test = p.predict(X_test)
    test_acc = np.mean(y_test == y_pred_test)
    test_accuracy_list.append(test_acc)

# plot the results
plt.figure(figsize=(10, 6))
plt.semilogx(num_epochs, train_accuracy_list, label='Training Accuracy')
plt.semilogx(num_epochs, test_accuracy_list, label='Test Accuracy')
plt.title('Perceptron Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend()
plt.show()
