import numpy as np #I need numpy for arrays
import matplotlib.pyplot as plt # I need this for plotting a graph

def c_accurate(f): #defining formulas
    return 5*(f-32)/9 #returning the value i need
def c_aprox(f): #defining formula
    return (f-30)/2 #returing the value i need

f_temp = np.linspace(-20, 120, 141) #desciding the farenheit tempratures i want to use

plt.xlabel("temperature[f]") #names on the labels
plt.ylabel("temperature[c]")
plt.axis([-25, 125, min(c_aprox(f_temp))-10, max(c_aprox(f_temp))+10]) #desciding how long each axis should be
plt.plot(f_temp, c_accurate(f_temp), label = "accurate c-value") #ploting and labeling each graph
plt.plot(f_temp, c_aprox(f_temp), label="aprox c-value") #ploting and labeling each graph
plt.legend(loc="best") #places the box the best possible place
plt.show() #shows the graph

"""
terminal > f2c_shortcut_plot.py
"""
