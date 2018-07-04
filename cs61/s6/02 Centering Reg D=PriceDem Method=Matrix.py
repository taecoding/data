############################################
# Regression Matrix Method
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

X = [49, 69, 89, 99, 109]
y = [124, 95, 71, 45, 18]

plt.plot(X, y, "b.")
plt.xlabel("$Price$", fontsize=18)
plt.ylabel("$Demand$", rotation=90, fontsize=18)
plt.axis([40, 110, 10, 130])

X_b = np.c_[np.ones((5,1)), X]
print(X_b)

X_T_X = X_b.T.dot(X_b)
print(X_T_X)

X_T_X_I = np.linalg.inv(X_T_X)
print(X_T_X_I)

X_T_Y = X_b.T.dot(y)
print(X_T_Y)

answer = X_T_X_I.dot(X_T_Y)
print(answer)

###########################################################
###########################################################
############################################################
# Center the model
#
Xarray = np.array(X)
Yarray = np.array(y)

meanX = np.mean(Xarray)
print(meanX)

meanY = np.mean(Yarray)
print(meanY)

Xarray_modified = Xarray - meanX
print(Xarray_modified)

Yarray_modified = Yarray - meanY
print(Yarray_modified)

####################################
X = Xarray_modified
y = Yarray_modified

X_b = np.c_[X]
print(X_b)

X_T_X = X_b.T.dot(X_b)
print(X_T_X)

X_T_X_I = np.linalg.inv(X_T_X)
print(X_T_X_I)

X_T_Y = X_b.T.dot(y)
print(X_T_Y)

answer = X_T_X_I.dot(X_T_Y)
print(answer)
