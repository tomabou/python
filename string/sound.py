import cProfile
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import numba


def initialize(n, m):
    Vx = np.zeros((n, m))
    Vy = np.zeros((n, m))
    P = np.zeros((n, m))
    ax = np.zeros((n, m))
    ay = np.zeros((n, m))
    b = np.zeros((n, m))

    return (Vx, Vy, P, ax, ay, b)


# @numba.jit
def calc_NVx(dx, dt, ax, Vx, P):
    # 畳み込みなのでひっくり返ることに注意
    Px = convolve2d([[1], [-1]], P, mode='full') / dx
    Px = Px[1:, ]  # 最初のほうがいらないはず
    NVx = -Px + (1/dt - ax/2)*Vx
    return NVx / (1/dt + ax/2)


# @numba.jit
def calc_NVy(dy, dt, ay, Vy, P):
    # 畳み込みなのでひっくり返ることに注意
    Px = convolve2d([[1, -1]], P, mode='full') / dy
    Px = Px[:, 1:]  # 最初のほうがいらないはず
    NVx = -Px + (1/dt - ay/2)*Vy
    return NVx / (1/dt + ay/2)


# @numba.jit
def calc_NP(dx, dy, dt, Vx, Vy, P, b, k):
    Vxx = convolve2d([[1], [-1]], Vx, mode='full') * k / dx
    Vxx = Vxx[:-1, :]
    Vyy = convolve2d([[1, -1]], Vy, mode='full') * k / dy
    Vyy = Vyy[:, :-1]
    NP = -Vxx - Vyy + (1/dt - b/2)*P
    return NP/(1/dt + b/2)


class BOUND(object):
    def __init__(self, x, y):
        self.VxB = np.ones((x, y))
        self.VyB = np.ones((x, y))
        self.PB = np.ones((x, y))

        for i in range(x):
            self.VxB[i][0] = 0
            self.VxB[i][0] = 0
        for i in range(y):
            self.VyB[x-1][i] = 0
            self.VyB[x-1][i] = 0

        for i in range(x//3, 2 * x//3):
            for j in range(4):
                self.VyB[i][y//2+j] = 0
                self.VxB[i][y//2+j] = 0
                self.PB[i][y//2+j] = 0

    def __call__(self, Vx, Vy, P):
        return (self.VxB * Vx, self.VyB * Vy, self.PB * P)


def leapfrog(dx, dy, dt, ax, ay, b, Vx, Vy, P, k, bound):
    NVx = calc_NVx(dx, dt, ax, Vx, P)
    NVy = calc_NVy(dy, dt, ay, Vy, P)
    NP = calc_NP(dx, dy, dt, NVx, NVy, P, b, k)
    NVx, NVy, NP = bound(NVx, NVy, NP)
    return NVx, NVy, NP


def test():
    np.set_printoptions(precision=3, suppress=True)
    Vx, Vy, P, ax, ay, b = initialize(10, 10)
    P[5, 5] = 1
    dx = 0.1
    dy = 0.1
    dt = 0.1
    k = 0.1
    for i in range(10):
        print(P)

        Vx, Vy, P = leapfrog(dx, dy, dt, ax, ay, b, Vx, Vy, P, k, bound)


def draw_test():
    np.set_printoptions(precision=3, suppress=True)
    Vx, Vy, P, ax, ay, b = initialize(50, 50)
    bound = BOUND(50, 50)
    for i in range(35, 40):
        for j in range(35, 40):
            P[i, j] = 1
    dx = 0.1
    dy = 0.1
    dt = 0.1
    k = 0.1
    fig = plt.figure()
    ims = []
    for i in range(200):
        print(P)

        Vx, Vy, P = leapfrog(dx, dy, dt, ax, ay, b, Vx, Vy, P, k, bound)
        im = plt.imshow(P, animated=True, vmin=-0.1, vmax=0.2)
        ims.append([im])
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                    repeat_delay=1000)

    #ani.save('anim.mp4', writer="ffmpeg")
    plt.show()


if __name__ == "__main__":
    #pr = cProfile.Profile()
    # pr.enable()
    # test()
    draw_test()
    # pr.disable()
    # pr.print_stats()
    # pr.dump_stats('fib.profile')
