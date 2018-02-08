from methods import *
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

if __name__ =="__main__":
    N = 100
    c = 2
    b = 2*rand(N)-1
    loop = 105
    w = optw(N,c)
    
    result4 = SOR(N,c,b,loop,w)
    result5 = RBSOR(N,c,b,loop,w)
 
    
    matrix = np.empty((0,N))
    for vec in result4:
        vec = np.log10(np.abs(vec))
        matrix = np.vstack((matrix,vec.reshape(1,N)))

    matrix = matrix.T        
    print(matrix.shape)
    sns.heatmap(matrix)
    filename= "matrix_N={}_c={}_w={}_loop={}.png".format(N,c,w,loop)
    plt.savefig(filename, bbox_inches='tight')

    # グラフを表示する
    plt.show()

    