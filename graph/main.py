import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numba import jit

@jit
def warshall(d,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(d[i][j] > d[i][k] + d[k][j]):
                    d[i][j] = d[i][k] + d[k][j]
    return d

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

    for i in range(n):
        if lines["e_status"][i] != 0:
            for j in range(n):
                has_edge[i][j] = 0
                has_edge[j][i] = 0
    
    d = np.copy(has_edge)

    for i in range(n):
        for j in range(n):
            if d[i][j] == 0:
                d[i][j] = 999

    d = warshall(d,n)
    
    m = 0
    start = 0
    end =0
    for i in range(n):
        for j in range(n):
            if d[i][j] != 999 and d[i][j] >m:
                start = i
                end = j
                m = d[i][j]
            if i == j:
                d[i][j] = 0
    np.savetxt("output/d.csv",d,delimiter=',',fmt="%.0f")
    print(m)

    for i in range(n):
        for j in range(n):
            if d[i][j] == 26:
                print(lines["line_name"][i],end=' ')
                print(lines["line_name"][j])

    cur = start
    while cur != end:
        print(lines["line_name"][cur])
        for i in range(n):
            if cur != i and has_edge[cur][i] == 1 and d[cur][end] == d[i][end] + 1:
                cur = i
                break

    print(lines["line_name"][end])
    

    for i in range(n):
        for j in range(n):
            if d[i][j] == 999:
                d[i][j] = -1

    max_r = 999
    center = 0
    for i in range(n):
        if d[i][end] == -1:
            continue
        m  = 0
        for j in range(n):
            if i!=j and d[i][j] != 999:
                m = max(m,d[i][j])
        if max_r > m and m != 999 :
            center = i
            max_r = m
        if m == 13:
            print("center is " + lines["line_name"][i])
            print("radius is {}".format(max_r))



    print("center is " + lines["line_name"][center])
    print("radius is {}".format(max_r))

#    sns.heatmap(has_edge)
#    plt.show()


if __name__ == "__main__":
    calc()
        