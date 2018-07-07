import numpy as np

class board:
    def __init__(self):
        self.bd = np.zeros((6,10),dtype=int)

    def show(self):
        print(self.bd)

    def can_put(self,x,y, mino):
        for (dx, dy) in mino:
            if (self.bd[(x + dx, y + dy)] == 1):
                return False 
        return True

    def put(self, x, y, mino):
        for (dx, dy) in mino:
            self.bd[(x + dx, y + dy)] = 1

def calc():
    minos = [
    [(0,0),(1,0),(2,0),(3,0),(4,0)],
    [(0,0),(1,0),(2,0),(3,0),(3,1)],
    [(0,0),(1,0),(2,0),(2,1),(3,1)],
    [(0,0),(1,0),(2,0),(2,1),(3,0)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0),(2,1),(1,1)],
    [(0,0),(1,0),(2,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(0,1),(3,1)],
    [(0,0),(1,0),(1,1),(1,2),(2,2)],
    [(0,0),(1,0),(1,1),(2,1),(2,2)],
    [(0,0),(1,0),(1,1),(2,1),(1,2)],
    [(1,0),(1,1),(0,1),(1,2),(2,1)]
    ]
