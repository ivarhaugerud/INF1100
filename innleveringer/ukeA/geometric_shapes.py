from math import sqrt

class Rectangle:
    def __init__(self, W, H, x0, y0):
        self.W = W
        self.H = H
        self.x0 = x0
        self.y0 = y0

    def area(self):
        return float(self.W*self.H)

    def perimeter(self):
        return float(2*self.W + 2*self.H)


class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self. x0, self. y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2

    def area(self):
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        return ((x1 - x0 * y2 - ((y1-y0)/2.0))/2.0)

    def perimeter(self):
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        return sqrt((x1-x0)**2 + (y1-y0)**2) + sqrt((x2-x1)**2 + (y2-y1)**2) + sqrt((x2-x0)**2 + (y2-y1)**2)

def test_Rectangle():
    computed_rectangle = Rectangle(2, 3, 0, 0)
    computed_area = computed_rectangle.area()
    computed_perimeter = computed_rectangle.perimeter()
    calculated_area = 6.0
    calculated_perimeter = 10.0
    tol = 10**(-10)
    success = abs(computed_area - calculated_area) < tol and abs(computed_perimeter - calculated_perimeter) < tol
    msg = "something went wrong with the rectangle!"
    assert success, msg

def test_Triangle():
    computed_triangle = Triangle(0, 0, 6, 0, 3, 4)
    computed_area = computed_triangle.area()
    computed_perimeter = computed_triangle.perimeter()
    calculated_area = 3.0
    calculated_perimeter = 16.0
    tol = 10**(-10)
    success = abs(computed_area - calculated_area) < tol and abs(computed_perimeter - calculated_perimeter) < tol
    msg = "something went wrong with the triangle!"
    assert success, msg

test_Triangle()
test_Rectangle()

"""
terminal > python geometric_shapes.py
"""
