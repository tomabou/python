import numpy as np
from matplotlib import pyplot as plt
import os.path
import numba

@numba.jit
def Hq(p,q):
    return 0.1*q+1*q*q*q
@numba.jit
def Hp(p,q):
    return p

@numba.jit
def Hqt(p,q,t):
    return 0.1 * q+1*q*q*q #+ 12*np.cos(t)

@numba.jit
def forward_euler(h,T,initial):
    (p,q) = initial
    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = p + h*(-Hq(p,q))
        q1 = q + h*(Hp(p,q))
        p = p1
        q = q1
    return (p_res,q_res)

@numba.jit
def backward_euler(h,T,initial):
    (p,q) = initial

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
def symplectic(h,T,initial):
    (p,q) = initial

    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p1 = (p - h*Hq(p,q))
        q1 = (h*p1 + q)
        p = p1
        q = q1
    return (p_res,q_res)
@numba.jit
def dai(h,T,initial):
    (p,q) = initial

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
def runge_kutta(h,T,inital):
    (p,q) = inital
    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        t = h*i
        p1 = -Hqt(p,q,t)
        q1 = p
        p2 = -Hqt(p,q+h*q1/2,t)
        q2 = p + h*p1/2
        p3 = -Hqt(p,q+h*q2/2,t)
        q3 = p + h*p2/2
        p4 = -Hqt(p,q+h*q3,t)
        q4 = p + h*p3
        p = p + h*(p1/6 + p2/3+p3/3+p4/6)
        q = q + h*(q1/6 + q2/3+q3/3+q4/6)
    return (p_res,q_res)
if __name__ =="__main__":
    h = 0.3
    time = 1000
    initial = (1,0)

    size = 2
    lim = 1.5


    plt.figure(figsize=(9,9))
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    #(P,Q) = forward_euler(h,time,initial)
    #plt.scatter(P,Q,label = "forward_euler",s=size)
    #(P,Q) = backward_euler(h,time,initial)
    #plt.scatter(P,Q,label = "backward_eular",s = size)
    (P,Q) = symplectic(h,time,initial)
    plt.scatter(P,Q,label = "symplectic", s = size)
    #(P,Q) = dai(h,time,initial)
    #plt.scatter(P,Q,label = "dai", s=size)
    (P,Q) = runge_kutta(h,time,initial)
    plt.scatter(P,Q,label = "runge_kutta", s=size)
    for i in range(1000):
        filename= "./image/output_h={}_{}.png".format(h,i)
        if not os.path.exists(filename):
            break

    plt.legend()

    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    