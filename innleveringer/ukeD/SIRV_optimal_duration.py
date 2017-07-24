import numpy as np
from SIR import SIR_class
from ODESolver import RungeKutta4
import matplotlib.pyplot as plt

def p(t, vt):
    if 6 <= t <= 6 + vt:
        return 0.1
    else:
        return 0

class SIRV2(SIR_class):
    def __init__(self, my, dt, beta, N, p, vt):
        SIR_class.__init__(self, my, dt, beta, N)
        self.vt = vt

        if isinstance(p, (float,int)):
            self.p = lambda t:p
        elif callable(p):
            self.p = p

    def __call__(self, u, t):
        S, I, R, V = u
        new_S = -self.beta*S*I - self.p(t, self.vt)*S
        new_I = self.beta*S*I - self.my*I
        new_R = self.my * I
        new_V = self.p(t, self.vt)*S
        return new_S, new_I, new_R, new_V

if __name__ == "__main__":
    max_infected = np.zeros(32)
    qq = 0
    a = False
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

        max_infected[i] = np.amax(I)

        q = np.amax(I)
        tol = 0.5
        if abs(qq-q) < tol and a == False:
            ii = i
            print "when we have vacinated %d days, from day 6, to day %d, we have the most effective vaccination period" % (i, (i+6))
            a = True

        plt.plot(t, S, label="Susceptibles")
        plt.plot(t, I, label="Infected")
        plt.plot(t, R, label="Recoverd")
        plt.plot(t, V, label="Vaccinated, 6 -> %d" %(6+i))
        plt.legend(loc="best")
        plt.title("SIR-graph")
        plt.xlabel("time [days]")
        plt.ylabel("scalar [humans]")
        #plt.pause(0.25)
        #plt.draw()
        qq = q
    plt.show()

    t_i = np.linspace(0, 32, 32)
    plt.plot(t_i, max_infected, label="amount of maximum infected people")
    plt.xlabel("duration of vaccinationing susceptibles [days]")
    plt.ylabel("max amount of people sick")
    plt.plot(0, np.amax(max_infected), "ro", label="maximum point")
    plt.plot(ii, max_infected[ii], "yo", label="when to stop vaccinating")
    plt.legend(loc="best")
    plt.show()
