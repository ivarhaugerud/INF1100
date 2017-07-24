import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, log
from ODESolver import ForwardEuler

#a)
class Decay:
    def __init__(self, a):
        self.a = a

    def __call__(self, u, t):
        a = self.a
        return - a * u

#b)
a = log(2)/5600.0
U0 = 1.0
aprox = Decay(a)
number_of_points = 20000/500 + 1

t_points = np.linspace(0, 20000, number_of_points)

solver = ForwardEuler(aprox)
solver.set_initial_condition(U0)
u, t = solver.solve(t_points)

#c)
exact_value = np.zeros(len(t_points))
for i in range(number_of_points):
    exact_value[i] = exp(-a*t_points[i])

plt.plot(t, exact_value, "b", label="Exact decay")
plt.plot(t, u, "r", label="Forward Euler aproximation")
plt.plot(t, u, "ro")
plt.ylabel("fraction of particles that remain")
plt.xlabel("time [years]")
plt.legend(loc = "best")
plt.show()

print "the difference between the aproximation and the exact value is %g" % (abs(u[-1] - exact_value[-1]))
