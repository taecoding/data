# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:50:42 2018

@author: Ash
"""

import pandas as pd
df = pd.read_csv('StudentPoints.csv')
df[0:10]

bins = [0, 60, 70, 80, 90, 100]
group_names = ['F', 'D', 'C', 'B','A']

c1 = pd.cut(df['Points'], bins, labels=group_names)

print(c1.value_counts())
dict(c1.value_counts())

print( df['Points'][0:50] )
print( c1[0:50] )

df['grade'] = pd.cut(df['Points'], bins, labels=group_names)
df[0:50]

###################################################

