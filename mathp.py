import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 600, 1)
y = np.sin(x)

plt.plot(x, y)
plt.draw()
plt.show()