# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 20:06:12 2018

@author: Ash
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

######################################
# 1. Read Data File 
#
Xlist = [25, 30, 35, 40, 45]
Ylist = [5, 260, 480, 745, 1100]
#######################################
Xarray = np.array(Xlist)
Yarray = np.array(Ylist)

XYarray = Xarray * Yarray
XYarray

X2array = Xarray**2
X2array
#################################################
meanX = np.mean(Xarray)
print(meanX)

meanY = np.mean(Yarray)
print(meanY)

meanXY = np.mean(XYarray)
print(meanXY)

meanX2 = np.mean(X2array)
print(meanX2)

stdX = np.std(Xarray)
print(stdX)

stdY = np.std(Yarray)
print(stdY)

r = np.corrcoef(Xarray, Yarray)
r[0][1]


########################################
# Problem 1a : Closed form solution - using only the mean of X, Y, XY, X^2
#
slope = (meanXY - (meanX*meanY))/(meanX2 - meanX*meanX)
print(slope)

intercept = meanY - slope*meanX
print(intercept)

#######################################
# Problem 1b: Using Correlation and Standard Deviation

slope = r[0][1]*stdY/stdX
print(slope)

#####################################
# Problem 1c: Regression Using Scikit-Learn
#
df_x = pd.DataFrame(Xlist)
df_y = pd.DataFrame(Ylist)

reg = linear_model.LinearRegression()

reg.fit(df_x,df_y)
print(reg.coef_)
print(reg.intercept_)

##########################################

