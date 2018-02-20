import numpy as np
from matplotlib import pyplot as plt
import os.path
import numba
import sys
import math

@numba.jit
def Hq(p,q):
    return q#+1*q*q*q
@numba.jit
def Hp(p,q):
    return p

@numba.jit
def Hqt(p,q,t):
    return 0.1*p+1.05*q*q*q - 12*np.cos(0.1+t)

@numba.jit
def reslist(h,T,initial,loopfunc):
    (p,q) = initial
    loop = int(T/(h*1000))

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        for j in range(1000):
            p,q = loopfunc(p,q,h,i*1000+j)
    return (p_res,q_res)
@numba.jit
def err_list(h,T,initial,loopfunc):
    (p,q) = initial
    loop = int(T/h)

    p_res = np.ndarray(loop)
    q_res = np.ndarray(loop)

    for i in range(loop):
        p_res[i] = p
        q_res[i] = q
        p,q = loopfunc(p,q,h)
    tp = np.cos(np.arange(loop)*h)
    tq = np.sin(np.arange(loop)*h)
    ERR = np.sqrt((p_res-tp)*(p_res-tp)+(q_res-tq)*(q_res-tq))
    #ERR = p_res*p_res + q_res*q_res - tp*tp-tq*tq
    return ERR 
    
@numba.jit
def errlog_list(hlist,T,initial,loopfunc):
    errlog = np.arange(len(hlist),dtype="float")
    for num,logh in enumerate(hlist):
        h = (10**logh)
        ERR = err_list(h,T,initial,loopfunc)
        errlog[num] = np.linalg.norm(ERR)/len(ERR)
    return errlog 
@numba.jit
def forward_euler_loop(p,q,h):
    p1 = p + h*(-Hq(p,q))
    q1 = q + h*(Hp(p,q))
    return (p1,q1)
@numba.jit
def backward_euler_loop(p,q,h):
    p1 = (p - h*q)/(1 + h*h)
    q1 = (h*p + q) / (1 + h*h)
    return (p1,q1)

@numba.jit
def symplectic_loop(p,q,h):
    p1 = (p - h*Hq(p,q))
    q1 = (h*p1 + q)
    return (p1,q1)
@numba.jit
def dai_loop(p,q,h):
    p1 = ((1-h*h/4)*p - h*q) / (1 + h*h/4)
    q1 = (h*p + (1-h*h/4)*q) / (1 + h*h/4)
    return (p1,q1)
@numba.jit
def runge_kutta_loop(p,q,h,conter = 0):
    t = h*conter
    kp1 = -Hqt(p,q,t)
    kq1 = p
    kp2 = -Hqt(p+h*kp1/2,q+h*kq1/2,t+h/2)
    kq2 = p + h*kp1/2
    kp3 = -Hqt(p+h*kp2/2,q+h*kq2/2,t+h/2)
    kq3 = p + h*kp2/2
    kp4 = -Hqt(p+h*kp3,q+h*kq3,t+h)
    kq4 = p + h*kp3
    p5 = p + h*(kp1/6 + kp2/3+kp3/3+kp4/6)
    q5 = q + h*(kq1/6 + kq2/3+kq3/3+kq4/6)
    return (p5,q5)



if __name__ =="__main__":
    filename = "def" 

    if sys.argv[1]=="res":
        h = math.pi/500
        time = 100000
        initial = (0,3)
    
        size = 2
        lim = 1.8
    
        plt.figure(figsize=(9,9))
        #plt.xlim(-lim,lim)
        #plt.ylim(-lim,lim)
        #(P,Q) = reslist(h,time,initial,forward_euler_loop)
        #plt.scatter(P,Q,label = "forward_euler",s=size)
        #(P,Q) = reslist(h,time,initial,backward_euler_loop)
        #plt.scatter(P,Q,label = "backward_eular",s = size)
        #(P,Q) = reslist(h,time,initial,symplectic_loop)
        #plt.scatter(P,Q,label = "symplectic", s = size)
        (P,Q) = reslist(h,time,initial,runge_kutta_loop)
        plt.scatter(P,Q,label = "runge_kutta", s=size)
        #(P,Q) = reslist(h,time,initial,runge_kutta_loop)
        #plt.scatter(P,Q,label = "2.828", s=size)
        #h = 2.829
        #(P,Q) = reslist(h,time,initial,runge_kutta_loop)
        #plt.scatter(P,Q,label = "2.829", s=size)
        #(P,Q) = reslist(h,time,initial,dai_loop)
        #plt.scatter(P,Q,label = "dai", s=size)
        for i in range(1000):
            filename= "./image/output_h={}_{}.png".format(h,i)
            if not os.path.exists(filename):
                break
                
    elif sys.argv[1]=="err":
        h = 0.3
        time = 1000
        initial = (1,0)
    
        size = 2
        lim = 1.5
    
        plt.figure(figsize=(9,9))
        ERR = err_list(h,time,initial,forward_euler_loop)
        #plt.plot(range(len(ERR)), ERR,label = "forward_euler")

        ERR = err_list(h,time,initial,backward_euler_loop)
        #plt.plot(range(len(ERR)), ERR,label = "backward_euler")
        ERR = err_list(h,time,initial,symplectic_loop)
        plt.plot(range(len(ERR)), ERR,label = "symplectic")

        ERR = err_list(h,time,initial,dai_loop)
        plt.plot(range(len(ERR)), ERR,label = "dai")
        ERR = err_list(h,time,initial,runge_kutta_loop)
        plt.plot(range(len(ERR)), ERR,label = "runge_kutta")
        for i in range(1000):
            filename= "./image/err_output_h={}_{}.png".format(h,i)
            if not os.path.exists(filename):
                break
    elif sys.argv[1]=="errlog":
        
        time = 10
        initial = (1,0)
    
        size = 2
        lim = 1.5

        hlist = np.arange(-3,-1,0.01)
    
        plt.figure(figsize=(9,9))

        ERR = errlog_list(hlist,time,initial,forward_euler_loop)
        plt.plot(hlist, np.log10(ERR),label = "forward_euler")

        ERR = errlog_list(hlist,time,initial,dai_loop)
        plt.plot(hlist, np.log10(ERR),label = "dai")
        ERR = errlog_list(hlist,time,initial,runge_kutta_loop)
        plt.plot(hlist, np.log10(ERR),label = "rungekuttas")

        #ERR = errlog_list(hlist,time,initial,backward_euler_loop)
        #plt.plot(hlist, np.log10(ERR),label = "backward_euler")
        ERR = errlog_list(hlist,time,initial,symplectic_loop)
        plt.plot(hlist, np.log10(ERR),label = "symplectic")
        plt.xlabel("time step")
        plt.ylabel("error")
        print(ERR)
        for i in range(1000):
            filename= "./image/logerr_{}.png".format(i)
            if not os.path.exists(filename):
                break
    else:
        print("実行時引数足りません")


    plt.legend()

    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    