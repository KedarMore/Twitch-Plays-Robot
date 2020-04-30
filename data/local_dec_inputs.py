from sklearn.preprocessing import PolynomialFeatures
import pylab as plot
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.linear_model import LinearRegression

# reader=csv.reader('C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/analysis/myfile.csv')
with open("C:/Users/kedar/OneDrive - UCB-O365/Documents/Thesis/twitch plays/data/final1new.csv") as file:
    reader = csv.reader(file, delimiter="\t")
    rows = list(reader)
players=['']*len(rows)
for i in range(len(rows)):
    players[i]=rows[i][1]

sort = list(dict.fromkeys(players))

noofchats = [0]*len(sort)
for i in range(len(players)):
    temp = sort.index(players[i])
    noofchats[temp] = noofchats[temp]+1

noofchats, sort = zip(*sorted(zip(noofchats,sort)))
sort=sort[::-1]
noofchats = noofchats[::-1]
ax = plt.subplot(111)
ax.get_xaxis().set_ticks(np.linspace(0,290,29))

ax.get_xaxis().set_ticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
# ax.get_xaxis().set_ticklabels(

plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170,
          180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290], noofchats,alpha=0.5)
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170,
          180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290], noofchats,'bo',alpha=0.5)
leg=ax.legend()
leg.set_title('1 '+sort[0]+'\n2 '+sort[1]+'\n3 ' +sort[2]+
            '\n4 '+sort[3]+'\n5 '+sort[4]+'\n6 '+sort[5]+
            '\n7 '+sort[6]+'\n8 '+sort[7]+'\n9 '+sort[8]+
            '\n10 '+sort[9]+
           '\n11 '+sort[10]+'\n12 '+sort[11]+'\n13 '+sort[12]+
           '\n14 '+sort[13]+'\n15 '+sort[14]+'\n16 '+sort[15]+
           '\n17 '+sort[16]+'\n18 '+sort[17]+'\n19 '+sort[18] +
           '\n20 '+sort[19]+'\n21 '+sort[20]+'\n22 '+sort[21] +
           '\n23 '+sort[22]+'\n24 '+sort[23]+'\n25 '+sort[24] +
              '\n26 '+sort[25]+'\n27 '+sort[26]+'\n28 '+sort[27]+'\n29 '+sort[28], prop={'size': 8.4})
plt.title("Number of Inputs from each Player")
plt.xlabel("players")
plt.ylabel("number of inputs")
# circle1=patches.Ellipse([20,290],50,70,color='green',alpha=0.1)
# circle2=patches.Ellipse([250,0],100,70,color='red',alpha=0.1)
# ax.add_artist(circle1)
# ax.add_artist(circle2)

X = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170,
     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
X = X.reshape(-1, 1)

lin = LinearRegression()
lin.fit(X, noofchats)


poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(X)

poly.fit(X_poly, noofchats)
lin2 = LinearRegression()
lin2.fit(X_poly, noofchats)

plt.plot(X, lin2.predict(poly.fit_transform(X)),'r')

plt.show()
