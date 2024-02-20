import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm

plt.rcParams['contour.negative_linestyle'] = 'solid'

X = np.array([[-0.68, -0.18],
 [-0.68, -0.48],
 [-1.54, -1.65],
 [-0.32, -0.25],
 [-0.13, -0.54],
 [-0.33, -0.50],
 [-0.76, -0.71],
 [0.63, 0.74],
 [2.58, 2.77],
 [0.26, 2.73],
 [0.29, 1.39],
 [2.43, 3.31],
 [1.58, 0.11],
 [2.68, -0.20],
 [0.50, -0.33],
 [0.22, -0.04],
 [0.02, 0.45],
 [-0.08, 0.68],
 [-0.17, 0.86],
 [0.77, 0.60],
 [0.81, 0.44]])
y = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# create a new figure, figsize: floats, w x h in inches
fig = plt.figure(figsize=(6, 6))
# specify that the subplot grid has 1 row, 1 column, and this subplot is the first (and only) subplot in the grid
ax = fig.add_subplot(111)
# setting colors for markers on plt
colors = ['b' if y[i] == 0 else 'r' for i in range(len(y))]
# X[:, 0] selects all rows from the first column of X
# X[:, 1] selects all rows from the second column of X
ax.scatter(X[:, 0], X[:, 1], c=colors, s=50, alpha=0.8)
# set labels
ax.set_xlabel('Feature 1', fontsize=12)
ax.set_ylabel('Feature 2', fontsize=12)

plot_str = ['or', '+b']  # red circles, blue crosses
# define min and max for plot
xmin = -5
xmax = 5
ymin = -5
ymax = 5

def decision_surface(classifier, X, y):
    is_svm = True
    markersize = 5
    contour_fontsize = 10
    # setting up the grid
    delta = 0.01
    xx = np.arange(xmin, xmax, delta)
    yy = np.arange(ymin, ymax, delta)

    YY, XX = np.meshgrid(yy, xx)
    xy = np.stack([XX.ravel(), YY.ravel()], axis=-1)
    # alternatively:
    # xy = np.column_stack([XX.ravel(), YY.ravel()])
    # print(xy.shape)

    Z = classifier.decision_function(xy).reshape(XX.shape)

    plt.figure(figsize=(5, 5))
    im = plt.imshow(np.transpose(Z),
                    interpolation='bilinear', origin='lower',
                    cmap=plt.cm.gray, extent=(xmin, xmax, ymin, ymax) )

    if is_svm:
        C = plt.contour(np.transpose(Z),
                        [-1, 0, 1],
                        origin='lower',
                        linewidths=(1, 3, 1),
                        colors='black',
                        extent=(xmin, xmax, ymin, ymax))
        plt.scatter(classifier.support_vectors_[:, 0],
                    classifier.support_vectors_[:, 1],
                    s=100, linewidth=1, facecolors="none", edgecolors="k")
    else:
        C = plt.contour(np.transpose(Z),
                        [0],
                        origin='lower',
                        linewidths=3,
                        colors='black',
                        extent=(xmin, xmax, ymin, ymax))

    plt.clabel(C, inline=1, fmt='%1.1f',
               fontsize=contour_fontsize)
    # plot the data
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], plot_str[y[i]], markersize=markersize)

# create an instance of a linear SVM
classifier = svm.SVC(kernel="linear", C=1000)

# train the model:
classifier.fit(X, y)

# visualize:
decision_surface(classifier, X, y)