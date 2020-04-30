import matplotlib.pyplot as plt
import math

n=53
q=0.765
Td = 0.15
Lambda=0.1
x=1
# x=1
y=1

N=range(1,30)
totaltime=[0]*len(N)

t0 = (1/y)*n*(1+(N[0]*x)*Lambda*Td)/((N[0]*x)*Lambda*(2*q*math.exp(-Lambda*(((N[0]*x)-1)*Td))-1))
for i in range(len(N)):
    totaltime[i]=(1/y)*n*(1+(N[i]*x)*Lambda*Td)/((N[i]*x)*Lambda*(2*q*math.exp(-Lambda*(((N[i]*x)-1)*Td))-1))
    totaltime[i]=totaltime[i]*65/t0

plt.xlabel("Number of Players")
plt.ylabel("Total Time")
plt.title("Expected total time")
plt.plot(N, totaltime)
plt.show()
