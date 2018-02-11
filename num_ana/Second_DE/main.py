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

def backward_euler(h,T):
    p = 1
    q = 0  
    p_res = []
    q_res = []

    for i in range(100):
        p_res.append(p)
        q_res.append(q)
        p1 = (p - h*q)/(1 + h*h)
        q1 = (h*p + q) / (1 + h*h)
        p = p1
        q = q1
    return (p_res,q_res)
def symplectic(h,T):
    p = 1
    q = 0  
    p_res = []
    q_res = []

    for i in range(100):
        p_res.append(p)
        q_res.append(q)
        p1 = (p - h*q)
        q1 = (h*p1 + q)
        p = p1
        q = q1
    return (p_res,q_res)
def dai(h,T):
    p = 1
    q = 0  
    p_res = []
    q_res = []

    for i in range(100):
        p_res.append(p)
        q_res.append(q)
        p1 = ((1-h*h/4)*p - h*q) / (1 + h*h/4)
        q1 = (h*p + (1-h*h/4)*q) / (1 + h*h/4)
        p = p1
        q = q1
    return (p_res,q_res)
def runge_kutta(h,T):
    p = 1
    q = 0  
    p_res = []
    q_res = []

    for i in range(100):
        p_res.append(p)
        q_res.append(q)
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
    h = 0.1 

    (P,Q) = forward_euler(h,10)
    plt.scatter(P,Q,label = "forward_euler")
    (P,Q) = backward_euler(h,10)
    plt.scatter(P,Q,label = "backward_eular")
    (P,Q) = symplectic(h,10)
    plt.scatter(P,Q,label = "symplectic")
    (P,Q) = dai(h,10)
    plt.scatter(P,Q,label = "dai")
    (P,Q) = runge_kutta(h,10)
    plt.scatter(P,Q,label = "runge_kutta")
    for i in range(1000):
        filename= "./image/output_{}.png".format(i)
        if not os.path.exists(filename):
            break

    plt.legend()
    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    