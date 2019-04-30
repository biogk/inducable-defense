import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import cm

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
#Again

c = 0.2

#mu = 2
max2 = 2
max1 = 1
r0 = 0.9 #default might be changed later
mu0 = 0.2
#Initiation

#well...
def f(z):
    ff = 0.1 * z + 0.9
    return ff

def df(z):
    dff = 0.1
    return dff

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

def derw (ay, r):
    p1 = prob(max1)
    print("p1=", p1)
    p2 = prob(max2)
    print("p2=", p2)

    print("")
    dw = (p2 - p1) * f(ay) * (1 - 2 * c * y)
    dw = dw - c * p1 * f(ay)
    zz = r * (p1 * (1 - y )+p2 * y) * df(y)
    zz = zz * (1 - c * y)
    dw = dw + zz
    return dw
#My wild calculation

rvalues = [0.9, 0.5, 0.1]
muvalues = [0.25,0.2,0.15,0.1]

# examine r
plt.subplots(figsize=(7, 6))
plt.title('dW/dy with varying relatedness, λ=0.2, c=0.2')
plt.xlabel('y')
plt.ylabel('dW/dy')
for r in rvalues:
    dd = poi(mu0)
    dws = derw(y, r)
    plt.plot(y,dws)

plt.legend(rvalues, loc='upper left')
plt.axhline(0, color='grey', linestyle='--')


# examine the distribution parameter
plt.subplots(figsize=(7, 6))
plt.title('dW/dy with varying Poisson parameter, relatedness=0.9, c=0.2')
plt.xlabel('y')
plt.ylabel('dW/dy')
for muv in muvalues:
    dd = poi(muv)
    dws = derw(y, r0)
    plt.plot(y,dws)

plt.legend(muvalues, loc='upper left')
plt.axhline(0, color='grey', linestyle='--')

plt.show()
