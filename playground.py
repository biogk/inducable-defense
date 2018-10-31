import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
plt.bar(x, height= [0.25,0.5,0.25])
plt.xticks(x, ['AA','Aa','aa']);
plt.show()
