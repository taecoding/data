# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:24:44 2018

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
Xlist = [3765, 3984, 3530, 3175, 2580, 3730, 2605, 3772, 3310, 2991, 2752]
Ylist = [19, 18, 21, 22, 27, 18, 26, 17, 20, 25, 26]

#####################################
# Problem 4a: Regression Using Scikit-Learn
#
df_x = pd.DataFrame(Xlist)
df_y = pd.DataFrame(Ylist)

reg = linear_model.LinearRegression()

reg.fit(df_x,df_y)
print(reg.coef_)
print(reg.intercept_)

####################################
# Problem 4b
# slope: For every pound added to the weight of the car will reduce the gas mileage by 0.007 MPG
# intercept: Interpretation of intercept is outside the scope of the model

#######################################
# Problem 4c
weight = 2780

MPG = weight * reg.coef_ + reg.intercept_
print(MPG)

# Since 22 < 25.318.  Below average

########################################
# 4 d
# No. This data is for internal combustion engines only.
# Toyota Prium is a hybrid car
#