# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:19:09 2018

@author: Ash
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

X = np.array([ [1,1],
        [2,1],
        [4, 3],
        [5,4]])
print(X)
plt.scatter(X[:,0], X[:,1], s=10, linewidth=5)
plt.show()

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_
print(centroids)
print(labels)

####################################
# Colors = Green, Red, Cyan, Blue, Black, Green
colors = ["g.","r.","c.","b.","k.","g."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
    
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidth=5)
plt.show()
    