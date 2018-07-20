import numpy as np

class board:
    def __init__(self,n):
        self.bd = np.zeros(n*n,dtype = int)
        self.n = n

    def show(self):
        count = 0
        for i in range(self.n):
            print(" "*2 * (self.n-i),end='')
            for j in range(i+1):
                print(self.bd[count], end='   ')
                count += 1
            print("")
            print(" "*2 * (self.n-i),end='')
            if i == self.n - 1:
                break
            for j in range(i+1):
                print(self.bd[count], end='   ')
                count += 1
            print("")
if __name__ == "__main__":
    bd = board(9)
    bd.show()



