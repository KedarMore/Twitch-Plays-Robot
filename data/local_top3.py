import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as st

with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/data/final1new.csv") as file:
    reader = csv.reader(file,delimiter="\t")
    rows = list(reader)

chat1=[]
chat2 = []
chat3 = []

for i in range(len(rows)):
    if rows[i][1]=='Fifa Mobile':
        chat1.append(float(rows[i][2]))
    if rows[i][1] == 'Saptarshi Mitra':
        chat2.append(float(rows[i][2]))
    if rows[i][1] == 'Abhijeet D.Srivastava':
        chat3.append(float(rows[i][2]))

# print(rows[0][1])
# plt.hist(chat1, density=False, bins=20, histtype='step', label='Fifa Mobile')
# plt.hist(chat2, density=False, bins=20, histtype='step', label='Saptarshi Mitra')
# plt.hist(chat3, density=False, bins=20, histtype='step', label='Abhijeet Srivastava')

plt.title("Top 3 Players with Maximum Input")
plt.xlabel("time (seconds)")
plt.ylabel("no of chats")

n, x, _ = plt.hist(chat1, density=False, bins=5,
                   histtype=u'bar', alpha=0, color='w')
bin_centers = 0.5*(x[1:]+x[:-1])
# using bin_centers rather than edges
plt.plot(bin_centers, n, label='Fifa Mobile')
# plt.fill_between(bin_centers, n)

n, x, _ = plt.hist(chat2, density=False, bins=5,
                   histtype=u'bar', alpha=0, color='w')
bin_centers = 0.5*(x[1:]+x[:-1])
# using bin_centers rather than edges
plt.plot(bin_centers, n, label='Saptarshi Mitra')
# plt.fill_between(bin_centers, n)

n, x, _ = plt.hist(chat3, density=False, bins=5,
                   histtype=u'bar', alpha=0, color='w')
bin_centers = 0.5*(x[1:]+x[:-1])
# using bin_centers rather than edges
plt.plot(bin_centers, n, label='Abhijeet Srivastava')
# plt.fill_between(bin_centers, n)
plt.legend()

plt.show()
