from IPython.display import clear_output
import csv
import numpy as np
import matplotlib.pyplot as plt
import math
# import scipy.stats as st

import matplotlib.patches as patches
import sys
# import numpy as np
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
with open("home/abhijeet/wholedata.csv",  encoding="utf8") as file:
    reader = csv.reader(file)
    rows = list(reader)
a = ['']*len(rows)
for i in range(len(rows)):
    a[i] = " " .join(rows[i]).split()

time = [0]*len(rows)
for i in range(len(rows)):
    if len(a[i][1]) == 8:
        t1 = list(map(int, a[i][1].split(":")))
        t0 = list(map(int, a[i][0].split("-")))
        time[i] = t1[2]+t1[1]*60+t1[0]*3600+t0[2]*3600*24+t0[1]*3600*24*28
    if len(a[i][1]) == 5:
        t1 = list(map(int, a[i][1].split(":")))
        t0 = list(map(int, a[i][0].split("-")))
        time[i] = t1[1]*60+t1[0]*3600+t0[2]*3600*24+t0[1]*3600*24*28
t = time[0]
for i in range(len(rows)):
    time[i] = time[i]-t

sort = ['']*len(rows)
for i in range(len(rows)):
    sort[i] = a[i][2]
sort = list(dict.fromkeys(sort))

players = ['']*len(rows)
for i in range(len(rows)):
    players[i] = a[i][2]

noofchats = [0]*len(sort)
for i in range(len(sort)):
    noofchats[i] = players.count(sort[i])
    clear_output(wait=True)
    print(len(sort)-i, flush=True)

plt.hist(noofchats, density=False, bins=384, histtype='step')
plt.show()
plt.savefig("home/abhijeet/graph.jpg")
