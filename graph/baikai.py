import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numba import jit
import collections


#@jit
def calc():
    joins = pd.read_csv("data/join.csv")
    companys = pd.read_csv("data/company.csv")
    lines = pd.read_csv("data/line.csv")
    stations = pd.read_csv("data/station.csv")

    stgcd_to_id = dict()
    c = 0
    for i in range(len(stations)):
        x = stations["station_g_cd"][i]
        if not x in stgcd_to_id:
            stgcd_to_id[x] = c
            c += 1

    stcd_to_id = dict()
    id_to_stcd = dict()
    for i in range(len(stations)):
        if stations["e_status"][i] != 0:
            continue
        x = stations["station_cd"][i]
        g = stations["station_g_cd"][i]
        stcd_to_id[x] = stgcd_to_id[g]
        id_to_stcd[stcd_to_id[x]] = x

    edges = []
    for i in range(c):
        edges.append([])
    
    for i in range(len(joins)):
        cd1 = joins["station_cd1"][i]
        cd2 = joins["station_cd2"][i]
        if cd1 in stcd_to_id and cd2 in stcd_to_id:
            x1 = stcd_to_id[cd1]
            x2 = stcd_to_id[cd2]
            edges[x1].append(x2)
            edges[x2].append(x1)

    c = 10
    edges=[]
    for i in range(10):
        edges.append([])
    for i in range(8):
        edges[i].append(i+1)
        edges[i+1].append(i)
    edges[3].append(4)
    edges[4].append(3)
        

    baikai = np.zeros(c)
    #j = 4544
    for j in range(c):
#        if not j in id_to_stcd:
#            continue
        d = np.zeros(c, dtype=int)
        que = collections.deque()
        que.append(j)
        while len(que) > 0:
            v = que.popleft()
            for nv in edges[v]:
                if d[nv] == 0 and nv != j:
                    d[nv] = d[v] +1
                    que.append(nv)

        print("d   ",end='')
        for i in range(c):
            print(d[i],end = ' ')
        print("")


        g = np.zeros(c,dtype=int)
        used = np.zeros(c,dtype = int)
        g[j] = 1
        used[j]=1
        que = collections.deque()
        que.append(j)
        while len(que) > 0:
            v = que.popleft()
            for nv in edges[v]:
                if d[nv] == d[v]+1:
                    g[nv] += g[v]
                if used[nv]==0:
                    que.append(nv)
                    used[nv] = 1
                    
        print("g   ",end='')
        for i in range(c):
            print(g[i],end = ' ')
        print("")
        
        maxlen = np.max(d)
        depthlist = []
        for i in range(maxlen+1):
            depthlist.append([])
        for i in range(c):
            if d[i] > 0:
                depthlist[d[i]].append(i)
        
        for i in range(len(depthlist)):
            print("{} is".format(i),end=' ')
            for v in depthlist[i]:
                print(v,end=' ')
            print("")
        print("\n")

        new_baikai = np.zeros(c)
        for vs in reversed(depthlist):
            for v in vs:
                for nv in edges[v]:
                    if d[nv] == d[v] + 1:
                        new_baikai[v] += (new_baikai[nv] + 1) * g[v]/g[nv]
        
        baikai += new_baikai

    for i in range(c):
        print(baikai[i])

    m = 0
    x = 0
    for i in range(c):
        if m < baikai[i]:
            m = baikai[i]
            x = i
    #sname1 = stations[stations["station_cd"] == id_to_stcd[x]].iat[0,2]
    #print(sname1,end=" ")

if __name__ == "__main__":
    calc()
        