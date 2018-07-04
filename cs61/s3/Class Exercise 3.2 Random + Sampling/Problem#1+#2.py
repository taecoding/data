# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 05:37:51 2018

@author: Ash
"""

import numpy as np
import random
import matplotlib.pyplot as plt
##################################################
# Problem#1
#
ran_sample = []
for i in range(0,10000):
    sample1 = random.randint(1,6)
    sample2 = random.randint(1,6)
    ran_sample.append(sample1 + sample2)

plt.hist(ran_sample,bins=11)

##############################################
## Problem#2
## Sampling
#
name = ['A','B','C','D','E','F','G','H','I','J']
print(name)

random.shuffle(name)
print(name)

train = random.sample(name,k=7)
print(train)

test = list(set(name) - set(train))
print(test)
#################################################


