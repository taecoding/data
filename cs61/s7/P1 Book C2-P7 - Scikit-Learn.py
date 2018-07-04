# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:42:45 2018

@author: Ash
"""

import numpy as np
import pandas as pd
from sklearn import neighbors

###############################################
# Read the Training and Test dataset
#
train = pd.read_csv("P1 Book C2 - P7 - Train.csv")
test = pd.read_csv("P1 Book C2 - P7 - Test.csv")

print(train)
print(test)

X_train = np.array(train[['X1','X2','X3']])
X_train

y_train = train['Y']
y_train

X_test = np.array(test[['X1','X2','X3']])
X_test
#####################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=1)
clf.fit(X_train, y_train)
clf.predict(X_test)

#####################################################
clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
clf.predict(X_test)

