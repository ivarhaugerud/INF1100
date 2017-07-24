import numpy as np #need this for linspace
import matplotlib.pyplot as plt #need this for graphing
T = 2*np.pi #[Radianer], i assume
#T is a global variable i need trough the task

def S(t, n): #defining a function
    s = 0 #use this so that the sum starts at zero
    for i in range(n): #the list goes from 0 up to n-1, this is ok since on the line below I never write i, I only write (i+1)
        s += 1.0/(2.0*(i+1.0)-1.0)*np.sin((2.0*(2.0*(i+1.0)-1.0)*np.pi*t)/T) #finding the sum, which is dependent on n from above, then I use this in the line below
    return (4/np.pi)*s #the actuall formula I need to return, using the sum from the loop above

n = 314 #will use this a lot in the task
t_verdier = np.linspace(0, 2*np.pi, n) #making an array of t-values which I will use in the graph
t_f_verdier = np.zeros(n) #making an empty arrays with 314 zeros

def f(t): #defining the f(t) formula
    if 0 < t < T/2.0: #3 if's, each of them will return a value, the problem is how to get these values into an array!
        return 1
    elif t == T/2.0:
        return 0
    else:
        return -1

for i in range(n): #to get the values from above into an array
    t_f_verdier[i] = f(t_verdier[i]) #filling the empty array using the formula from above
#plotting each of the graphs, with names, axis and a box at the top
plt.plot(t_verdier, S(t_verdier, 1), label="n=1")
plt.plot(t_verdier, S(t_verdier, 3), label="n=3")
plt.plot(t_verdier, S(t_verdier, 20), label="n=20")
plt.plot(t_verdier, S(t_verdier, 200), label="n=200")
plt.axis([-0.1, 2*np.pi+0.1, -2, 2])
plt.legend(loc="best") #puts it the best possible spot
plt.plot(t_verdier, t_f_verdier) #plotting the f(t) function, looks a bit weird because of line 24 and 25. I have already run it trough the f(t) formula
plt.show()
"""
terminal > python sinesum1_plot.py
"""
