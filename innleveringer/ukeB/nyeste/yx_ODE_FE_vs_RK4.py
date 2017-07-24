from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt


def func(y, t):
    return 1/float(2*(y-1))


def y_exact(x):
    eps = 0.001
    a = 1.0 + sqrt(x + eps)
    return a


def runge_kutta(n, b):
    T = 4
    eps = 0.001
    dt = 4.0/(2.0**b)

    t = np.linspace(0, T, n+1)
    u = np.zeros(n+1)
    u[0] = 1 + sqrt(eps)

    for k in range(n):
        K1 = dt * func(u[k], t[k])
        K2 = dt * func(u[k] + 0.5*K1, t[k] + 0.5*dt)
        K3 = dt * func(u[k] + 0.5*K2, t[k] + 0.5*dt)
        K4 = dt* func(u[k] + K3, t[k] + dt)
       # u[k+1] = u[k] + (dt/12.0) * 23*func(u[k], t[k]) - 16*func(u[k-1], t[k-1]) + 5*func(u[k-2], t[k-2])
        u[k+1] = u[k] + (1/6.0)*(K1 + K2 + K3 + K4)
    return t, u

def Eulers(n, b):
    T = 4
    eps = 0.001
    dt = float(T)/2**b
    t_ = np.linspace(0, 4, n+1)
    u_ = np.zeros(n+1)
    u_[0] = 1 + sqrt(eps)
    for k in range(n):
        u_[k+1] = u_[k] + dt * func(u[k], t[k])
        t_[k+1] = t[k] + dt
    return t_, u_
"""
y = np.zeros(1001)
for i in range(1001):
    y[i] = y_exact(t[i])
"""

for i in range(11):
    plt.clf()
    t, u = runge_kutta(1000, i)
    t_, u_ = Eulers(1000, i)
    plt.plot(t, u, label = "Runge Kutta")
    plt.plot(t, y_exact(t), label = "exact")
    plt.axis([0, 4, 0, 4])
    plt.plot(t_, u_, label = "Eulers")
    plt.legend(loc="best")
    plt.pause(0.1)
    plt.draw()
plt.show()
"""
t, u = runge_kutta(1000, 20)
t_, u_ = Eulers(1000, 20)

y = np.zeros(1001)
for i in range(1001):
    y[i] = y_exact(t[i])

plt.plot(t, u)
plt.plot(t, y, label="real graph")
plt.plot(t_, u_)
plt.legend(loc="best")
plt.show()

diff = 10**(-11)
i = 1
while diff < 10**(-10):
    t, y =  runge_kutta(0, 4, 100, i)
    i += 1
    diff = abs(y - y(t))

"""
