import numpy as np
import math
import matplotlib.pyplot as plt

m = 0.75
k = np.arange(0, 20, 1)
d = []
i = 0

for i in k:
    p = pow(math.e,-m)
    p = p * pow(m,i)
    q = p/math.factorial(i)
    d.append(q)

print(d)
print(k)
plt.bar(k, d, width=1)
plt.show()
