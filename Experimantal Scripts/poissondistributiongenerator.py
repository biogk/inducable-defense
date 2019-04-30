import numpy as np
import math
import matplotlib.pyplot as plt

def prob (maxn):
    j = 0
    opt = 0
    for j in range(0,maxn):
        opt = opt + d[j]
    return opt

m = 1
k = np.arange(0, 20, 1)
d = []
i = 0

for i in k:
    p = pow(math.e,-m)
    p = p * pow(m,i)
    q = p/math.factorial(i)
    d.append(q)

v = prob(1)
print(d)
print(k)
print(v)
plt.bar(k, d, width=1)
plt.show()
