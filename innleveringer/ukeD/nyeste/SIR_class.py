import numpy as np
import ODESolver as ODESolver
from ODESolver import RungeKutta4
from SIR import test_function, spread_disease
import matplotlib.pyplot as plt
#importing what I need

def beta(t):
    if t > 12:
        return 0.0001
    else:
        return 0.0005
#function for beta

class ProblemSIR(object):
    def __init__(self, nu, beta, S0, I0, R0, T, N):
        #this is copy paste
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.T = T
        #variables to be saved in the instance of the class

        if isinstance(nu, (float,int)):
            self.nu = lambda t:nu
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float,int)):
            self.beta = lambda t:beta
        elif callable(beta):
            self.beta = beta
    #these two works so that if nu/beta is a function, it will save it to the class as a function
    #if beta/nu is not a function it will save it as a function which only returns one value
    #the reason to do this is that if i for example import this __init__ in a later task it will
    #still work if my beta/nu is not a function but a constant value

    def __call__(self, u, t):
        S, I, R = u
        beta = self.beta
        nu = self.nu
        test_function(S, I, R)
        new_S = -beta(t) *S*I
        new_I = beta(t) * S*I - nu(t)*I
        new_R = nu(t) * I
        return new_S, new_I, new_R
        #returns values which were found using the derivated for each of them

#this below is just copy paste from the book
class SolverSIR(object):
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:, 0], u[:, 1], u[:, 2]

    def plot(self): #standard function for plotting
        S = self.S
        I = self.I
        R = self.R
        t = self.t
        plt.plot(t, S, label="Susceptibles")
        plt.plot(t, I, label="Infected")
        plt.plot(t, R, label="Recoverd")
        plt.legend(loc="best")
        plt.title("SIR-graph")
        plt.xlabel("time [days]")
        plt.ylabel("scalar [humans]")
        plt.show()

if __name__ == "__main__":
    p = ProblemSIR(0.1, beta, 1500, 1, 0, 60, 120) #making an instance of that class
    solver = SolverSIR(p, 0.5) #solving the class p with dt 0.5
    solver.solve() #running the solve, important that this is done before the two things below
    S = solver.S
    I = solver.I
    R = solver.R
    solver.plot() #running the plot
    S_accurate, I_accurate, R_accurate, t_accurate = spread_disease(0.1, 0.0005, 0.5, 120, 1500, 1, 0)
    #imported the accurate one so that I can tell the difference between with and without vaccine
    print "Amount of people infected when beta is %g is %g" % (0.0005, np.ceil(max(I_accurate)))
    print "Amount of people infected when the goverment makes a campaign for washing hands is is %g" % (np.ceil(max(I)))
    print "This means that %d fewer people get infected!" % (abs(np.ceil(max(I_accurate) - np.ceil(max(I)))))
    #print statements

"""
terminal > python SIR_class.py
Amount of people infected when beta is 0.0005 is 932
Amount of people infected when the goverment makes a campaign for washing hands is is 746
This means that 186 fewer people get infected!
"""
