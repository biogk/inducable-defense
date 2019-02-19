import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import cm

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
#Again

c = 0.1

#mu = 2
max2 = 7
max1 = 3
#Initiation

#well...
def f(y):
    ff = 1 - y
    return ff

def df(y):
    dff = -1
    return dff


def mapZeros (tobemapped) :
    for ax in range(0,length):
        for bx in range(0,length):
            tester = tobemapped[ax][bx]
            if tester * tester < 0.0000001 :
                line[ax][bx]=1
    return

def poi(m):
    k = np.arange(0, 40, 1)
    d = []
    i = 0
    for i in k:
        p = pow(math.e,-m)
        p = p * pow(m,i)
        q = p/math.factorial(i)
        d.append(q)
    return d
#d is the pmf
def prob (maxn):
    j = 0
    opt = 0
    for j in range(0,maxn):
        opt = opt + dd[j]
    return opt
#cmf receiving max attack


#Now start the real attack.

preci = 2000
length = preci +1

y = np.arange(preci+1)
y = y / 2000

def derw (ay):
    p1 = prob(max1)
    print("p1=", p1)
    p2 = prob(max2)
    print("p2=", p2)

    print("")

    dw = 1 - ( c * ay )
    dw = dw * df(ay) * ay
    aa = 1 - ( 2 * c * ay )
    dw = dw + ( aa * f(ay))
    dw = dw * p2
    aa = (1 - ay) * df(ay)
    aa = aa - f(ay)
    aa = aa * p1
    dw = dw + aa
    return dw
#My wild calculation

muvalues = [17]

for muv in muvalues:
    dd = poi(muv)
    dws = derw(y)
    plt.plot(y,dws)


plt.axhline(0, color='grey', linestyle='--')

plt.legend(muvalues, loc='upper left')
plt.show()
