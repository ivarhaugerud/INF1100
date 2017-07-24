import numpy as np
from SIR import SIR_class
from ODESolver import RungeKutta4
from SIRV import plot4
#importing what i need

def p(t):
    if 6 <= t <= 15:
        return 0.1
    else:
        return 0
#function for vacination

class SIRV_vary(SIR_class):
    def __init__(self, my, dt, beta, N, p):
        SIR_class.__init__(self, my, dt, beta, N) #inherit from SIR_class __init__, and add one for p

        if isinstance(p, (float,int)):
            self.p = lambda t:p
        elif callable(p):
            self.p = p

    def __call__(self, u, t):
        S, I, R, V = u
        new_S = -self.beta*S*I - self.p(t)*S
        new_I = self.beta*S*I - self.my*I
        new_R = self.my * I
        new_V = self.p(t)*S
        return new_S, new_I, new_R, new_V
        #now with one more, V. sthe other is the same as the earlier ones

if __name__ == "__main__":
    problem = SIRV_vary(0.1, 0.5, 0.0005, 120, p)
    solver = RungeKutta4(problem)
    solver.set_initial_condition([1500, 1, 0, 0])
    t = np.linspace(0, 60, 121)
    u, t = solver.solve(t)
    #using the class in RungeKutta from ODESolver

    S = u[:, 0]
    I = u[:, 1]
    R = u[:, 2]
    V = u[:, 3]
    #unpacking the 4D array
    plot4(S, I, R, V, t)
    #ploting the graph from SIRV.py

"""
terminal > python SIRV_varying_p.py
"""
