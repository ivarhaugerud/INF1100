import numpy as np  #need this for linspace
import matplotlib.pyplot as plt #need this for ploting a graph
from math import tanh #need this for the formula

#under here defined som variables
g = 9.81 #[m/s**2] gravity
s = 0.079 #[N/m] air-water surface tension
p = 1000 #[kg/m**3] density of water
h = 50 #[m] water depth

def c(A): #defining the formula
    return np.sqrt(((g*A)/(2.*np.pi))*(1.+(s*4.*(np.pi)**2.)/(p*g*A**2.))*np.tanh((2.*np.pi*h)/A)) #returning the formua

A = np.linspace(0.001, 0.1, 100) #the x-values i want
plt.plot(A, c(A), label="velocity for short distance") #ploting the graph
plt.xlabel("wavelength") #name of x-label
plt.ylabel("waterspeed") #name of y-label
plt.axis([0.001, 0.1, min(c(A))-0.1, max(c(A))+0.1]) #how far the axis should go
plt.legend(loc="best")  #locking the box in the best place
plt.show() #showing the graph

#this is the same as above, I did it this was so that i can get each graph up in different windows
#the x-values in each of the graphs are too different, so there is no point in having them
#in the same window toughether, here i only changed the name of the graph and the x-values
B = np.linspace(1, 2000, 1000)
plt.plot(B, c(B), label="velocity long distance")
plt.xlabel("wavelength")
plt.ylabel("waterspeed")
plt.axis([1, 2000, min(c(B)), max(c(B))+1])
plt.legend(loc="best")
plt.show()
"""
terminal > python water_wave_velocity.py 
"""
