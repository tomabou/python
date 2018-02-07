import numpy as np
from methods import *
from numpy.linalg import inv
def mat(c):
    N = 1001
    a = []
    temp = [0 for i in range(N)]
    temp[0] = c
    temp[1]  =-1
    a.append(temp)
    for i in range(1,N-1):
        temp = [0 for i in range(N)]
        temp[i-1] = -1
        temp[i] = c 
        temp[i+1] = -1
        a.append(temp)
    temp = [0 for i in range(N)]
    temp[N-1] = c
    temp[N-2]  =-1
    a.append(temp)
    return a
    
def getD(N,c):
    ans = np.zeros(N*N).reshape(N,N)
    for i in range(N):
        ans[(i,i)] = c
    return ans

def getU(N):
    ans = np.zeros(N*N).reshape(N,N)
    for i in range(N-1):
        ans[(i,i+1)] = -1
    return ans
def RBgetU(N):
    ans = np.zeros(N*N).reshape(N,N)
    n = N//2
    for i in range(n):
        ans[(i,n+i)] = -1
    for i in range(n-1):
        ans[(i,n+i+1)] = -1
    return ans

def getL(N):
    ans = np.zeros(N*N).reshape(N,N)
    for i in range(N-1):
        ans[(i+1,i)] = -1
    return ans
def RBgetL(N):
    ans = np.zeros(N*N).reshape(N,N)
    n = N//2
    for i in range(n):
        ans[(n+i,i)] = -1
    for i in range(n-1):
        ans[(n+i+1,i)] = -1
    return ans

if __name__ == "__main__":
        print(np.linalg.cond(np.array(mat(1.9))))
        N = 10
        c = 2
        w = optw(N,c)-0.05
        print (w)
        I = np.identity(N)
        D = getD(N,c)
        U = getU(N)
        L = getL(N)
        H = inv(I+w *inv(D).dot(L) ).dot((1-w)*I - w *inv(D).dot(U))
        l,P = np.linalg.eig(H)
        np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
        print(H)
        print(np.abs(l))

