import numpy as np
import matplotlib.pyplot as plt
#importing what i need for the task

def fortune(p, q, I, F, n):
    X = np.zeros(n+1)
    C = np.zeros(n+1)
    year_array = np.linspace(0, n+1, n+1)
    #made empty arrays that i can fill later, and then use for the graphing.

    X[0] = F #Desciding the initial values, that will be used for finding the X[1]
    C[0] = p*q*F/(10**4) #The function for the initial amount of money spent the first year, will use this to find the money used in later years

    for i in range(n): #for loop to run through for every year, since i have X[i+1] and C[i+1] i can start the for-loop with a zero
        C[i+1] = C[i] + (I/100.0)*C[i] #the formula A.32 from the book
        X[i+1] = X[i]+p/100.0*X[i]-C[i] #the formula A.31 from the book
    return X, C, year_array

p = 5 #percent interest
q = 90 #how much of the intrest i will spend each year in present
I = 2 #percent inflation
F = 100 #Fortune
n = 35 #Number of years
#chose the variables that i thought fit to the task, I will use these when calling the function

X, C, year_array = fortune(p, q, I, F, n) #calling the function

plt.axis([0, n+1, min(X)-min(X)/10, max(X) + max(X)/100.0]) #i want some room  around the graph
plt.plot(year_array, X, label="Money") #plot the graph with a label
plt.title("money earned over years") #title of graph
plt.xlabel("time [years]") #setting labels
plt.ylabel("money [Million Norwegian kroners]") #setting labels
plt.legend(loc="best") #Choose the best possible place to have the legend-box
plt.show() #showing the graph

"""
terminal >  python fortune_and_infaltion1.py
"""
