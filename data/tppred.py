import csv
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
with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/data/wholedata.csv",  encoding="utf8") as file:
    reader=csv.reader(file)
    rows = list(reader)
a = ['']*len(rows)
for i in range(len(rows)):
    a[i]=" " .join(rows[i]).split()


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
