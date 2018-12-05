import numpy as np
import matplotlib.pyplot as plt
import math

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
#Again

c =0.05
m = 0.75
#mu = 2
maximunAttack = 3
#Initiation

#well...

def newa (m):
    n = 1 - pow(math.e,-m)
    return n



def theConstant(m):
    tc = 0
    for i in range(0,maximunAttack):
        p = pow(math.e,-m)
        p = p * pow(m,i)
        q = p/math.factorial(i)
        tc = tc + q
    return tc


#Now start the real attack.

preci = 2000
length = preci +1

y = np.arange(preci+1)
y = y / 2000

def w (mu):
    print("now attack the undenfenced", newa(mu) )
    w = (1 - y) * (1 - y)
    w = w * newa(mu)
    w = 1 - w
    w = w * (1 - (c * y))
    w = w * theConstant(mu)
    print("now attack the defenced", theConstant(mu))
    return w
#My wild calculation

w1 = w(0.01)
w2 = w(0.05)
w3 = w(0.1)
w4 = w(0.5)
w5 = w(1)
w6 = w(5)

plt.subplot(231)
plt.scatter(y,w1,s=0.1)
plt.title('m = 0.01')

plt.subplot(232)
plt.scatter(y,w2,s=0.1)
plt.title('m = 0.05')

plt.subplot(233)
plt.scatter(y,w3,s=0.1)
plt.title('m = 0.1')

plt.subplot(234)
plt.scatter(y,w4,s=0.1)
plt.title('m = 0.5')

plt.subplot(235)
plt.scatter(y,w5,s=0.1)
plt.title('m = 1')

plt.subplot(236)
plt.scatter(y,w6,s=0.1)
plt.title('m = 5')

#plt.xlim(0, 1)
#lt.ylim(0, 1)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,
                    wspace=0.35)
plt.show()
