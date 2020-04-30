import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as st
time = []
input=[]
# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/final.csv") as file:
    reader = csv.reader(file, delimiter="\t")
    rows = list(reader)
for i in range(len(rows)):
    time.insert(i,math.floor(float(rows[i][2])))
    input.insert(i,len(rows[i][0]))
    e=time[0]
for i in range(len(rows)):
    time[i]=time[i]-e
print(time)
print(input)
plt.title("Inputs per Minute")
plt.xlabel("time (seconds)")
plt.ylabel("number of inputs")
# plt.title("Level: "+str(level)+", Number of Players: "+str(players))
# plt.xlabel("time")
# plt.ylabel("number of inputs")
n, x, _=plt.hist(time, density=False, bins=38, histtype=u'bar',alpha=0,color='w')
bin_centers = 0.5*(x[1:]+x[:-1])
plt.plot(bin_centers, n)  # using bin_centers rather than edges
# plt.fill_between(bin_centers, n)
plt.show()
# mn, mx = plt.xlim()
# plt.xlim(mn, mx)
# kde_xs = np.linspace(mn, mx, 200)
# kde = st.gaussian_kde(time)
# plt.plot(kde_xs, kde.pdf(kde_xs)*50, label="PDF")
# plt.show() 
