import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import math
level=2
# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
for players in [4,2,1]:
    with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/"+str(players)+str(level)+".csv") as file:
    # with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/final.csv") as file:
        reader = csv.reader(file, delimiter="\t")
        rows = list(reader)
    input=[]
    time=[]
    j=0
    for i in range(len(rows)):
        for k in range(len(rows[i][0])):
            if rows[i][0][k] == "w" or rows[i][0][k] == "W":
                input.insert(j,1)
            elif rows[i][0][k] == "a" or rows[i][0][k] == "A":
                input.insert(j,3)
            elif rows[i][0][k] == "s" or rows[i][0][k] == "S":
                input.insert(j,2)
            elif rows[i][0][k] == "d" or rows[i][0][k] == "D":
                input.insert(j,4)
            a=float(rows[i][2])
            time.insert(j,a)
            j = j+1
    #print(input)
    yhat = input
    #yhat = savgol_filter(input, 31, 5) # uncomment to use filter
    t=time[0]
    for i in range(len(time)):
        time[i]=time[i]-t
    e=time[-1]
    for i in range(len(time)):
        time[i] = time[i]*100/e
    #print(time)
    if players==1:
        ax=plt.subplot(1,1,1)
        ax.plot(time,yhat,'r-o',label="1 (total time="+str(math.floor(e))+" secs)")
    elif players==2:
        ax=plt.subplot(1,1,1)
        ax.plot(time, yhat, 'g', label="2 (total time="+str(math.floor(e))+"secs)")
    elif players == 4:
        ax = plt.subplot(1, 1,1)
        ax.plot(time, yhat, 'y', label="4 (total time="+str(math.floor(e))+"secs)")
    plt.xlabel("time (scaled to 100)")
    plt.ylabel("inputs")
    y_ticks_labels = ['up','down','left','right'] # 1,2,3,4
    ax.set_yticks(np.arange(1,5,1))
    ax.set_yticklabels(y_ticks_labels)
    plt.title("Comparision of inputs at Level "+str(level))
    plt.legend(title="number of players", loc="upper left")
plt.show()
