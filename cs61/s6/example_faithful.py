# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:03:09 2018

@author: ash
"""
####################################################
# June 10, 2018
# Data: Old Faithful
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

######################################
# 1. Read Data File + Show dimensions + Plot Data
#
data = np.genfromtxt('oldfaithful.csv',delimiter=',',skip_header=1)
#data = data[0:20]
print(data)
data.shape

eruptionX = data[:,0]
waitingY = data[:,1]

eruptionX.shape
waitingY.shape

plt.figure()
plt.plot(eruptionX, waitingY,'.b',label='Observation')
plt.xlabel('Eruption Duration (minutes)')
plt.ylabel('Time Between Eruptions (minutes)')


#####################################
# 2. Regression with all data 
# Compute Regression Equation + + Plot Regression Line
#
reg = linear_model.LinearRegression()

df_x = pd.DataFrame(eruptionX)
df_y = pd.DataFrame(waitingY)

df_x.describe()
df_y.describe()

reg.fit(df_x,df_y)
reg.coef_
reg.intercept_

# Plot Regression Line
#
plot_x = np.array([1.5,5.5])
plot_y = reg.coef_[0]*plot_x + reg.intercept_

plt.figure()
plt.plot(eruptionX, waitingY,'.b',label='Observation')
plt.xlabel('Eruption Duration (minutes)')
plt.ylabel('Time Between Eruptions (minutes)')
plt.plot(plot_x, plot_y, 'r:', label='Linear Regression')

####################################################
# 2.1. Compute Predicted Values + RSquare
#
predicted_value = reg.predict(df_x)

r2_score(waitingY,predicted_value)
r2_score(df_y,predicted_value)

###################################################
# 3. Split data into Training / Testing
#
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=0)

x_train
y_train

x_test
y_test

x_train.shape
y_train.shape
x_test.shape
y_test.shape

plt.plot(x_train, y_train,'.b')
plt.plot(x_test, y_test,'.b')
#################################################
# 4. Build Regression model using training data
#
reg_train = linear_model.LinearRegression()

reg_train.fit(x_train,y_train)
reg_train.coef_
reg_train.intercept_

################################################
# 5.1 Predict Using Training data
# Compute Training MSE
#
predcited_values_training = reg_train.predict(x_train)
mean_squared_error(y_train, predcited_values_training)

# 5.2 Predict Using Testing data
# Compute Testing MSE
#
predcited_values_testing = reg_train.predict(x_test)
mean_squared_error(y_test, predcited_values_testing)

