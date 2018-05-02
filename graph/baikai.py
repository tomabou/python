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


    baikai = np.zeros(c)
    #j = 4544
    for j in range(c):
        if not j in id_to_stcd:
            continue
        d = np.zeros(c, dtype=int)
        g = np.zeros(c,dtype=int)
        que = collections.deque()
        que.append(j)
        while len(que) > 0:
            v = que.popleft()
            for nv in edges[v]:
                if d[nv] == 0 and nv != j:
                    d[nv] = d[v] +1
                    que.append(nv)

        g[j] = 1
        que = collections.deque()
        que.append(j)
        while len(que) > 0:
            v = que.popleft()
            for nv in edges[v]:
                if d[nv] == d[v]+1:
                    g[nv] += g[v]
                    que.append(nv)
        
        maxlen = np.max(d)
        depthlist = []
        for i in range(maxlen+1):
            depthlist.append([])
        for i in range(c):
            depthlist[d[i]].append(i)

        for vs in reversed(depthlist):
            for v in vs:
                for nv in edges[v]:
                    if d[nv] == d[v] + 1:
                        baikai[v] += (baikai[nv]) * g[v]/g[nv]

        m = 0
        x = 0
        for i in range(c):
            #if m < d[i]:
            #    m = d[i]
            #    x = i
            m += d[i]
        sname1 = stations[stations["station_cd"] == id_to_stcd[j]].iat[0,2]
        print(sname1,end=" ")
        print(m)

if __name__ == "__main__":
    calc()
        