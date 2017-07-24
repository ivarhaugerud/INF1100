import numpy as np
import matplotlib.pyplot as plt

R = 1.0 #radius of pipe, meters
B = 0.02 #pressure gradient
u = 0.02 #viscosity
n = 0.1 #viscous properties of the fluid

# a)
def v(r):
    return (B/(2.0*u))**(1.0/n)*(n/(n+1.0))*(R**(1.0+(1.0/n))-r**(1.0+(1.0+n)))
#b)
#ion()
r = 0
y = v(r)
plt.plot(r, y(r))
#values = range(0, 101, 5)
#radius_values = [v(r) for r in values]
x_min = 0
max_y = 15
x_axis = np.linspace(x_min, R, 100)
plt.xlabel("velocity")
plt.ylabel("radius")
plt.title("hella nice graph")
plt.legend(["v(r)"])
plt.axis([x_min, R, 0, max_y])

show()
