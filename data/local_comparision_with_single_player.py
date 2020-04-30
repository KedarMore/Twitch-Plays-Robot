import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import math

plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#000000'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '1'  # very light grey
# bluish dark grey, but slightly lighter than background
ax = plt.subplot(111)
ax.grid(color='#555555')

for graph in ['final1new.csv','kedarfinal.csv']:
    with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/data/"+graph) as file:
            reader = csv.reader(file, delimiter="\t")
            rows = list(reader)
    input = []
    time = []
    cancelupdown=[]
    cancelleftright=[]
    cancelupdowntime=[]
    cancelleftrighttime = []
    j = 0
    for i in range(len(rows)):
        if rows[i][0] == "w" or rows[i][0] == "W":
            input.insert(j, 1)
            a = float(rows[i][2])
            time.insert(j, a)
            j = j+1
        elif rows[i][0] == "a" or rows[i][0] == "A":
            input.insert(j, 3)
            a = float(rows[i][2])
            time.insert(j, a)
            j = j+1
        elif rows[i][0] == "s" or rows[i][0] == "S":
            input.insert(j, 2)
            a = float(rows[i][2])
            time.insert(j, a)
            j = j+1
        elif rows[i][0] == "d" or rows[i][0] == "D":
            input.insert(j, 4)
            a = float(rows[i][2])
            time.insert(j, a)
            j = j+1

    t = time[0]
    for i in range(len(time)):
        time[i] = time[i]-t
    e = time[-1]
    for i in range(len(time)):
        time[i] = time[i]*100/e
    
    k=0
    if graph == 'final1new.csv':
        for i in range(len(input)):
            tempupdown = 0
            templeftright = 0
            for j in range(35): #original 35
                if input[i] == 1:
                    tempupdown=tempupdown+1
                if input[i] == 2:
                    tempupdown=tempupdown-1
                if input[i] == 3:
                    templeftright=templeftright+1
                if input[i] == 4:
                    templeftright=templeftright-1
                if i<len(input)-1:
                    i=i+1
                else:
                    break
            if tempupdown>=1:
                cancelupdown.insert(k,1)
            else:
                cancelupdown.insert(k,2)
            cancelupdowntime.insert(k,time[i])
            if templeftright>=1:
                cancelleftright.insert(k,3)
            else:
                cancelleftright.insert(k, 4)
            cancelleftrighttime.insert(k,time[i])
    else:
        for i in range(len(input)):
            tempupdown = 0
            templeftright = 0
            for j in range(1):
                if input[i] == 1:
                    tempupdown = tempupdown+1
                if input[i] == 2:
                    tempupdown = tempupdown-1
                if input[i] == 3:
                    templeftright = templeftright+1
                if input[i] == 4:
                    templeftright = templeftright-1
                if i < len(input)-1:
                    i = i+1
                else:
                    break
            if tempupdown >= 1:
                cancelupdown.insert(k, 1)
            else:
                cancelupdown.insert(k, 2)
            cancelupdowntime.insert(k, time[i])
            if templeftright >= 1:
                cancelleftright.insert(k, 3)
            else:
                cancelleftright.insert(k, 4)
            cancelleftrighttime.insert(k, time[i])



    ax=plt.subplot(111)

    if graph=='final1new.csv':
        plt.plot(cancelupdowntime, cancelupdown,linewidth=1, label='all players (total time='+str(int(e))+'secs)')
        plt.plot(cancelleftrighttime, cancelleftright,linewidth=1,color='C0')
        
    if graph == 'kedarfinal.csv':
        plt.plot(cancelupdowntime, cancelupdown,'r-o',linewidth=3, label='single player (total time='+str(int(e))+'secs)')
        plt.plot(cancelleftrighttime, cancelleftright,'r-o',linewidth=3)
    print(cancelupdown)
    print(cancelleftright)

plt.xlabel("time (scaled to 100)")
plt.ylabel("inputs")
y_ticks_labels = ['up','down','left','right'] # 1,2,3,4
ax.set_yticks(np.arange(1,5,1))
ax.set_yticklabels(y_ticks_labels)
plt.title("Comparision of inputs")
plt.legend(title="inputs from players", loc="right")
plt.show()
