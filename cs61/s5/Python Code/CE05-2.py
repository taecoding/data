# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 07:45:48 2018

@author: Ash
"""

#############################################
# Problem #2
# Video Games and GPA
# y (GPA) = -0.0526 * x (Hours Video Games) + 2.9342
#
slope = -0.0526
intercept = 2.9342

##############################################
# 2 a
hoursVideoGames = 8

GPA = hoursVideoGames * slope + intercept
print(GPA)

##############################################
# 2 b

# Every additional hour of video game played, decreases the GPA by 0.0526
#
#############################################
# 2 c
#
# When the value of 'x' (number of hours video games played) is zero, 
# GPA = 2.9342
#
#############################################
#  2 d
hoursVideoGames = 7

GPA = hoursVideoGames * slope + intercept
print(GPA)

# Since 2.68 > 2.566
# Above the average


