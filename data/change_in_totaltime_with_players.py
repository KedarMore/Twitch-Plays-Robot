from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.signal import savgol_filter

import matplotlib.pyplot as plt
totaltime=np.array([2,4,6,7,8,8,7,6,5,5,5,5,5,6,7,9,11,13,16,20,22,24,25,26,26,27,27])
noofplayers=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])

yhat = savgol_filter(totaltime, 25, 6)
ax=plt.subplot(111)

ax.set_xticks(np.arange(1, 27, 4))
ax.set_xticklabels([1,10,100,1000,10000,100000,1000000])
ax.set_yticks(np.arange(2, 27, 3))
ax.set_yticklabels([1,5,10,50,100,500,1000,5000,10000])
plt.xlabel("number of players")
plt.ylabel("total time (in hours)")
plt.title("Change in total time w.r.t number of players")
ax.plot(noofplayers,yhat)

plt.show()
