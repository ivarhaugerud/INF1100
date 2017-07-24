import matplotlib.pyplot as plt #need for plotting graph
import numpy as np #need for linspace

def f(x, t): #defining formula
    return np.e**(-(x-3*t)**2)*np.sin(3*np.pi*(x-t)) #returning this

x_values = np.linspace(-4, 4, 81) #all the x-values i need for the plot

plt.xlabel("x-values") #naming the x-axis
plt.ylabel("f(x) values") #naming the y-axis
#plt.axis([-4, 4, min(f(x_values, 0)), max(f(x_values, 0))]) #how far should the axis go?
plt.axis([-4, 4, -1, 1])
plt.plot(x_values, f(x_values, 0), label="f(x, t)") #plotting
plt.legend(loc="best") #placing the box the best place possible
plt.show() # showing the graph
