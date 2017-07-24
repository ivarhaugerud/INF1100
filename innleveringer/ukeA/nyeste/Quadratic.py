from cmath import sqrt
import numpy as np
#importing what I need

class Quadratic: #Defining the class
    def __init__(self, a, b, c): #The information I will use troughout the task, that i need
        self.a = a
        self.b = b
        self.c = c

    def value(self, x): #Simpel formula which returns the value f(x) in a given point
        a = self.a
        b = self.b
        c = self.c
        return a*x**2 + b*x + c

    def roots(self): #Finds the root, it also works for complex numbers, two real roots, and when there is only one root
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

    def table(self, L, R, n): #making a nice formatted table
        x_val = np.linspace(L, R, n)
        print "|-------------------|"
        print "| x-value | f-value |"
        print "|-------------------|"
        for i in x_val:
            print "| %7.3f | %7.3f |" % (i, self.value(i)) #using the formula from above for finding the f-value
        print "|-------------------|"

def test_Quadratic(): #making the test
    computed_quadratic = Quadratic(1, 2, 0) #calling the class
    computed_value = computed_quadratic.value(5) #computer value
    computed_roots = computed_quadratic.roots() #computer roots
    calculated_value = 35.0 #hand made values
    calculated_roots = (-1.0, -3.0) #hand made roots
    tol = 10**(-12) #the tolerance
    success = abs(computed_value - calculated_value) < tol and computed_roots == calculated_roots #both have to be True for it to be a success
    msg = "wrong" #message will pop up if the Success fails
    assert success, msg #asserting

if __name__ == "__main__": #this only runs if it is called in the terminal, so if I run a py.check or want to import the function it wont print the things below
    test_Quadratic()

"""
python > terminal Quadratic.py
"""
