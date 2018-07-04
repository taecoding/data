# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:07:14 2018

@author: Ash
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#matplotlib inline   #For Jupyter only

test = np.random.normal(0,1,10000)
plt.plot(test)
plt.hist(test)

sm.qqplot(test)
sm.qqplot(test,line='45')

################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
y_axis = norm.pdf(x_axis,0,2)
plt.plot(x_axis, y_axis)

sm.qqplot(y_axis)
sm.qqplot(y_axis,line='45')

