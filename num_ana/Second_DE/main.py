import numpy as np
from matplotlib import pyplot as plt
import os.path
import numba

@numba.jit
def forward_euler(h,T):
    p = 1
    q = 0  
    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = p + h*(-q)
        q1 = q + h*(p)
        p = p1
        q = q1
    return (p_res,q_res)

@numba.jit
def backward_euler(h,T):
    p = 1
    q = 0  

    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = (p - h*q)/(1 + h*h)
        q1 = (h*p + q) / (1 + h*h)
        p = p1
        q = q1
    return (p_res,q_res)
@numba.jit
def symplectic(h,T):
    p = 1
    q = 0  

    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = (p - h*q)
        q1 = (h*p1 + q)
        p = p1
        q = q1
    return (p_res,q_res)
@numba.jit
def dai(h,T):
    p = 1
    q = 0  

    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = ((1-h*h/4)*p - h*q) / (1 + h*h/4)
        q1 = (h*p + (1-h*h/4)*q) / (1 + h*h/4)
        p = p1
        q = q1
    return (p_res,q_res)
@numba.jit
def runge_kutta(h,T):
    p = 1
    q = 0  

    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = -q
        q1 = p
        p2 = -(q+h*q1/2)
        q2 = p + h*p1/2
        p3 = -(q+h*q2/2)
        q3 = p + h*p2/2
        p4 = -(q+h*q3)
        q4 = p + h*p3
        p = p + h*(p1/6 + p2/3+p3/3+p4/6)
        q = q + h*(q1/6 + q2/3+q3/3+q4/6)
    return (p_res,q_res)
if __name__ =="__main__":
    h = 0.3 
    time = 100000

    size = 1

    plt.figure(figsize=(9,9))
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    #(P,Q) = forward_euler(h,time)
    #plt.scatter(P,Q,label = "forward_euler",s=size)
    #(P,Q) = backward_euler(h,time)
    #plt.scatter(P,Q,label = "backward_eular",s = size)
    #(P,Q) = symplectic(h,time)
    #plt.scatter(P,Q,label = "symplectic", s = size)
    #(P,Q) = dai(h,time)
    #plt.scatter(P,Q,label = "dai", s=size)
    (P,Q) = runge_kutta(h,time)
    plt.scatter(P,Q,label = "runge_kutta", s=size)
    for i in range(1000):
        filename= "./image/output_{}.png".format(i)
        if not os.path.exists(filename):
            break

    plt.legend()

    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    