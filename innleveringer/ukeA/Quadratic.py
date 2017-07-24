from cmath import sqrt
import numpy as np

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        a = self.a
        b = self.b
        c = self.c
        return a*x**2 + b*x + c

    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        q = b**2 - 4*a*c

        if q < 0:
            return (-b + sqrt(q)/(2*a), (-b -sqrt(q)/(2*a)))
        if q == 0:
            return (-b + sqrt(q)/(2*a)).real
        else:
            return (-b + sqrt(q)/(2*a)).real, (-b - sqrt(q)/(2*a)).real

    def table(self, L, R, n):
        x_val = np.linspace(L, R, n)
        print "|-------------------|"
        print "| x-value | f-value |"
        print "|-------------------|"
        for i in x_val:
            print "| %7.3f | %7.3f |" % (i, self.value(i))
        print "|-------------------|"

def test_Quadratic():
    computed_quadratic = Quadratic(1, 2, 0)
    computed_value = computed_quadratic.value(5)
    computed_roots = computed_quadratic.roots()
    calculated_value = 35.0
    calculated_roots = (-1.0, -3.0)
    tol = 10**(-12)
    success = abs(computed_value - calculated_value) < tol and computed_roots == calculated_roots
    msg = "wrong"
    assert success, msg
test_Quadratic()
