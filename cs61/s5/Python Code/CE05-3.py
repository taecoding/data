# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:03:01 2018

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
Xlist = [27.75, 24.5, 25.5, 26, 25, 27.75, 26.5, 27, 26.75, 26.75, 27.5]
Ylist = [17.5, 17.1, 17.1, 17.3, 16.9, 17.6, 17.3, 17.5, 17.3, 17.5, 17.5]

#####################################
# Problem 3a: Regression Using Scikit-Learn
#
df_x = pd.DataFrame(Xlist)
df_y = pd.DataFrame(Ylist)

reg = linear_model.LinearRegression()

reg.fit(df_x,df_y)
print(reg.coef_)
print(reg.intercept_)

##########################################
# 3 b
# slope: if height increases by 1 inch, head-circumference increases by 0.1827 inches
#
# intercept:  If height is zero, head circumfrence = 12.49.  This is absured.  
# Therefore, interpretation is outside the scope of the model

##########################################
# 3 d
height = 25

head_cir = height * reg.coef_ + reg.intercept_
residual = head_cir - 16.9
print(residual)

