from matplotlib.lines import Line2D
import csv
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/final.csv") as file:
    reader = csv.reader(file, delimiter="\t")
    rows = list(reader)
sorted = [0]*len(rows)
time=[0]*len(rows)
t=rows[0][2]
for i in range(len(rows)):
    sorted[i]=rows[i][1]
    time[i]=float(rows[i][2])-float(t)
sorted = list(dict.fromkeys(sorted))
print(sorted)
color=['b','g','r','c','m','y']
ax = plt.subplot(1, 1, 1)
for i in range(len(rows)):
    if rows[i][0]=='w' or rows[i][0]=='W':
        for j in range(len(sorted)):
            if rows[i][1] == sorted[j]:
                ax.bar(time[i], 1, width=1, color=color[j])
    elif rows[i][0] == 's' or rows[i][0] == 'S':
        for j in range(len(sorted)):
            if rows[i][1] == sorted[j]:
                ax.bar(time[i], 2, width=1, color=color[j])
    elif rows[i][0]=='a' or rows[i][0]=='A':
        for j in range(len(sorted)):
            if rows[i][1] == sorted[j]:
                ax.bar(time[i], 3, width=1, color=color[j])
    elif rows[i][0]=='d' or rows[i][0]=='D':
        for j in range(len(sorted)):
            if rows[i][1] == sorted[j]:
                ax.bar(time[i], 4, width=1, color=color[j])
    else:
        for j in range(len(sorted)):
            if rows[i][1] == sorted[j]:
                ax.bar(time[i], 5, width=1, color=color[j])
                # print(str(rows[i][0]))
                # ax.annotate(str(rows[i][0]), (time[i], 5),size=7,rotation=-45)
plt.xlabel("time")
plt.ylabel("inputs")
y_ticks_labels = ['up', 'down', 'left', 'right','other']  # 1,2,3,4,5
ax.set_yticks(np.arange(1, 6, 1))
ax.set_yticklabels(y_ticks_labels)
plt.title("Inputs from all Players over Time")
custom_lines = [Line2D([0], [0], color=color[0], lw=2),
                Line2D([0], [0], color=color[1], lw=2),
                Line2D([0], [0], color=color[2], lw=2),
                Line2D([0], [0], color=color[3], lw=2), 
                Line2D([0], [0], color=color[4], lw=2), 
                Line2D([0], [0], color=color[5], lw=2), ]
plt.legend(custom_lines, ['player1', 'player2', 'player3', 'player4', 'player5', 'player6'])
plt.show()