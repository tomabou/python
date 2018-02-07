import numpy as np
from methods import *
from matplotlib import pyplot as plt


if __name__ =="__main__":
    N = 100
    c = 2.3
    
    w = np.arange(1.2,1.6,step=0.001)
    r = 2/c *  cos(pi/(N+1))

    b = w*w*r*r/2-w+1
    y = b + np.sqrt(b*b-(w-1)*(w-1))
    plt.plot(w,w-1)
    plt.plot(w,y)
    plt.plot(w,w/c)
    plt.show()
