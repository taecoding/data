# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:14:51 2018

@author: Ash
"""
from sklearn import datasets
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

########################################
# Load Data
# 
iris = datasets.load_iris()
X_iris = iris.data

# Retrieve only the first 2 variables
# Petal Length + Petal Width from the data
#
X2_iris = iris.data[:,0:2]

#print(X2_iris)
#y_iris = iris.target
#print(y_iris)
#len(y_iris)

plt.scatter(X2_iris[:,0], X2_iris[:,1], s=10, linewidth=5)
plt.show()

##################################
clf = KMeans(n_clusters=3)
clf.fit(X2_iris)

centroids = clf.cluster_centers_
labels = clf.labels_
print(centroids)
print(labels)

####################################
# Colors = Green, Red, Cyan, Blue, Black, Green
colors = ["g.","r.","c.","b.","k.","g."]

for i in range(len(X2_iris)):
    plt.plot(X2_iris[i][0], X2_iris[i][1], colors[labels[i]], markersize = 10)
    
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidth=5)
plt.show()
    