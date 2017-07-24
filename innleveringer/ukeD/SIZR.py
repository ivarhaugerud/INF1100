import numpy as np
from ODESolver import RungeKutta4
import matplotlib.pyplot as plt

class SIZR_class():
    def __init__(self, alpha, sigma, gamma1, gammaS, p, beta, n):
        self.t = np.linspace(0, T, n+1)
        self. alpha, self.sigma, self.gamma1, self.gammaS, self.p, self.beta, self.T = alpha, sigma, gamma1, gammaS, p, beta,T

    def __call__(self, u, t):
        S, I, Z, R = u
        new_S = self.sigma -self.beta*S*I - self.gammaS*S
        new_I = self.beta*S*Z - self.p*I - self.gamma1*I
        new_Z = self.p*I - self.alpha*S*Z
        new_R = self.gammaS*S + self.gamma1*I + self.alpha*Z
        return new_S, new_I, new_Z, new_R


def plot4zombie(t, S, I, Z, R):
    plt.plot(t, S, label="Susceptibles")
    plt.plot(t, I, label="Infected")
    plt.plot(t, Z, label="Zombies")
    plt.plot(t, R, label="Removed")
    plt.xlabel("time [hours]")
    plt.ylabel("scalar [humans]")
    plt.title("zombie-graph")
    plt.legend(loc="best")
    plt.show()

n = 240
alpha = 0.0016#chance that a human kills a zmobie
sigma = 2.0 #number of new people
gammaS = 0.014#chance that a susceptible human dies
gamma1 = 0.014#chance that an infected human dies
p = 1#chance that an human zombie turns into a zombie
beta = 0.0012 #chance of human turning zombie
T = 24 #time in hours
S0 = 10
I0 = 0
Z0 = 100
R0 = 0

p = SIZR_class(alpha, sigma, gamma1, gammaS, p, beta, n)
solver = RungeKutta4(p)
solver.set_initial_condition([S0, I0, Z0, R0])
t = np.linspace(0, T, n+1)
u, t = solver.solve(t)
S = u[:, 0]
I = u[:, 1]
Z = u[:, 2]
R = u[:, 3]

plot4zombie(t, S, I, Z, R)
