import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin

m = 30.0
g = 9.81
k = 3.0

n = 100
T = 35.0
t = np.linspace(0, T, n+1)
u = np.zeros(n+1)
u[0] = 0
dt = T/n

"""
def func(u, k):
    return float(g)/m - (k*u**2)/float(m)
"""
def func(u, t):
    return cos(t)

def func2(x):
    return sin(x)

for k in range(n):
    K1 = dt * func(u[k], t[k])
    K2 = dt*func(u[k] + 0.5*K1, t[k]+ 0.5*dt)
    u[k+1] = u[k] + K2


a = abs(u - func2(t))

plt.plot(t, a)
plt.show()
