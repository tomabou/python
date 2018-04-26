import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numba import jit

@jit
def calc():
    joins = pd.read_csv("data/join.csv")
    companys = pd.read_csv("data/company.csv")
    lines = pd.read_csv("data/line.csv")
    stations = pd.read_csv("data/station.csv")
    
    n = len(lines)
    print(lines["line_cd"][0])
    print(n)

    has_edge = np.zeros((n,n),dtype=int)

    line_cd_to_node = dict()
    for i in range(n):
        line_cd_to_node[lines["line_cd"][i]] = i

    edges = list()
    for i in range(n):
        edges.append([])

    A = dict()

    for i in range(len(stations)):
        
        v = stations["station_g_cd"][i]
        if v in A:
            A[v].append(stations["line_cd"][i])
        else:
            A[v] = [stations["line_cd"][i]]
    
    for xs in A.values():
        for x in xs:
            for y in xs:
                fr = line_cd_to_node[x]
                to = line_cd_to_node[y]
                has_edge[fr][to] = 1
    
    d = has_edge

    for i in range(n):
        for j in range(n):
            if d[i][j] == 0:
                d[i][j] = 999

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(d[i][j] > d[i][k] + d[k][j]):
                    d[i][j] = d[i][k] + d[k][j]
    
    m = 0
    for i in range(n):
        for j in range(n):
            if d[i][j] >m:
                m = d[i][j]
    np.savetxt("output/d.csv",d,delimiter=',',fmt="%.0f")
    
    print("")
    print(m)

    sns.heatmap(has_edge)
    plt.show()


if __name__ == "__main__":
    calc()
        