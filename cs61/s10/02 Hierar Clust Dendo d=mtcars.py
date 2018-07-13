# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:51:39 2018

@author: Ash
"""
###########################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

###########################################################
dataset = pd.read_csv("mtcars.csv")
dataset
len(dataset)

dataset.columns = ['car_names','mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
dataset
#########################################################
# Since we are performing clustering
# we only need X variable
#
# Clustering is a unsupervised method, 
# that's why we do NOT need the response variable or the 'y' variable
#
# Retrieve only 'mpg' and 'hp'
#
#X = dataset.iloc[:,[1,3,4,6]].values
X = dataset.iloc[:,[1,4]].values
X

##########################################################
# Plot the dendrogram
# The plot will determine how many clusters we should need
#

import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(X,method='ward'))
plt.axhline(y=300)
plt.axhline(y=150)
plt.title('Dendrogram')
plt.xlabel('Cars')
plt.ylabel('Eucledian Distance')

plt.show()

# Find the longest line which is not crossed by horizontal line
#
# This shows total number of clusters = 4
#
 
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=4, affinity='euclidean',linkage='average')

y_hc = hc.fit_predict(X)

size = 50
plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=size,c='red',label='Cluster1')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=size,c='blue',label='Cluster2')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=size,c='green',label='Cluster3')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=size,c='cyan',label='Cluster4')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=size,c='magenta',label='Cluster5')

plt.title('Cluster of the Cars')
plt.xlabel('mpg')
plt.ylabel('hp')
plt.legend()

##############################################
