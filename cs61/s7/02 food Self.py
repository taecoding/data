# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from collections import Counter

################################################
# Read Food Dataset
#
train = pd.read_csv('03 food1-15.csv')
test = pd.read_csv('05 food16.csv')
train
test
 
#####################################################
################################################
# Compute the distance
# from Test object to all the Train's objects
#
trainC = train.shape[0]
print(trainC)
sum = np.zeros(trainC)

for i in range (0, trainC):
    sum[i] = sum[i] + (train.Sweetness[i] - test.Sweetness[0])**2
    sum[i] = sum[i] + (train.Crunchiness[i] - test.Crunchiness[0])**2

distance = np.sqrt(sum)
print(sum)
print(distance)
train['dist'] = distance
print(train)

###########################################
# Sort the dataset by distance
#
trainSorted = train.sort_values(['dist'])
print(trainSorted)

#############################################
# Find the nearest neighbor
#
k = 1
nearestNeighbor = trainSorted.FoodType[0:k]
print(nearestNeighbor)
Counter(nearestNeighbor)

k = 3
nearestNeighbor = trainSorted.FoodType[0:k]
print(nearestNeighbor)
Counter(nearestNeighbor)
