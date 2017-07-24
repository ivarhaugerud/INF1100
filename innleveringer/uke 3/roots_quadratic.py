#a)
# a*x*x + b*x + c = 0
from cmath import sqrt

def roots(a, b, c):
    value1 = (b**2.0) - (4.0*a*c)
    x1 = ((-b + sqrt(value1))/(2.0*a))
    x2 = ((-b - sqrt(value1))/(2.0*a))
    if value1 >= 0.0:
        return float(x1.real), float(x2.real)
    else:
        return complex(x1), complex(x2)

print roots(1, 1, -2)
print roots(1, -2, 5)

def test_roots_float(): 
    print "test_roots_float is running!"
    expected = (1.0, -2.0)
    computed = roots(1, 1, -2)
    success = expected == computed
    if success:
        print "success!"
    else:
        print "fail"
    msg = "expected value was %s computed value was %s" % (expected, computed)
    assert success, msg

def test_roots_complex(): 
    print "test_roots_complex is running!"
    expected = ((1+2j),(1 -2j))
    computed = roots(1, -2, 5)
    success = expected == computed
    if success:
        print "success!"
    else:
        print "fail!"
    msg = "expected value was %s computed value was %s" % (expected, computed)
    assert success, msg

test_roots_float()
test_roots_complex()

"""
terminal > python roots_quadratic.py
(1.0, -2.0)
((1+2j), (1-2j))
test_roots_float is running!
success!
test_roots_complex is running!
success!
"""
