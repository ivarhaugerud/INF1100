import numpy as np
from SIR import SIR_class, test_function, plot_SIR
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
#importing what I need

class SIRV(SIR_class):
    def __init__(self, my, dt, beta, N, p):
        SIR_class.__init__(self, my, dt, beta, N)
        self.p = p
        #inherting from SIR_class, but now I need a p as well

    def __call__(self, u, t):
        S, I, R, V = u
        new_S = -self.beta*S*I - self.p*S
        new_I = self.beta*S*I - self.my*I
        new_R = self.my * I
        new_V = self.p*S
        return new_S, new_I, new_R, new_V
        #returning 4 vlaues, one of them is not for vaccinated people

def plot4(S, I, R, V, t):
    plt.plot(t, S, label="Susceptibles")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recoverd")
    plt.plot(t, V, label="Vaccinated")
    plt.legend(loc="best")
    plt.title("SIR-graph")
    plt.xlabel("time [days]")
    plt.ylabel("scalar [humans]")
    plt.show()
    #function for plotting

if __name__ == "__main__":
    problem = SIRV(0.1, 0.5, 0.0005, 120, 0.1)
    solver = RungeKutta4(problem)
    solver.set_initial_condition([1500, 1, 0, 0])
    t = np.linspace(0, 60, 121)
    u, t = solver.solve(t)
    #getting the values I need using the class, ODESolver and RungeKutta4

    S = u[:, 0]
    I = u[:, 1]
    R = u[:, 2]
    V = u[:, 3]
    #unpacking the values

    print "When the 10%% of the Susceptible people get a vaccination that works 100%% of the time, the max amount of infected people is %g" %(np.ceil(max(I)))
    plot4(S, I, R, V, t)
    #printstatement and a plot, I need double % to make it work

"""
terminal > python SIRV.py
When the 10% of the Susceptible people get a vaccination that works 100% of the time, the max amount of infected people is 65
"""
