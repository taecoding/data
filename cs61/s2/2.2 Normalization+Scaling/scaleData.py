# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:42:23 2018

@author: Ash
"""
import pandas as pd
import numpy as np

df = pd.read_csv('Data.csv')
df
Xarray = np.array(df['X'])

XNormalize = ( Xarray - np.mean(Xarray))/np.std(Xarray)
print(XNormalize)

XScale = ( Xarray - np.min(Xarray))/(np.max(Xarray) - np.min(Xarray))
print(XScale)

df['Normalize'] = XNormalize
df['Scale'] = XScale
df


