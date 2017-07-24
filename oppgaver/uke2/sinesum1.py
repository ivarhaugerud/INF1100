from math import pi
from math import sin

n = 0
i = 0
k = 0
list = []
def S(t, n, T):
    return (4.0/pi)*(1.0/(2.0*i - 1)) * sin(((2.0*(2.0*i) - 1.0)* pi * t)/T)

#while n <= 10.0:
for n in [1, 3, 4, 10, 30, 100]:
    a = S(1.0*10**100, 2.0, 3.0)
    print "for i %.2f the value for S equals %.2f" % (i, a)
    k += a
    i += 1.0
    list.append(a)

print "the sum from zero to ten, equals %.2f" % (k)
