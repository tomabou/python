from methods import *
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

if __name__=="__main__":
    N = 100
    c = 2.3
    b = 2*rand(N)-1
    loop = 25
    w = optw(N,c)
    

    
    wopt = w
    ws = np.arange(1,2,step=0.001)
    ans =[]
    ans2 =[]
    for w in ws:
        result5 =[]
        result5 = SOR(N,c,b,loop,w)
        A = np.array([range(loop-10),np.ones(loop-10)])
        A = A.T
        a,sd = np.linalg.lstsq(A,result5[10:])[0]
        ans.append(10 ** a)
        #pyplot.plot(range(loop),result5,label = "RBSOR w={}".format(w))
    for w in ws:
        result5 =[]
        result5 = RBSOR(N,c,b,loop,w)
        A = np.array([range(loop-10),np.ones(loop-10)])
        A = A.T
        a,sd = np.linalg.lstsq(A,result5[10:])[0]
        ans2.append(10 ** a)
    r = 2/c *  cos(pi/(N+1))

    plt.xlabel("w")
    plt.ylabel("convergence speed")

    b = ws*ws*r*r/2-ws+1
    y = b + np.sqrt(b*b-(ws-1)*(ws-1))
    plt.plot(ws,ws-1, label = "w-1")
    plt.plot(ws,y)
    plt.plot(ws,ws/c,label = "w/c")
    plt.plot(ws,ans,label = "SOR real speed")
    plt.plot(ws,ans2,label = "RBSOR real speed")
    plt.legend()
    
    filename= "RBchangew_N={}_c={}.png".format(N,c)
    pyplot.savefig(filename, bbox_inches='tight')
    pyplot.show()
