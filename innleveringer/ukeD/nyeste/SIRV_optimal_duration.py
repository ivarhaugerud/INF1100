import numpy as np
from SIR import SIR_class
from ODESolver import RungeKutta4
import matplotlib.pyplot as plt
#importing what I need

def p(t, vt):
    if 6 <= t <= 6 + vt:
        return 0.1
    else:
        return 0
#function for p

class SIRV2(SIR_class):
    def __init__(self, my, dt, beta, N, p, vt):
        SIR_class.__init__(self, my, dt, beta, N)
        self.vt = vt

        if isinstance(p, (float,int)):
            self.p = lambda t:p
        elif callable(p):
            self.p = p
        #using the __init__ from SIR_class

    def __call__(self, u, t):
        S, I, R, V = u
        new_S = -self.beta*S*I - self.p(t, self.vt)*S
        new_I = self.beta*S*I - self.my*I
        new_R = self.my * I
        new_V = self.p(t, self.vt)*S
        return new_S, new_I, new_R, new_V
        #for finding each value

if __name__ == "__main__":
    max_infected = np.zeros(32) #empty array for max_infected depending on vaccination time
    qq = 0 #has to be something for the first run
    a = False #so the if-test below wont run

    for i in range(32):
        plt.clf()
        problem = SIRV2(0.1, 0.5, 0.0005, 120, p, i)
        solver = RungeKutta4(problem)
        solver.set_initial_condition([1500, 1, 0, 0])
        t = np.linspace(0, 60, 121)
        u, t = solver.solve(t)
        S = u[:, 0]
        I = u[:, 1]
        R = u[:, 2]
        V = u[:, 3]
        #collecting the values using RungeKutta in ODESolver

        max_infected[i] = np.amax(I)
        #an array wich contains the max amount of people sick for different timeperiods of vaccination
        q = np.amax(I) #storing in a variable
        tol = 0.5 #tolerence
        if abs(qq-q) < tol and a == False: #will only continue if both are correct
            ii = i #storing this for later
            print "when we have vacinated %d days, from day 6, to day %d, we have the most effective vaccination period" % (i, (i+6))
            a = True #so that it will only run one time

        plt.plot(t, S, label="Susceptibles")
        plt.plot(t, I, label="Infected")
        plt.plot(t, R, label="Recoverd")
        plt.plot(t, V, label="Vaccinated, day 6 to %d" %(6+i))
        plt.legend(loc="best")
        plt.title("SIR-graph")
        plt.xlabel("time [days]")
        plt.ylabel("scalar [humans]")
        plt.pause(0.25)
        plt.draw()
        #plotting as a gif

        qq = q #storing this for the next run trough the for-loop, use this for the difference between amount of sick now and the previous loop
    plt.show() #still shows the function when the gif is over

    t_i = np.linspace(0, 31, 32)#array for the time
    plt.plot(t_i, max_infected, label="maximum infected people")
    plt.xlabel("duration of vaccinationing susceptibles from day 6 and outwards[days]")
    plt.ylabel("max amount of people infected")
    plt.plot(0, np.amax(max_infected), "ro", label="maximum point")
    plt.plot(ii, max_infected[ii], "yo", label="when to stop vaccinating")
    plt.legend(loc="best")
    plt.axis([0, 31, 300, 900])
    plt.show()
    #graph over max infected amount for different vaccination lengths

"""
terminal > python SIRV_optimal_duration.py
/home/ivar/.local/lib/python2.7/site-packages/matplotlib/backend_bases.py:2437: MatplotlibDeprecationWarning: Using default event loop until function specific to this GUI is implemented
  warnings.warn(str, mplDeprecation)
when we have vacinated 9 days, from day 6, to day 15, we have the most effective vaccination period
"""
#only the bottom line is my text, the other is an error message, would be nice to have feedback on why it pops up
