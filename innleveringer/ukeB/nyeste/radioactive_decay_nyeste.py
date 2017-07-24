import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, log
from ForwardEuler_func import ForwardEuler

"""task a"""
class Decay:
  def __init__(self, a, U0, T, n):
    self.a = a
    self.U0 = U0
    self.T = T
    self.n = n

  def __call__(self):
    a = self.a
    U0 = self.U0
    T = self.T
    n = self.n
    u, t = ForwardEuler(U0, T, n)
    return u, t

""" task b """

a = log(2)/5600.0
b = Decay(a, 1, 20000, 40)
u, t = b()

def f(t, u):
    return -a*u

""" task c """
T = np.linspace(0, 20000, 20000/500.0)

exact_value = np.zeros(40)
for i in range(40):
    exact_value[i] = exp(-a*T[i])

plt.plot(T, exact_value, "b", label="Exact decay")
plt.plot(t, u, "r", label="Forward Euler aproximation")
plt.plot(t, u, "ro")
plt.ylabel("fraction of particles that remain")
plt.xlabel("time [years]")
plt.legend(loc = "best")
plt.show()
