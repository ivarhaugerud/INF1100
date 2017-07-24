from math import exp

def f(t):
    return exp(-t)

def f_exact(t):
    return -exp(-t)

class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x - 2*h) - 4 * f(x - h) + 3 * f(x))/ (float(2*h))

print "---------------------------------------------------------------------------------------------------------"
print "|      h-value      |   Backward1-value  |   Error Backward1  |     Backward2      |   Error Backward2  |" 
print "---------------------------------------------------------------------------------------------------------"

for k in range(15):
    t = 0
    h = 2**(-k)
    a = Backward1(f, h)
    b = Backward2(f, h)
    print "%20.16f|%20.16f|%20.16f|%20.16f|%20.16f|" % (h, a(0), abs(f_exact(0) - a(0)), b(0), abs(b(0) - f_exact(0)))
print "---------------------------------------------------------------------------------------------------------"
