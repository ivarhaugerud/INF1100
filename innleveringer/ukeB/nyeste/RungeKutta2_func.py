import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi

def runge_kutta(f, U0, T, n, i, a):
    dt = float(T)/(n+i-a)
    t = np.linspace(0, T, n+1)
    u = np.zeros(n+1)
    u[0] = U0

    exact_func = np.zeros(n+1)
    for d in range(n+1):
        exact_func[d] = sin(t[d])

    def func(u, t):
        return cos(t)

    for k in range(n):
        K1 = dt * func(u[k], t[k])
        K2 = dt*func(u[k] + 0.5*K1, t[k]+ 0.5*dt)
        u[k+1] = u[k] + K2
    return t, u, exact_func, dt

a = 55
for i in range(a):
    t, u, exact_func, dt = runge_kutta(0, 0, 10.0, 100, i, a)
    #plt.clf()
    plt.plot(t, u, label="RungeKutta [dt=%g]" %dt)
    plt.axis([0, 3*pi, -2.6, 2.6])
    plt.plot(t, exact_func, label="original function [sin(t)]")
    plt.xlabel("t")
    plt.ylabel("y")
    #plt.legend(loc="best")
    plt.pause(0.005)
    plt.draw()
plt.show()
