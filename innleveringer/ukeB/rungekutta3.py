import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi

n = 100
T = 3*pi
t = np.linspace(0, T, n+1)
u = np.zeros(n+1)
u[0] = 0
dt = float(T)/n

def func(u, t):
    return cos(t)

b = np.zeros(n+1)
for i in range(n+1):
    b[i] = sin(t[i])

def runge_kutta(i):
    dt = (float(i)/30.0)*float(T)/n
    for k in range(n):
        K1 = dt * func(u[k], t[k])
        K2 = dt*func(u[k] + 0.5*K1, t[k]+ 0.5*dt)
        u[k+1] = u[k] + K2
    return u

for i in range(31):
    u = runge_kutta(i)
    plt.clf()
    plt.plot(t, u, label="RungeKutta")
    plt.axis([0, 3*pi, -1.1, 1.1])
    plt.plot(t, b, label="original function [cos(t)]")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend(loc="best")
    plt.pause(0.010)
    plt.draw()
plt.show()

numerical_difference = (b - u)
plt.plot(t, numerical_difference)
plt.show()
