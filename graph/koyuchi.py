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
            if not x2 in edges[x1]:
                edges[x1].append(x2)
                edges[x2].append(x1)

    eigen = np.ones(c)
    for p in range(600):
        new = np.zeros(c)
        for i in range(c):
            for v in edges[i]:
                new[v]+=eigen[i]
        new = new / np.linalg.norm(new)
        #print(np.linalg.norm(eigen-new))
        if np.linalg.norm(eigen - new) < 0.000001:
            break
        eigen = new      

    for i in range(c):
        if not i in id_to_stcd:
            continue
        if True:
            sname1 = stations[stations["station_cd"] == id_to_stcd[i]].iat[0,2]
            print(sname1,end=' ')
            #print(stations[stations["station_cd"]==id_to_stcd[i]])
            print(eigen[i])

if __name__ == "__main__":
    calc()
        