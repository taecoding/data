# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:20:08 2018

@author: Ash
"""

import scipy.stats as st
###########################################
# Convert z-value of 1.64 into p-value
#
st.norm.cdf(1.64)

############################################
# Convert  p-value of 0.95 into z-value
#
st.norm.ppf(0.95)





import numpy as np
##########################################
# Problem#1
#
d1_list = [-2.45, -0.43, 1.35, 3.49]
d1_array = np.array(d1_list)
st.norm.cdf(d1_array)

#########################################
# Problem#2
#
d2_list = [-3.01, -1.59, 1.78, 3.11]
d2_array = np.array(d2_list)
1 - st.norm.cdf(d2_array)

##########################################
# Problem#3
#
d3_list = [-2.04, -0.55, -1.04]
d4_list = [2.04, 0, 2.76]
d3_array = np.array(d3_list)
d4_array = np.array(d4_list)

st.norm.cdf(d4_array) - st.norm.cdf(d3_array)


##########################################
# Problem#4
#
d5_list = [-2, -1.56, -0.24]
d6_list = [2, 2.56, 1.20]
d5_array = np.array(d5_list)
d6_array = np.array(d6_list)

st.norm.cdf(d5_array) + (1 - st.norm.cdf(d6_array))

###########################################


