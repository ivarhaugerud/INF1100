from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt
#importing what I need

def func(u, t):
    return 1.0/(float(2*(u-1)))
#function for the derivation

def y_exact(x):
    eps = 0.001
    a = 1.0 + sqrt(x + eps)
    return a
#the exact analytical solution

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
#formula from the book for forth degree runge_kutta, since the n value changes i included a call-argument that i will use below

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
    #formula from the book for Eulers method, since the n value has to chamge i include a call-argument that I will use below

z = 1001
t__ = np.linspace(0, 4, z)
y = np.zeros(z)
for i in range(z):
    y[i] = y_exact(t__[i])
#array for the exact value that I will include in the plot

for i in range(10): #i goes from 0 to 10
    plt.clf()#cleareing the figure
    t, u = runge_kutta(i) #calling runge_kutta with the i which changes
    t_, u_ = Eulers(i) #calling euler with i which changes
    plt.plot(t_, u_, label = "Eulers")
    plt.plot(t, u, label = "Runge Kutta")
    plt.plot(t__, y, label = "exact") #ploting the exact
    plt.axis([0, 4, 0, 3.5])
    plt.legend(loc="best")
    plt.pause(1.0)
    plt.draw()
plt.show()

"""
terminal > python yx_ODE_FE_vs_RK4.py
"""
