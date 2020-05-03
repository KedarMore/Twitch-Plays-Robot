import csv
import numpy as np
import matplotlib.pyplot as plt
# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/data/final1new.csv") as file:
    reader=csv.reader(file,delimiter="\t")
    rows = list(reader)
a=np.zeros(len(rows))
j=0
for i in rows:
    a[j]=float(i[2])
    j=j+1
a=a-a[0]
no=range(len(rows))
plt.plot(a,no)
plt.title("Level: 5, Number of Players: 4")
plt.xlabel("time")
plt.ylabel("number of inputs")
plt.show()