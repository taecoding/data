# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:42:45 2018

@author: Ash
"""

import numpy as np
import pandas as pd
from collections import Counter

###############################################
# Read the Training and Test dataset
#
train = pd.read_csv("P1 Book C2 - P7 - Train.csv")
test = pd.read_csv("P1 Book C2 - P7 - Test.csv")

print(train)
print(test)

################################################
# Compute the distance
# from Test object to all the Train's objects
#
trainC = train.shape[0]
print(trainC)
sum = np.zeros(trainC)

for i in range (0, trainC):
    #print(i)
    sum[i] = sum[i] + (train.X1[i] - test.X1[0])**2
    sum[i] = sum[i] + (train.X2[i] - test.X2[0])**2
    sum[i] = sum[i] + (train.X3[i] - test.X3[0])**2

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
nearestNeighbor = trainSorted.Y[0:k]
print(nearestNeighbor)
Counter(nearestNeighbor)

k = 3
nearestNeighbor = trainSorted.Y[0:k]
print(nearestNeighbor)
Counter(nearestNeighbor)

############################################