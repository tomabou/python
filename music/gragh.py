import numpy as np
from matplotlib import pyplot as plt

y = np.random.rand(100)
x = np.arange(100)

plt.plot(x,np.sin(2*np.pi *x/100))
plt.plot(x,np.sin(4*np.pi *x/100))
plt.show()
