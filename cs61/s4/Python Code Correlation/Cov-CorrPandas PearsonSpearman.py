# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:45:05 2018

@author: Ash
"""

import numpy as np
import pandas as pd
##################################################
# Correlation + Covariance in Pandas
#
df1 = pd.DataFrame({'A':[6,10,14,19,21], 'B':[5,3,7,8,12]})
df1

df1.corr()
df1.cov()

df1.corr(method='pearson')
df1.corr(method='spearman')
df1.corr(method='kendall')

##############################################
# Correlation + Covariance in Numpy
#
Alist = [6,10,14,19,21]
Blist =[5,3,7,8,12]

Aarray = np.array(Alist)
Barray = np.array(Blist)

np.corrcoef(Aarray,Barray)
np.cov(Aarray,Barray)

#############################################