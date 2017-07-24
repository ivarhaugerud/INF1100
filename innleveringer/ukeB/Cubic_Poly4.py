from Parabola import Parabola

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        return self.c3*x**3 + Parabola.__call__(x)

a = Cubic(1, 1, 1, 1)
a(5)

class Quadratic(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        return self.c4*x**4 + Cubic.__call__(x)
