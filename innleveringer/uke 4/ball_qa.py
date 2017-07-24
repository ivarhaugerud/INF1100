v0 = float(raw_input("v0=")) #asking the user for input
g = 9.81 #defining gravity
t = float(raw_input("t=")) #asking the user for more input

y = v0*t - 0.5*g*t*t # defining the formula
print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y) #a good looking printing statement

"""
terminal > python ball_qa.py
v0=3
t=0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.
"""
