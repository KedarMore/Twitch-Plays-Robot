import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as st
import matplotlib.patches as patches
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
        plt.title("Inputs per 1/2 minutes")
        plt.xlabel("time (seconds)")
        plt.ylabel("number of inputs")
        # plt.title("Level: "+str(level)+", Number of Players: "+str(players))
        # plt.xlabel("time")
        # plt.ylabel("number of inputs")
        n, x, _=plt.hist(time, density=False, bins=18, histtype=u'bar',alpha=0,color='w')
        bin_centers = 0.5*(x[1:]+x[:-1])
        ax=plt.subplot(111)
        ax.plot(bin_centers, n)  # using bin_centers rather than edges
        # plt.fill_between(bin_centers, n)
        circle1 = patches.Ellipse([1600, 30], 500, 20, color='red', alpha=0.1)
        ax.add_artist(circle1)
        circle2 = patches.Ellipse([360, 68], 150, 10, color='green', alpha=0.1)
        ax.add_artist(circle2)
        plt.show()
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
