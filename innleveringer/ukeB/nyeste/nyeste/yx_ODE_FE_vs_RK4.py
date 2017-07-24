from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt

def func(u, t):
    return 1.0/(float(2*(u-1)))

def y_exact(x):
    eps = 0.001
    a = 1.0 + sqrt(x + eps)
    return a

def runge_kutta(i):
    n = 4*2**i
    eps = 0.001
    u = np.zeros(n+1)
    t = np.linspace(0, 4, n+1)
    dt = t[1] - t[0]
    u[0] = 1.0 + sqrt(eps)
    for k in range(n):
        K1 = dt * func(u[k], t[k])
        K2 = dt * func(u[k] + 0.5*K1, t[k] + 0.5*dt)
        K3 = dt * func(u[k] + 0.5*K2, t[k] + 0.5*dt)
        K4 = dt* func(u[k] + K3, t[k] + dt)
        u[k+1] = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
    return t, u

def Eulers(i):
    n = 4*2**i
    eps = 0.001
    u_ = np.zeros(n+1)
    t_ = np.linspace(0, 4, n+1)
    dt = t_[1] - t_[0]
    u_[0] = 1.0 + sqrt(eps)
    for k in range(n):
        u_[k+1] = u_[k] + dt * func(u[k], t[k])
    return t_, u_

z = 1001
t__ = np.linspace(0, 4, z)
y = np.zeros(z)
for i in range(z):
    y[i] = y_exact(t__[i])

for i in range(10):
    plt.clf()
    t, u = runge_kutta(i)
    t_, u_ = Eulers(i)
    plt.plot(t, u, label = "Runge Kutta")
    if i < 6:
        plt.plot(t, u, "bo")
        plt.plot(t_, u_, "ro")
    plt.plot(t, y_exact(t), label = "exact")
    plt.axis([0, 4, 0, 3.5])
    plt.plot(t_, u_, label = "Eulers")
    plt.legend(loc="best")
    plt.pause(0.01)
    plt.draw()
plt.show()
