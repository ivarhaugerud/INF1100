import numpy as np
from SIZR import plot4zombie
from ODESolver import RungeKutta4
#importing what I need

class NotLD():
    def __init__(self, gamma1, gammaS, alpha, beta, p, sigma):
        if isinstance(gamma1, (float,int)):
            self.gamma1 = lambda t:gamma1
        elif callable(gamma1):
            self.gamma1 = gamma1

        if isinstance(gammaS, (float,int)):
            self.gammaS = lambda t:gammaS
        elif callable(gammaS):
            self.gammaS = gammaS

        if isinstance(alpha, (float,int)):
            self.alpha = lambda t:alpha
        elif callable(alpha):
            self.alpha = alpha

        if isinstance(beta, (float,int)):
            self.beta = lambda t:beta
        elif callable(beta):
            self.beta = beta

        if isinstance(sigma, (float,int)):
            self.sigma = lambda t:sigma
        elif callable(sigma):
            self.sigma = sigma

        if isinstance(p, (float,int)):
            self.p = lambda t:p
        elif callable(p):
            self.p = p
    #took a long time, but made this thing for every variable. I need it because some of the variables depends on what time it is
    #so now, if i import this in a next task and some of the variables are not functions, the __init__ will still work

    def __call__(self, u, t):
        S, I, Z, R = u
        new_S = self.sigma(t) -self.beta(t)*S*I - self.gammaS(t)*S
        new_I = self.beta(t)*S*Z - self.p(t)*I - self.gamma1(t)*I
        new_Z = self.p(t)*I - self.alpha(t)*S*Z
        new_R = self.gammaS(t)*S + self.gamma1(t)*I + self.alpha(t)*Z
        return new_S, new_I, new_Z, new_R
    #call function which returns 4 values, which is the derivated of each of the different type of stages a human can be in

def gamma1(t):
    if t < 5:
        return 0
    elif 29 > t > 4:
        return 0.014
    else:
        return 0

def gammaS(t):
    if t < 29:
        return 0
    else:
        return 0.0067

def alpha(t):
    if t < 5:
        return 0
    elif 29 > t > 4:
        return 0.0016
    else:
        return 0.006

def beta(t):
    if t < 5:
        return 0.03
    elif 29 > t > 4:
        return 0.0012
    else:
        return 0

def p(t):
    return 1

def sigma(t):
    if t < 5:
        return 20
    elif 29 > t > 4:
        return 2
    else:
        return 0
#made all these functions, taken from the task

if __name__ == "__main__": #this wont run when I import something later
    S0 = 60
    I0 = 0
    Z0 = 1
    R0 = 0
    T = 50 #I know this is too much, but I wanted to see how the fighting went, but idealy it should say 33 because 4 + 24 + 5 = 33, so my graph is not exact accurate
    #I think this graph looks really good, and exciting to watch
    n = 330
    #desciding variables

    p = NotLD(alpha, gamma1, gammaS, beta, p, sigma)
    solver = RungeKutta4(p)
    solver.set_initial_condition([S0, I0, Z0, R0])
    t = np.linspace(0, T, n+1)
    u, t = solver.solve(t)
    #making a class for my problem and using ODESolvers RungeKutta to find the aproximation

    S = u[:, 0]
    I = u[:, 1]
    Z = u[:, 2]
    R = u[:, 3]
    #unpacking each array

    plot4zombie(t, S, I, Z, R)
    #using the plot function from SIZR.py

"""
terminal > python Night_of_the_Living_Dead.py
"""
