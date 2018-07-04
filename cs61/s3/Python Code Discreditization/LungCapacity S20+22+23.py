# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:50:42 2018

@author: Ash
"""

import pandas as pd
df = pd.read_csv('Lung Capacity.csv')
df[0:10]

bins = [0, 50, 55, 60, 65, 70, 100]
group_names = ['A', 'B', 'C', 'D','E','F']

c1 = pd.cut(df['Height'], bins, labels=group_names)

print(c1.value_counts())
dict(c1.value_counts())

print( df['Height'][0:8] )
print( c1[0:8] )

df['grade'] = pd.cut(df['Height'], bins, labels=group_names)
df[0:8]

###################################################

import matplotlib.pyplot as plt
plt.hist(c1.value_counts())
