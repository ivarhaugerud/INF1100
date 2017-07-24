import numpy as np
def h(x):
    return 1/(np.sqrt(2*np.pi))*np.exp(-0.5*x**2)

x_values = np.linspace(-4, 4, 41)
y_values = h(x_values)

print "----------------------"
print "x-values  |   y-values"
print "----------------------"
for i in x_values:
    print "%5.2f     |    %5.2f" % (i, h(i))
print "----------------------"
