# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 05:37:51 2018

@author: Ash
"""

import numpy as np
import matplotlib.pyplot as plt
import string

import random

############################################
# 1. Random number between 0 - 1
#
value = random.random()
print (value)

##################################################
# 2. Single number from Uniform distribution
#
print(random.uniform(2000,2015))

print(random.randint(0,100))
#################################################
# 3. Uniform Distribution
#
ran_sample = []
for i in range(0,10000):
    sample = random.randint(0,100)
    ran_sample.append(sample)

plt.hist(ran_sample,bins=10)
##############################################
# 3.1 Simulation of a Die + Toss
#
value = random.randint(1,6)
print (value)
#
value = random.randint(0,1)
print (value)
###############################################
# 4. Sorting the random numbers
#
ran_sample = []
for i in range(0,10):
    sample = random.randint(0,100)
    ran_sample.append(sample)

ran_sample
ran_sample.sort()
ran_sample

##################################################
# 5. Random number with replacement
# A series of random numbers with replacement
# 
random.randrange(1900,2010,10)

ran_sample = []
for i in range(0,10):
    sample = int(random.uniform(2000,2015))
    ran_sample.append(sample)

print(ran_sample)
ran_sample.sort()
print(ran_sample)

##################################################
# 6. String set sorting
#
my_cards = ['club','spade','heart','diamond']

random.shuffle(my_cards)
my_cards

my_card = random.choice(my_cards)
print(my_card)

###########################
greetings = ['Hello','Hi','Hey','Howdy','Hola']

value = random.choice(greetings)

print(value + ', Ash')
#################################################
# 7. random selection
#
print(random.choice(['yes','no','maybe']))

##################################################
# 8. Gaussian Distribution
#
test_list = []
for i in range (0,10000):
    test_list.append(random.gauss(100,25))
    
len(test_list)

sum(test_list)/10000
print(np.std(test_list))

plt.hist(test_list,bins=100)

#################################################
# 9. Random Password generation
#
print (string.digits)
print(string.ascii_letters)

pw = ''
for i in range(0,16):
    ran_char = random.choice(string.ascii_letters + string.digits)
    pw = pw + ran_char

print(pw)

####################################################
# 10. Random numbers - Normal Distribution
#
r = np.random.randn(10000)
plt.hist(r,bins=100)

r = 10*np.random.randn(10000) + 30
plt.hist(r,bins=100)
################################################
# 11. Simulation of deck of cards + Sampling
#
deck = list(range(1,53))
print(deck)

random.shuffle(deck)
print(deck)

hand = random.sample(deck,k=5)
print(hand)
