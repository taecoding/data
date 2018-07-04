# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:26:19 2018

@author: Ash
"""

# Imports Libraries
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
######################################
X = [25, 30, 35, 40, 45]
y = [5, 260, 480, 745, 1100]


plt.figure()
plt.plot(X, y, "b.")
plt.xlabel('Price')
plt.ylabel('Demand')
plt.xlim([40, 110])
plt.ylim([10, 130])
plt.show()

X_b = np.c_[np.ones((5,1)), X]
print(X_b)

X_T_X = X_b.T.dot(X_b)
print(X_T_X)

X_T_X = X_b.T.dot(X_b)
print(X_T_X)

X_T_X_I = np.linalg.inv(X_T_X)
print(X_T_X_I)

X_T_Y = X_b.T.dot(y)
print(X_T_Y)

answer = X_T_X_I.dot(X_T_Y)
print(answer)
