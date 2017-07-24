from Line import Line

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self, x):
        print "Parabola is running"
        return self.c2*x**2 + self.c1*x + self.c0

    def table(self, L, R, n):
        s = ""
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += "%12g %12g \n" %(x, y)
        return s
