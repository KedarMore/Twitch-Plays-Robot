from matplotlib import pyplot as plt
player1 = [31.12,
           41.59,
           63.56,
           73.24,
           76.02
           ]
player2 = [23.09,
           44.09,
           121.29,
           71.38,
           111.49
           ]
player4 = [27.63,
           79.91,
           56.64,
           87.88,
           153.49
           ]
levels=['level 1','level 2','level 3','level 4','level 5']
plt.plot(levels,player1,label="1 player")
plt.plot(levels, player2,label="2 players")
plt.plot(levels, player4, label="4 players")
plt.xlabel("Levels")
plt.ylabel("Time")
plt.title("Total Time Taken")
plt.legend()
plt.show()
