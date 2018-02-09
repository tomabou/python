import numpy as np
from matplotlib import pyplot as plt
import os.path

def forward_euler(h,T):
    p = 1
    q = 0  
    p_res = []
    q_res = []

    for i in range(100):
        p_res.append(p)
        q_res.append(q)
        p1 = p + h*(-q)
        q1 = q + h*(p)
        p = p1
        q = q1
    return (p_res,q_res)


if __name__ =="__main__":
    h = 0.1

    (P,Q) = forward_euler(h,10)
    plt.scatter(P,Q)
    for i in range(1000):
        filename= "./image/output_{}.png".format(i)
        if not os.path.exists(filename):
            break

    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    