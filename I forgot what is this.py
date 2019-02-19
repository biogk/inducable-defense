import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

c = 0.25

def f(x):
    result = 1-x
    return result

x = np.arange(0,1001) * 0.001
x = np.vstack((x,x))
x = np.repeat(x,[1,1000],axis=0)
#greating a normal gradient

z = np.transpose(x)
y = x
#create a y and z gradient

w = (1-y) * (1-z) * c
w = f(w)
w = w * (1 - y * 0.2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(z, y, w)

Axes3D.plot_surface(ax, z, y, w, cmap=cm.coolwarm)
plt.show()
