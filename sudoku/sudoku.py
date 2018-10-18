import numpy as np
import random
import math
import numba 
import matplotlib.pyplot as plt

prob1 = [
    [0,8,6,0,0,0,1,0,9],
    [0,1,0,4,9,0,7,0,0],
    [0,0,0,0,1,2,0,0,0],
    [3,0,0,0,0,9,0,1,0],
    [0,0,4,0,0,0,2,0,0],
    [0,2,0,7,0,0,0,0,3],
    [0,0,0,9,3,0,0,0,0],
    [0,0,7,0,5,1,0,2,0],
    [8,0,1,0,0,0,4,9,0]
]
prob2 = [
    [1,2,3,4,5,6,7,8,9],
    [4,5,6,7,8,9,1,2,3],
    [7,8,9,1,2,3,4,5,6],
    [2,3,4,5,6,7,8,9,1],
    [5,6,7,8,9,1,2,3,4],
    [8,9,1,2,3,4,5,6,7],
    [3,4,5,6,7,8,9,1,2],
    [6,7,8,9,1,2,3,4,5],
    [9,1,2,3,4,5,6,7,8]
]

prob3 = [
    [0,1,0,0,0,0,0,6,0],
    [6,3,9,0,0,0,0,4,0],
    [0,0,5,0,9,0,7,0,0],
    [0,0,2,0,5,9,0,0,0],
    [0,0,1,0,0,0,6,0,0],
    [0,0,0,1,3,0,8,0,0],
    [0,0,6,0,8,0,9,0,0],
    [0,4,0,0,0,0,2,7,3],
    [0,7,0,0,0,0,0,8,0]
]

prob4 = [
    [0,0,5,3,0,0,0,0,0],
    [8,0,0,0,0,0,0,2,0],
    [0,7,0,0,1,0,5,0,0],
    [4,0,0,0,0,5,3,0,0],
    [0,1,0,0,7,0,0,0,6],
    [0,0,3,2,0,0,0,8,0],
    [0,6,0,5,0,0,0,0,9],
    [0,0,4,0,0,0,0,3,0],
    [0,0,0,0,0,9,7,0,0]
]

class sudoku:
    def __init__(self,prob):
        self.board = np.ndarray((9,9),int)
        for i in range(9):
            for j in range(9):
                self.board[(i,j)] = prob[i][j]

        self.ans = self.board.copy()
        for i in range(9):
            for j in range(9):
                if self.ans[(i, j)] == 0:
                    self.ans[(i,j)] = random.randint(1,9)

        self.E = -243 
        for i in range(9):
            for j in range(9):
                x = (i//3) * 3
                y = (j//3) * 3
                for dx in range(3):
                    for dy in range(3):
                        if self.ans[(i, j)] == self.ans[(x + dx, y + dy)]:
                            self.E += 1
                for k in range(9):
                    if self.ans[(i, j)] == self.ans[(i, k)]:
                        self.E += 1
                    if self.ans[(i, j)] == self.ans[(k, j)]:
                        self.E += 1

    def show(self):
        print("E = {}".format(self.E))
        print(self.ans)
    
    def rand_change(self, b):
        i = random.randint(0,8)
        j = random.randint(0,8)
        while self.board[(i, j)] != 0:
            i = random.randint(0,8)
            j = random.randint(0,8)

        v = self.ans[(i,j)]
        self.ans[(i,j)] = 0 #自分自身と等しいということをなくすため
        nv = random.randint(1,9)
        newE = self.E

        x = (i//3) * 3
        y = (j//3) * 3
        for dx in range(3):
            for dy in range(3):
                if v == self.ans[(x + dx, y + dy)]:
                    newE -= 2
                if nv == self.ans[(x + dx, y + dy)]:
                    newE += 2
        for k in range(9):
            if v == self.ans[(i, k)]:
                newE -= 2
            if nv == self.ans[(i, k)]:
                newE += 2
            if v == self.ans[(k,j)]:
                newE -= 2
            if nv == self.ans[(k,j)]:
                newE += 2

        if newE < self.E:
            self.E = newE
            self.ans[(i, j)] = nv
            return 
        elif newE > self.E:
# a b があったとして、a<b
# a -> b が1なら
# b -> a x    a + b(1-x) = b
# x = a/b
# ここで、exp(-Eb) に従うようにしたいので,
# x = exp(-(Ea - Eb) b)
            p = random.random()
            if p < math.exp(-(newE - self.E) * b):
                self.E = newE
                self.ans[(i,j)] = nv
                return 
        self.ans[(i,j)] = v

y = sudoku(prob4)
print(y.board)

xs = []
ys = []
for i in range(1, 50000000):
    #1.3 ~ 1.5ぐらいで煮詰めたtら解けた
    b = 1.3 +  0.00000001 * i
    y.rand_change(b)
    if y.E == 0:
        break
    if i % 10000 == 0:
        print(y.E)
        print(b)
        xs.append(b)
        print(y.ans)
        ys.append(y.E)

plt.scatter(xs,ys)
plt.show()
y.show()



