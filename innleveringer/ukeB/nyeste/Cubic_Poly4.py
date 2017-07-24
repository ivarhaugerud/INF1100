from Parabola import Parabola

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        print "Cubic is running"
        return self.c3 * x**3 + Parabola.__call__(self, x)

a = Cubic(1, 2, 1, 1)
print a.table(0, 5, 6)


class Quadratic(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        "print Quadratic is running"
        return self.c4*x**4 + Cubic.__call__(self, x)

b = Quadratic(1, 2, 1, 1, 0)
print b.table(0, 5, 6)
