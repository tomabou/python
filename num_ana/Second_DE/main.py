import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os.path

if __name__ =="__main__":
    matrix = np.random.rand(20,20)
    print(matrix.shape)
    sns.heatmap(matrix)
    for i in range(1000):
        filename= "./image/output_{}.png".format(i)
        print(filename)
        print(os.path.exists(filename))
        if not os.path.exists(filename):
            break

    plt.savefig(filename, bbox_inches='tight')

    plt.show()

    