from math import sqrt
#importing what I need

class Rectangle:#Defining the class Rectangle
    def __init__(self, W, H, x0, y0): #This is the nformation I will use for rectangel
        self.W = W
        self.H = H
        self.x0 = x0
        self.y0 = y0

    def area(self): #The formula for area of a rectangel
        return float(self.W*self.H)

    def perimeter(self): #The formula for the perimeter of a rectangel
        return float(2*self.W + 2*self.H)


class Triangle: #Another class, called triangle
    def __init__(self, x0, y0, x1, y1, x2, y2): #The information I will use for a rectangel
        self. x0, self. y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2

    def area(self): #The formula for rectangel, I got the formula from a function I used in the assignment from week three
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        return (0.5*abs(x1*y2 - x2*y1 - x0*y2 + x2*y0 + x0*y1 - x1*y0))

    def perimeter(self): #formula for the periemter, did this by hand. Using pythagoras to make a lot of triangels
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        return sqrt((x1-x0)**2 + (y1-y0)**2) + sqrt((x2-x1)**2 + (y2-y1)**2) + sqrt((x2-x0)**2 + (y2-y1)**2)

def test_Rectangle(): #Test function for triangle
    computed_rectangle = Rectangle(2, 3, 0, 0) #with is 2, height is 3, and the left corner has the cordinates (0, 0)
    computed_area = computed_rectangle.area() #getting the areal
    computed_perimeter = computed_rectangle.perimeter() #getting the perimeter of rectangle
    calculated_area = 6.0 #What I got by hand
    calculated_perimeter = 10.0 #What i got by hand
    tol = 10**(-10) # a small tollerence
    success = abs(computed_area - calculated_area) < tol and abs(computed_perimeter - calculated_perimeter) < tol #both of these must be True for this to be a success
    msg = "something went wrong with the rectangle!" #The message that will get printed if something is wrong
    assert success, msg #calling the two lines above

def test_Triangle(): #The same as above, but for triangle
    computed_triangle = Triangle(0, 0, 6, 0, 3, 4) #The cordinates i chose
    computed_area = computed_triangle.area() #computer area
    computed_perimeter = computed_triangle.perimeter() #computer perimeter
    calculated_area = 12.0 #What i got by hand
    calculated_perimeter = 16.0 #What i also got by hand
    tol = 10**(-10) #a low tolerance
    success = abs(computed_area - calculated_area) < tol and abs(computed_perimeter - calculated_perimeter) < tol #Both have to be true for this to be a success
    msg = "something went wrong with the triangle!" #this will get printed if the line above is not a success
    assert success, msg # calls the two lines above

test_Triangle()
test_Rectangle()
#calling the test-functions

"""
terminal > python geometric_shapes.py
"""
