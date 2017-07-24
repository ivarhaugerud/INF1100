from math import factorial
import numpy as np
import matplotlib.pyplot as plt
#importing what I need to do this task

#a)
def S(x, n): #defining the formula
  z = 0 #the sum starts at zero
  for j in range(n+1): #a for-loop to sum up the function below, n+1 times
    z += (((-1)**j)*(x**(2*j+1)))/float((factorial(2*j+1))) #the function from the task, I have to use float un the factorial because the number would be too large to preresent as an integer when n = 12
  return z #returning the finished summed up sum

#b)

x_ary = np.linspace(0, 4*np.pi, 314) #empty array for the x-values

plt.plot(x_ary, S(x_ary, 1), label="n = 1")
plt.plot(x_ary, S(x_ary, 2), label="n = 2")
plt.plot(x_ary, S(x_ary, 3), label="n = 3")
plt.plot(x_ary, S(x_ary, 6), label="n = 6")
plt.plot(x_ary, S(x_ary, 12), label="n = 12") #above is all the functions with different n-values
plt.plot(x_ary, np.sin(x_ary), label="sin(x)") #the original sin(x) function
plt.axis([0, np.pi*4, -1.5, 1.5]) #Desciding what the axis should be, if i would have skipped this it would zoom out way too far so we could not actually see the graphs for the y-value around -1.5 to 1.5
plt.legend(loc="best") #the box should be in the best possible spot
plt.show() #showing the graph

"""
terminal > python plot_Taylor_sin.py
"""
