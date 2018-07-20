import numpy as np
import math
import copy

class board:
    def __init__(self,n):
        self.bd = np.zeros((2*n-1,n),dtype = int)
        self.n = n
        self.label = 1

    def show(self):
        for i in range(self.n):
            print(" "*2 * (self.n-i),end='')
            for j in range(i+1):
                x = self.bd[(2*i,j)]
                if (x // 8) % 2 == 0:
                    print("\033[3{}mA\033[0m".format(x % 8), end='   ')
                if (x // 8) % 2 == 1:
                    print("\033[9{}mA\033[0m".format(x % 8), end='   ')
            print("")
            if i == self.n - 1:
                break
            print(" "*2 * (self.n-i),end='')
            for j in range(i+1):
                x = self.bd[(2*i+1,j)]
                if (x // 8) % 2 == 0:
                    print("\033[3{}mV\033[0m".format(x % 8), end='   ')
                if (x // 8) % 2 == 1:
                    print("\033[9{}mV\033[0m".format(x % 8), end='   ')
            print("")
        
    def smallest_gap(self):
        for i in range(self.n):
            for j in range(i + 1):
                if self.bd[(2 * i, j)] == 0:
                    return (2*i,j)
            if i == self.n - 1:
                break
            for j in range(i + 1):
                if self.bd[(2 * i+1, j)] == 0:
                    return (2*i+1,j)

    def can_put(self, pos, size):
        (a,b) = pos
        if a % 2 == 0:#上向きの三角形
            if (a/2 + size > self.n):
                return False
            for i in range(size):
                for j in range(i + 1):
                    if self.bd[(2 * i+a, j+b)] != 0:
                        return False
                if i == size - 1:
                    break
                for j in range(i + 1):
                    if self.bd[(2 * i+1+a, j+b)] != 0:
                        return False
            return True
        else: #下向きの三角形
            if (b + size > a / 2+1):
                return False
            if (a / 2 + size >= self.n):
                return False
            for i in range(size):
                if self.bd[(a, b + i)] != 0:
                    return False
            for i in range(1, size):
                for j in range(0, size - i):
                    if self.bd[(a - 1 + 2 * i, b + i+j )] != 0:
                        return False
                    if self.bd[(a + 2 * i, b + i+j )] != 0:
                        return False
            return True

    def put(self, pos, size):
        (a,b) = pos
        if a % 2 == 0:#上向きの三角形
            for i in range(size):
                for j in range(i + 1):
                    self.bd[(2 * i+a, j+b)] = bd.label
                if i == size - 1:
                    break
                for j in range(i + 1):
                    self.bd[(2 * i+1+a, j+b)] = bd.label 
        else: #下向きの三角形
            for i in range(size):
                self.bd[(a, b + i)] = bd.label
            for i in range(1, size):
                for j in range(0, size - i):
                    self.bd[(a - 1 + 2 * i, b + j+i  )] = bd.label
                    self.bd[(a + 2 * i, b + j+i )] = bd.label 
        bd.label += 1

    def is_filled(self):
        for i in range(self.n):
            for j in range(i + 1):
                if self.bd[(2 * i, j)] == 0:
                    return False
            if i == self.n - 1:
                break
            for j in range(i + 1):
                if self.bd[(2 * i+1, j)] == 0:
                    return False
        return True



def dfs(bd):
    if bd.is_filled():
        return [bd]
    ans = []
    pos = bd.smallest_gap()
    for size in range(1, bd.n + 1):
        if bd.can_put(pos, size):
            nbd = copy.deepcopy(bd)
            nbd.put(pos,size)    
            ans.extend(dfs(nbd))
    return ans

def dfs_count(bd):
    if bd.is_filled():
        return 1
    ans = 0 
    pos = bd.smallest_gap()
    for size in range(1, bd.n + 1):
        if bd.can_put(pos, size):
            nbd = copy.deepcopy(bd)
            nbd.put(pos,size)    
            ans += dfs_count(nbd)
    return ans

if __name__ == "__main__":
    bd = board(8)
    ans = dfs_count(bd)
    print(ans)