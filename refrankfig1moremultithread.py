import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
#multithreading

preci = 2000
length = preci +1

x = np.arange(preci+1)
x = x * (1 / preci)
x = np.vstack((x,x))
x = np.repeat(x,[1,preci],axis=0)
#a normal gradient is created

line = np.zeros(x.shape)
#create a blank plot

r = np.transpose(x)
y = x
#tow gradients used in solving

c = 0.2
tobemapped = line
ax = 1

def mapZeros (tobemapped) :
    for ax in range(0,length):
        pool = ThreadPool()
        pool.map(compare, range(0,length))
        pool.close()
        pool.join()
    return
#function to map solutions of the function

def compare (mtb):
    tester = tobemapped[ax][mtb]
    if tester * tester < 0.00000001 :
        line[ax][mtb]=1


def solve(a):
    equi = a * c * (1-x)
    equi = equi * (1-x) * (2+r)
    equi = equi + (1-y) * (1-c) * a * (1+r)
    equi = equi - c
    return equi
#function of solving the equation

pool = ThreadPool(8)
valuesofa = [1, 0.45, 0.25, 0.15, 0.1]
solutions= pool.map(solve, valuesofa)
pool.close()
pool.join()

for solution in solutions:
    mapZeros(solution)

plt.figure(figsize=(8,7))
plt.scatter(r,y,line)
plt.show()
