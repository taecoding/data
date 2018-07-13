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
dataset = pd.read_csv("Mall_Customers.csv")
dataset
len(dataset)
#########################################################
# Since we are performing clustering
# we only need X variable
#
# Clustering is a unsupervised method, 
# that's why we do NOT need the response variable or the 'y' variable
#
X = dataset.iloc[:,[3,4]].values

##########################################################
# Plot the dendrogram
# The plot will determine how many clusters we should need
#

import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Eucledian Distance')

plt.show()

# We can have 3 clusters as standard
# Or we can have 5 clusters
# Find the longest line which is not crossed by horizontal line
#
# This shows total number of clusters = 5
#
 
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean',linkage='average')

y_hc = hc.fit_predict(X)

plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=50,c='red',label='Cluster1')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=50,c='blue',label='Cluster2')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=50,c='green',label='Cluster3')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=50,c='cyan',label='Cluster4')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=50,c='magenta',label='Cluster5')

plt.title('Cluster of the Customers')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()









import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist


from pylab import rcParams
import seaborn as sb


import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm

############################################################
np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10,3))
#%matplotlib inline
plt.style.use('seaborn-whitegrid')

##########################################################

cars.columns = ['car_names','mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

##########################################################
#X = cars.ix[:,(1,3,4,6)].values
X = cars.iloc[:,[1,3,4,6]].values

#y = cars.ix[:,(9)].values
y = cars.iloc[:,[9]].values

##############################################################
#
z = linkage(X,'ward')

dendrogram(z, truncate_mode='lastp', p=12, leaf_rotation=45, leaf_font_size=15., show_contracted=True)

plt.title('Truncated Hierarchical Clustering Dendogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')
plt.axhline(y=500)
plt.axhline(y=150)

############################################################
k = 2
#HClustering=AgglomerativeClustering(n_clusters=k, affinity='eculidean',linkage='ward')

HClustering=AgglomerativeClustering(n_clusters=k,linkage='ward')

HClustering.fit(X)

sm.accuracy_score(y,HClustering.labels_)

##########################################################

HClustering=AgglomerativeClustering(n_clusters=k,linkage='complete')

HClustering.fit(X)

sm.accuracy_score(y,HClustering.labels_)

##########################################################

HClustering=AgglomerativeClustering(n_clusters=k,linkage='average')

HClustering.fit(X)

sm.accuracy_score(y,HClustering.labels_)

############################################################
HClustering=AgglomerativeClustering(n_clusters=k, affinity='manhattan',linkage='average')

HClustering.fit(X)

sm.accuracy_score(y,HClustering.labels_)

################################################################

