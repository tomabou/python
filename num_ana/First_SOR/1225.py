import numpy as np
from math import sqrt
from matplotlib import pyplot


def size(a):
  sum = 0
  for x in a:
    sum += x*x
  return sqrt(sum)

e = 2 
a = [[1+e,0,0],[0,e,-1],[0,3,e]]
b = [[1,0,0],[0,0,-1],[0,3,0]]
a = np.array(a)

x = np.ones(3)

ansa = []
ansb = []
ansc = []
roop = 30
for i in range(roop):
  ansa.append(x[0])
  ansb.append(x[1])
  ansc.append(x[2])
  x = np.dot(a,x)
  x = x/size(x)
  

pyplot.plot(range(roop),ansa,label="a")
pyplot.plot(range(roop),ansb,label="b")
pyplot.plot(range(roop),ansc,label="c")

pyplot.legend()

pyplot.show()

