# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from sklearn import neighbors

################################################
# Read Food Dataset
#
df = pd.read_csv('04 food1-16.csv')
df
 
###################################################
# Split data into train + test
#        
X = np.array(df[['Sweetness','Crunchiness']])
X

y = df['Food Type']
y
######################################################
X_train = X[0:15,]
X_train

y_train = y[0:15]
y_train

################################################
X_test = X[15:16,]
X_test

#####################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=1)
clf.fit(X_train, y_train)
clf.predict(X_test)

######################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
clf.predict(X_test)

#####################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)
clf.predict(X_test)

####################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=9)
clf.fit(X_train, y_train)
clf.predict(X_test)
######################################################

