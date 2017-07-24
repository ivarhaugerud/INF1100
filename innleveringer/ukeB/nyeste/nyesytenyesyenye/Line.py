class Line(): #Defining the class
    def __init__(self, c0, c1): #the main information I need
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

"""
    def __call__(self, x): #if you call the function without any specification this one gets called
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        a = (y1 - y0)/float(x1 - x0)
        b = y0 - a*x0
        return float(a*x + b) #the formula the task referd to
"""
"""
def test_Line(): #made a test function, made one for tuple and one for list to check that both work
    a = [0, 15]
    b = [7, 30]
    c = (32, 10)
    d = (41, 17)
    #descided some random values for x and y
    computed_list = Line(a, b)
    computed_tuple = Line(c, d)
    computed_list_x = computed_list(1)
    computed_tuple_x = computed_tuple(4)
    #the computed values for both the list and the tuple
    expected_list_value = 17.1428571429
    expected_tuple_value = -11.7777777778
    #i got this from the calculations by hand
    tol = 10**(-10) #the tol
    success = abs(computed_list_x - expected_list_value) < tol and abs(computed_tuple_x - expected_tuple_value) < tol
    msg = "wrong" #will get printed if something is wrong
    assert success, msg #asserting

test_Line() #runs the test function

"""
"""
terminal > python Line.py
"""
