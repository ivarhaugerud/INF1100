import numpy as np
from SIZR import plot4zombie
from Night_of_the_Living_Dead import NotLD
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
#importing what I need

def w(t):
    T = [5, 10, 18]
    zum = 0
    sigma = 0.5
    a = 50*alpha
    for i in range(len(T)):
        zum +=  np.exp(-0.5*((t -T[i])/float(sigma))**2)
    return zum*a
#Gauss function, with the variables from the task

if __name__ == "__main__":
    m = 3 #amount of attacks against zombie
    S0 = 50 #start humans
    I0 = 0 #start infected
    Z0 = 3 #start zombies
    R0 = 0 #start removed

    beta = 0.03
    alpha = 0.2*beta
    Sigma = 0
    gammaS = 0
    gamma1 = 0
    p = 1
    T = 20
    n = 200
    #variables from the task

    p = NotLD(gamma1, gammaS, alpha, beta, p, Sigma)
    solver = RungeKutta4(p)
    solver.set_initial_condition([S0, I0, Z0, R0])
    t = np.linspace(0, T, n+1)
    u, t = solver.solve(t)
    #using the class from Night_of_the_Living_Dead.py since the __init__ was good for funtions and not-functions
    S = u[:, 0]
    I = u[:, 1]
    Z = u[:, 2]
    R = u[:, 3]
    #collecting the variables out of u, since u is a 4D array

    plot4zombie(t, S, I, Z, R)
    #plotting the task, formula from task SIZR.py

"""
terminal > python war_on_zombies.py
"""
