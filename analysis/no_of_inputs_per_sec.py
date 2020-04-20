import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as st
time=[]
input=[]
# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
for players in [1]:
    for level in [1]:
        # with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/"+str(players)+str(level)+".csv") as file:
        with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/final.csv") as file:
            reader = csv.reader(file, delimiter="\t")
            rows = list(reader)
        for i in range(len(rows)):
            time.insert(i,math.floor(float(rows[i][2])))
            input.insert(i,len(rows[i][0]))
        e=time[0]
        for i in range(len(rows)):
            time[i]=(time[i]-e)
        print(time)
        print(input)
        plt.title("All players (local)")
        plt.xlabel("time")
        plt.ylabel("number of inputs")
        # plt.title("Level: "+str(level)+", Number of Players: "+str(players))
        # plt.xlabel("time")
        # plt.ylabel("number of inputs")
        plt.hist(time,density=False,bins=300,histtype=u'step')
        # mn, mx = plt.xlim()
        # plt.xlim(mn, mx)
        # kde_xs = np.linspace(mn, mx, 200)
        # kde = st.gaussian_kde(time)
        # plt.plot(kde_xs, kde.pdf(kde_xs)*50, label="PDF")
        # plt.show() 
        file.close()
        plt.show()
        plt.savefig('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/inputs_per_sec' + str(players)+str(level)+'.png')
        plt.close()
        time = []
        input = []
