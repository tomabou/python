import numpy as np
import matplotlib.pyplot as plt


def pause_plot():
    fig, ax = plt.subplots(1, 1)

    n = 1000
    dx = 1/n
    dt = 1/n
    c = 0.4

    x = np.arange(n)/n
    u = np.zeros(n)
    for i in range(n):
        if i < n//10:
            u[i + n // 2] = i/n
        elif i < n//10 * 2:
            u[i + n//2] = 0.2 - i/n
    u2 = np.sin(x * 8*np.pi)*0.1
    for i in range(n):
        if i < n * 7//8:
            u2[i] = 0
    #u = u + u2
    lines, = ax.plot(x, u)
    pre_u = u

    k = dt*dt*c/dx/dx
    u_range = max(-u.min(), u.max())
    ax.set_ylim((-u_range, u_range))
    while True:
        for i in range(10):
            u_x = np.convolve([1, -2, 1], u, mode='same')
            u_x[0] = 0
            u_x[-1] = 0
            next_u = 2*u - pre_u + k * u_x
            pre_u = u
            u = next_u

        lines.set_data(x, u)

        ax.set_xlim((x.min(), x.max()))

        plt.pause(0.01)


if __name__ == "__main__":
    pause_plot()
