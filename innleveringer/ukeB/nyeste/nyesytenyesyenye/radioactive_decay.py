import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, log
from ODESolver import ForwardEuler
#importing what I need, including the moduel ODESolver

#a)
class Decay:
    def __init__(self, a):
        self.a = a
    #defining the clas and storeing value in it

    def __call__(self, u, t):
        a = self.a
        return - a * u
    #the call function returns the derivate, that is the right hand side of the equation

#b)
a = log(2)/5600.0 #defining a
U0 = 1.0 #start value for U
aprox = Decay(a) #initializing the instance of the class with a value for a
number_of_points = 20000/500 + 1 #number of points i will use

t_points = np.linspace(0, 20000, number_of_points) #equally spaced t-values

solver = ForwardEuler(aprox)
solver.set_initial_condition(U0)
u, t = solver.solve(t_points)
#using the ODESolver which I imported from above, returns a u and t value in the end

#c)
exact_value = np.zeros(len(t_points)) #empty array
for i in range(number_of_points):
    exact_value[i] = exp(-a*t_points[i])
#computing the exact solution which was given in the task

plt.plot(t, exact_value, "b", label="Exact decay")
plt.plot(t, u, "r", label="Forward Euler aproximation")
plt.plot(t, u, "ro")
plt.ylabel("fraction of particles that remain")
plt.xlabel("time [years]")
plt.legend(loc = "best")
plt.show()
#plotting the graph, it looks close to the exact solution, so the aproximation is sound

print "the difference between the aproximation and the exact value is %g" % (abs(u[-1] - exact_value[-1]))
#print statement for the difference in the last point of the graph
"""
terminal > python radioactive_decay.py
the difference between the aproximation and the exact value is 0.00646097
"""
