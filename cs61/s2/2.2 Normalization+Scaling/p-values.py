# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:37:09 2018

@author: Ash
"""

import scipy
z_scores = 0

p_values = scipy.stats.norm.sf(abs(z_scores))
p_values