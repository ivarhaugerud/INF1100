import sys #importing sys

v0 = float(sys.argv[1]) #taking the first value from the command line and making it a float value
t = float(sys.argv[2]) #taking the secound value from the command line and making it a float value
g = 9.81 #defining g

y = v0*t - 0.5*g*t*t #defining the formula for y
print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y)
#made a good looking format for the answer, with a good amount of decimals, in my opinion

"""
python ball_cml.py 3 0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.
"""
