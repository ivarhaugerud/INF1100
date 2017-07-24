from math import pi, exp, sin
#importing what I need

class F: #Creating the class
    def __init__(self, a, w): #and desciding the core values of the self
        self.a = a
        self.w = w

    def __call__(self, x): #This special method gets used if you call F without any ".something" in the end
        a = self.a
        w = self.w
        return exp(-a*x)*sin(w*x) #returns the function

    def __str__(self): #if you just write the function without calling a function within the class, this gets called, in __str__ it must always return a string
        return "exp(-a*x)*sin(w*x)" #will return this as a string

"""
terminal > python
>>> from F2 import F
>>> f = F(a=1.0, w=0.1)
>>> from math import pi
>>> print f(x=pi)
0.013353835137
>>> f.a = 2
>>> print f(pi)
0.00057707154012
>>> print f
exp(-a*x)*sin(w*x)
"""
#this was what I got when I rat it in the terminal
