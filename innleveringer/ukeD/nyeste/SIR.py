import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
#import what I need

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
#these functions I found out were not really needed, but I included them and used them in the function spread_disease_accurate
#that function is basically RungeKutta, I use this function in the next exercise

def test_function(S, I, R):
    expected = 1500
    computed = S + I + R
    epsilon = 10**(-10)
    success = abs(expected - computed) > epsilon
    msg = "At a moment when the program was running there were fewer or more people in the system than it should be. Something went wrong."
    assert success, msg
    #test function, checks that there are no new people in the simulation

def spread_disease(my, beta, dt, N, S0, I0, R0): #I use this later
    S = np.zeros(N+1)
    I = np.zeros(N+1)
    R = np.zeros(N+1)
    t = np.linspace(0, N*dt, N+1)
    #creating arrays

    S[0] = S0
    I[0] = I0
    R[0] = R0
    #desciding start values

    for i in range(N):
        S[i+1] = S[i] - beta*S[i]*I[i]*dt
        I[i+1] = I[i] + beta*S[i]*I[i]*dt - my*I[i]*dt
        R[i+1] = R[i] + my*I[i]*dt
        test_function(S[i], I[i], R[i])
    #for-loop for finding the next value, I also run the test_function for each run trough to check that everything works
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
    #plot function

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
        #call function returning 3 values

if __name__ == "__main__": #this only gets called if i call this task from the terminal, not if if i import it from somewhere else
    my = 0.1
    dt = 0.5
    beta = 0.0005
    beta_ = 0.0001
    N = int(60/dt)
    S0 = 1500
    I0 = 1
    R0 = 0
    #desciding variables and getting some arrays
    def getting_it_all(my, dt, beta, N, S0, I0, R0): #since im doing it twice, I made a function
        p = SIR_class(my, dt, beta, N)
        solver = RungeKutta4(p)
        solver.set_initial_condition([S0, I0, R0])
        t = np.linspace(0, N*dt, N+1)
        u, t = solver.solve(t)
        S = u[:, 0]
        I = u[:, 1]
        R = u[:, 2]
        #unpacking u with the variables I need
        plot_SIR(S, I, R, t) #plotting this S

    getting_it_all(my, dt, beta, N, S0, I0, R0)
    getting_it_all(my, dt, beta_, N, S0, I0, R0) #different beta
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
