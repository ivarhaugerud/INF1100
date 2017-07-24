import sys
import matplotlib.pyplot as plt
import numpy as np
try:
    v0 = float(sys.argv[1]) # [m/s]
    m = float(sys.argv[2]) # [kg]
except:
    v0 = float(raw_input("v0="))
    m = float(raw_input("m="))
g = 9.81 # [m/s**2]
n = 100 # number of points
t = np.linspace(0.0, 2.0*v0/g, n)

def y(t):
    return v0*t-0.5*g*t*t
def v(t):
    return v0-g*t
def Ek(v, m):
    return 0.5*m*v**2
def Ep(h, m):
    return m*g*h

plt.plot(t, Ek(v(t), m), label="Kinetic Energy")
plt.plot(t, Ep(y(t), m), label="Potential Energy")
plt.plot(t, Ep(y(t), m) + Ek(v(t), m), label="Total Energy")
plt.xlabel("time[s]")
plt.ylabel("height[m]")
plt.legend(loc="best")
plt.show()
