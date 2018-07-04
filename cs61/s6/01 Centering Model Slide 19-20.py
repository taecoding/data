# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 20:06:12 2018

@author: Ash
"""

import numpy as np
import pandas as pd
from sklearn import linear_model

######################################
# 1. Read Data File 
#
Price = [49, 69, 89, 99, 109]
Demand = [124, 95, 71, 45, 18]
#######################################
Xarray = np.array(Price)
Yarray = np.array(Demand)

meanX = np.mean(Xarray)
print(meanX)

meanY = np.mean(Yarray)
print(meanY)

Xarray_modified = Xarray - meanX
print(Xarray_modified)

Yarray_modified = Yarray - meanY
print(Yarray_modified)
#####################################
# Regression Using Scikit-Learn
# Without Centering
#
df_x = pd.DataFrame(Xarray)
df_y = pd.DataFrame(Yarray)

reg = linear_model.LinearRegression()

reg.fit(df_x,df_y)
print(reg.coef_)
print(reg.intercept_)

##########################################
# Regression Using Scikit-Learn
# Centering the model
#
df_x = pd.DataFrame(Xarray_modified)
df_y = pd.DataFrame(Yarray_modified)

reg = linear_model.LinearRegression()

reg.fit(df_x,df_y)
print(reg.coef_)
print(reg.intercept_)

##########################################