class Line():
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print "Line is running"
        return self.c0 * self.c1 * x

    def table(self, L, R, n):
        s = ""
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += "%12g %12g \n" %(x, y)
        return s
#I could also write "from Line import Line", but since I was unsure weather or not this was easier for devilry, I included the code
#Included a print statement in the call function

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
#The class Parabola from the book, included it in this file, same reason as line 17
#Included printstatements in the call function

class Cubic(Parabola): #Inhereting from Parabola, which is inhereting from line
    def __init__(self, c0, c1, c2, c3): #this is the information I need
        Parabola.__init__(self, c0, c1, c2) #the code which was in parabola
        self.c3 = c3 #the new information which was not in parabola

    def __call__(self, x): #when Cubic gets called
        print "Cubic is running" #print statements
        return self.c3 * x**3 + Parabola.__call__(self, x) #returns the value of c3 multiplied by x**3 and add it to the sum from parabola

class Quadratic(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        "print Quadratic is running"
        return self.c4*x**4 + Cubic.__call__(self, x)
#basically all the hastags for this class is the same as the hastags for Cubic, so i wont att them

b = Quadratic(1, 2, 1, 1, 3) #Descided some values
print b(4) #test the call function
print b.table(0, 5, 6) #tests the table function

"""
terminal > python Cubic_Poly4.py
Cubic is running
Parabola is running
857
Cubic is running
Parabola is running
Cubic is running
Parabola is running
Cubic is running
Parabola is running
Cubic is running
Parabola is running
Cubic is running
Parabola is running
Cubic is running
Parabola is running
           0            1
           1            8
           2           65
           3          286
           4          857
           5         2036
"""
