import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

preci = 2000
length = preci +1

x = np.arange(preci+1)
x = x * (1 / preci)
x = np.vstack((x,x))
x = np.repeat(x,[1,preci],axis=0)
#a normal gradient is created

linex = []
liney = []
#create a blank plot

r = np.transpose(x)
y = x
#tow gradients used in solving

c = 0.2
def mapZeros (tobemapped) :
    for ax in range(0,length):
        for bx in range(0,length):
            tester = tobemapped[ax][bx]
            if tester * tester < 0.00000001 :
                linex.extend(ax)
                liney.extend(bx)
    return
#function to map solutions of the function

def solve(a):
    equi = a * c * (1-x)
    equi = equi * (1-x) * (2+r)
    equi = equi + (1-y) * (1-c) * a * (1+r)
    equi = equi - c
    return equi
#function of solving the equation


mapZeros(solve(1))
mapZeros(solve(0.45))
mapZeros(solve(0.25))
mapZeros(solve(0.15))
mapZeros(solve(0.1))

plt.figure(figsize=(8,7))
plt.scatter(r,y,line)
plt.show()
