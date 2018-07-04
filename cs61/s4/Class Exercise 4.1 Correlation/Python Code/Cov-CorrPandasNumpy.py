# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:45:05 2018

@author: Ash
"""

import numpy as np
import pandas as pd

df = pd.read_csv('BaseballData-BestPredictor.csv')
df[0:10]


##################################################
# Correlation + Covariance in Pandas
#
df.corr()
df.cov()

##############################################
# Correlation + Covariance in Numpy
#
A1array = np.array(df['wP'])
B2array = np.array(df['rS'])
B3array = np.array(df['hR'])
B4array = np.array(df['tbA'])
B5array = np.array(df['obP'])
B6array = np.array(df['baaT'])
B7array = np.array(df['terA'])

print(Aarray)
print(Barray)

np.corrcoef(A1array,B2array)
np.corrcoef(A1array,B3array)
np.corrcoef(A1array,B4array)
np.corrcoef(A1array,B5array)
np.corrcoef(A1array,B6array)
np.corrcoef(A1array,B7array)

np.cov(A1array,B2array)

#############################################