# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:45:46 2018

@author: Ash
"""

import pandas as pd

raw_data = {
        "city": ['LA', 'SF', 'NY', 'Seattle', 'Chicago'],
        "score": [12, 63, 35, 75, 82]
           }

df = pd.DataFrame( raw_data,
                  index = pd.Index ( ['A','B','C','D','E'], name='letter'),
                  columns = pd.Index ( ['city','score'], name='attribute')
                  )

df

bins = [0, 25, 50, 75, 100]
group_names = ['low', 'average', 'good', 'excellent']

df['grade'] = pd.cut(df['score'], bins, labels=group_names)

df

