import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

def S_derivate(S, I):
    beta = 0.0005
    return -beta*S*I

def I_derivate(S, I):
    beta = 0.0005
    my = 0.1
    return beta*S*I - my*I

def R_derivate(t, I):
    my = 0.1
    return my*I

def test_function(S, I, R):
    expected = 1500
    computed = S + I + R
    epsilon = 10**(-10)
    success = abs(expected - computed) > epsilon
    msg = "At a moment when the program was running there were fewer or more people in the system than it should be. Something went wrong."
    assert success, msg

def spread_disease_accurate(my, beta, dt, N, S0, I0, R0):
    S = np.zeros(N+1)
    I = np.zeros(N+1)
    R = np.zeros(N+1)
    t = np.linspace(0, N*dt, N+1)

    S[0] = S0
    I[0] = I0
    R[0] = R0

    for i in range(N):
        S[i+1] = S[i] - beta*S[i]*I[i]*dt
        I[i+1] = I[i] + beta*S[i]*I[i]*dt - my*I[i]*dt
        R[i+1] = R[i] + my*I[i]*dt
        test_function(S[i], I[i], R[i])

    return S, I, R, t

def plot_SIR(S, I, R, t):
    plt.plot(t, S, label="Susceptibles")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recoverd")
    plt.legend(loc="best")
    plt.title("SIR-graph")
    plt.xlabel("time [days]")
    plt.ylabel("scalar [humans]")
    plt.show()

def returning_arrays(N, dt, S0, I0, R0):
    t = np.linspace(0, N*dt, N+1)
    S = np.zeros(N+1)
    S[0] = S0
    I = np.zeros(N+1)
    I[0] = I0
    R = np.zeros(N+1)
    R[0] = R0
    return S, I, R

class SIR_class():
    def __init__(self, my, dt, beta, N):
        #self.array = np.zeros(N+1)
        self.t = np.linspace(0, N*dt, N+1)
        self.my = my
        self.dt = dt
        self.beta = beta
        self.N = N

    def __call__(self, u, t):
        S, I, R = u
        test_function(S, I, R)
        new_S = -self.beta*S*I
        new_I = self.beta*S*I - self.my*I
        new_R = self.my * I
        return new_S, new_I, new_R

if __name__ == "__main__":
    my = 0.1
    dt = 0.5
    beta = 0.0005
    beta_ = 0.0001
    N = int(60/dt)
    S0 = 1500
    I0 = 1
    R0 = 0
    S, I, R = returning_arrays(120, 0.5, 1500, 1, 0)

    p = SIR_class(my, dt, beta, N)
    solver = RungeKutta4(p)
    solver.set_initial_condition([S0, I0, R0])
    t = np.linspace(0, N*dt, N+1)
    u, t = solver.solve(t)
    S = u[:, 0]
    I = u[:, 1]
    R = u[:, 2]

    plot_SIR(S, I, R, t)

    S, I, R, t = spread_disease_accurate(my, beta, dt, N, 1500, 1, 0)
    plot_SIR(S, I, R, t)

    S, I, R, t = spread_disease_accurate(my, beta_, dt, N, 1500, 1, 0)
    plot_SIR(S, I, R, t)

"""
terminal > python SIR.py


                --- Comment on the task ---
What is the difference between the two graphs when beta is 0.005 compared to
when beta is 0.0001. To understand the different graphs it is important to know
what beta represents. When one infected meet one susceptibles there is a chance
that the susceptible gets infected. Beta represent how many of these encounters
lead to people get infected. When beta is 0.005 it means that 0.5%% of encounters
lead to one person getting sick.
If more people stayd inside it would reduce the mount of encounters, and therefor
amount of new sick people will be reduced. This is what happens when beta is lower.
It therefor makes sence that the graphs look like they do. When fewer people get sick
the whole process moves a lot slower, since there are fewer infected people to spread
the disease it is in a way exponsially slower than it would with a higher betta.
"""
