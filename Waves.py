import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(0, 20, 0.1)
y = 4


def g(x, a, y):
    return np.sin((x / y) + a)


def f(x):
    return 0 * x


fig = plt.figure()
ax = plt.axes()
ax.set_ylim(-7, 7)
ax.set_xlabel("Time", fontsize=7)
ax.set_ylabel("Velocity,", fontsize=7)
plt.ion()


left_sine_wave, = plt.plot(x, g(x, 1, 1), "-", label="sin(wt -\u03C6)", color="red")
right_sine_wave, = plt.plot(x, g(x, -1, 1), "-", label="sin(wt -\u03C6)", color="blue")
standing_wave, = plt.plot(x, f(x), "-", label=f"2Asin(kx)-cos(wt)", color="gray")
plt.legend()

for a in np.arange(1, 20, 0.1):
    left_sine_wave.set_ydata(g(x, a, 1.5))
    right_sine_wave.set_ydata(g(x, -a, 1.5))
    standing_wave.set_ydata(f(x))

    fig.canvas.draw()
    plt.pause(0.07)
