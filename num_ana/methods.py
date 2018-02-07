from math import sqrt,log,floor,cos,pi
import numpy as np
from numpy.random import rand
from matplotlib import pyplot
from numpy.linalg import norm
"""N must be even number!!!"""

def residual(v,c,b):
    return log( norm(np.convolve(v,np.array([-1,c,-1]),"same")-b,np.inf)/norm(b,np.inf),10)

def optw(N,c):
    return 2 / (1 + sqrt(1-((2/c)*cos(pi /(N+1)))**2))


"""CG method"""
def CG_method(N,c,b,loop):
    convv = np.array([-1,c,-1])
    result = []
    x = np.zeros(N)
    r = b - np.convolve(x,convv,"same")
    p = r
    for k in range(loop):
        Ap = np.convolve(p,convv,"same")
        a = np.dot(r,r)/np.dot(p,Ap)
        Nx = x + a*p
        Nr = r - a*np.convolve(p,convv,"same")
        beta = np.dot(Nr,Nr)/np.dot(r,r)
        Np = Nr + beta*p
    
        result.append(residual(Nx,c,b))
    
        x = Nx
        r = Nr
        p = Np
    return result
    

"""Jacobi method"""
def Jacobi(N,c,b,loop):
    result2 = []
    x = np.zeros(N)
    conv = np.array([-1,0,-1])
    for k in range(loop):
        x = (b-np.convolve(x,conv,"same"))/c
        result2.append(residual(x,c,b))
    return result2

"""Gauss-Seidel"""
def Gauss_Seidel(N,c,b,loop):
    result3 = []
    
    x = np.zeros(N)
    for k in range(loop):
        x[0] = (x[1]+b[0])/c
        for i in range(1,N-1):
            x[i] = (x[i-1]+x[i+1]+b[i])/c
        x[N-1] = (x[N-2]+b[N-1])/c
        
        result3.append(residual(x,c,b))
    return result3
    
    
"""SOR"""
def SOR(N,c,b,loop,w):
    result4 = []
    x = np.zeros(N)
    for k in range(loop):
        y = (x[1]+b[0])/c
        x[0] = x[0] + w*(y-x[0])
        for i in range(1,N-1):
            y = (x[i-1]+x[i+1]+b[i])/c
            x[i] = x[i] + w*(y-x[i])
        y = (x[N-2]+b[N-1])/c
        x[N-1] = x[N-1] + w*(y-x[N-1])
        
        result4.append(residual(x,c,b))
        #result4.append(np.convolve(x,[-1,c,-1],"same") - b)
    return result4

"""RBSOR"""
convE = np.array([0,-1,-1])
convO = np.array([-1,-1,0])
def EOresidual(E,O,bE,bO,c,b):
    x =  norm(c*E + np.convolve(O,convE,"same") - bE,np.inf)
    y =  norm(c*O + np.convolve(E,convO,"same") - bO,np.inf)
    return log(max(x,y)/norm(b,np.inf),10)
def RBSOR(N,c,b,loop,w):
    result5 = []
    bO = np.array([b[i*2+1] for i in range(N//2)])
    bE = np.array([b[i*2] for i in range(N//2)])

    even = np.zeros(N//2)
    odd = np.zeros(N//2)
    
    for k in range(loop):
        odd  = odd  + w*((bO - np.convolve(even,convO,"same"))/c - odd )
        even = even + w*((bE - np.convolve(odd, convE,"same"))/c - even)
    
        vec = np.vstack((c*even+np.convolve( odd,convE,"same")-bE
                        ,c*odd +np.convolve(even,convO,"same")-bO))
        #result5.append(vec)
        result5.append(EOresidual(even,odd,bE,bO,c,b))
    return result5

if __name__=="__main__":
    N = 100
    c = 20
    b = 2*rand(N)-1
    loop = 20
    w = optw(N,c)
    
    result = CG_method(N,c,b,loop)
    result2 =Jacobi(N,c,b,loop)
    result3 = Gauss_Seidel(N,c,b,loop)
    result4 = SOR(N,c,b,loop,w)
    result5 = RBSOR(N,c,b,loop,w)
 
    pyplot.xlabel('loop')
    pyplot.ylabel('residual norm')
    pyplot.title('N = {} c = {} w = {}'.format(N,c,w))
    #pyplot.plot(range(loop),result,label = "CG")
    #pyplot.plot(range(loop),result2,label = "Jacobi")
    #pyplot.plot(range(loop),result3,label = "Gauss-Seidel")
    pyplot.plot(range(loop),result4,label = "SOR")
    pyplot.plot(range(loop),result5,label = "RBSOR")

    spec = 10
    pyplot.plot(range(spec),log((w-1),10)*np.array(range(spec)),label = "SOR Spectral radius")

    huku = w/c
    #pyplot.plot(range(min(N,loop)),log(huku,10)*np.array(range(min(loop,N))),label = "huku")
    
#    wopt = w
#    for i in range(10):
#        w = i/1000.0 + wopt
#        result5 =[]
#        RBSOR()
#        pyplot.plot(range(loop),result5,label = "RBSOR w={}".format(w))
#
    pyplot.legend()
   # pyplot.ylim([-20,2])
    
    filename= "N={}_c={}.png".format(N,c)
    pyplot.savefig(filename, bbox_inches='tight')
    pyplot.show()

