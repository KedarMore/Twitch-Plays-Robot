from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
# from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import math

totaltime = np.array([63.56, 121.29, 121.29, 121.29, 56.64, 56.64, 56.64, 56.64, 400,400,400, 2281])
noofplayers=np.array([1,2,2,2,4,4,4,4,6,6,6,29])

plt.xlabel("number of players")
plt.ylabel("total time (in seconds)")
plt.title("Change in total time w.r.t number of players (Level 3)")

u=np.linspace(0,1,50)

Px = noofplayers[0]*1*np.power(u,4)+noofplayers[1]*4*np.power(u,3) * (1-u)+noofplayers[2]*6*np.power(u,2)*np.power((1-u),2)+noofplayers[3]*4*u*np.power((1-u),3)+noofplayers[4]*1*np.power((1-u),4)
Py= totaltime[0]*1*np.power(u,4)+totaltime[1]*4*np.power(u,3) * (1-u)+totaltime[2]*6*np.power(u,2)*np.power((1-u),2)+totaltime[3]*4*u*np.power((1-u),3)+totaltime[4]*1*np.power((1-u),4)

points=len(noofplayers)

Px=0
Py=0
for i in range(points):
    Px=Px+(math.factorial(points-1)/(math.factorial(i)*math.factorial(points-1-i)))*noofplayers[i]*np.power(u,points-1-i)*np.power(1-u,i)
    Py = Py+(math.factorial(points-1)/(math.factorial(i)*math.factorial(points-1-i)))*totaltime[i]*np.power(u, points-1-i)*np.power(1-u, i)

num=0

# for i in [0,1,4,8,11]:
#     plt.plot(noofplayers[i], totaltime[i],'o', color="C"+str(num), Label="Number of Players= "+str(noofplayers[i])+" with time= "+str(totaltime[i])+" secs")
#     plt.annotate(str(noofplayers[i]), (noofplayers[i], totaltime[i]))
#     num=num+1

plt.plot(noofplayers, totaltime, '-o',color="C0", alpha=1, Label="actual", linewidth=1)
# plt.plot(noofplayers, totaltime, 'o', color="b")
plt.plot(Px, Py, color="red", Label="best fit")
plt.legend()
plt.show()
