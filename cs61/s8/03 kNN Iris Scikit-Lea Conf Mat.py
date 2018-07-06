# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:46:24 2018

@author: Ash
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

############################################
iris = load_iris()
ir = pd.DataFrame(iris.data)
ir.columns = iris.feature_names
ir['Class'] = iris.target
ir.head()
ir.describe()
#############################################
# Split data into train + test
#
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.14)

#################################################################
# Classifier kNN
#
clf = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
y_predict = clf.predict(x_test)
accuracy_score(y_test, y_predict)
confusion_matrix(y_test,y_predict)

##########################################################
accuracy_values=[]
k_values=[]
x_train.shape[0]

for x in range(1,x_train.shape[0]):
    clf = KNeighborsClassifier(n_neighbors=x).fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    accuracy = accuracy_score(y_test, y_predict)
    accuracy_values.append(accuracy)
    k_values.append(x)
    pass

accuracy_values = np.array(accuracy_values)
k_values = np.array(k_values)

plt.plot(k_values,accuracy_values)
plt.xlabel("K")
plt.ylabel("Accuracy")

##########################################################


