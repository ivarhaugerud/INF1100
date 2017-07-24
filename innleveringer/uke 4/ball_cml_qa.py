import sys #importing sys to be able to have user input
g = 9.81  #defining gravity
try: #writing a try-function, which the program should tro to execute
    v0 = float(sys.argv[1]) #getting the first value you write in
    t = float(sys.argv[2]) #getting the secound value you write in
    y = v0*t - 0.5*g*t*t    #defining the formula for height
    print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y) # a good looking print of the answer i get, if the try function is correct
    sys.exit(1) #quitting the program
except IndexError: #if there was an index error I want my program to tell the user what is wrong, and not use the standard terminal error message, and give the user the option to define the values again
    print "There is an index error!" #to tell the user what went wrong
    v0 = float(raw_input("v0=")) #to give the user a new chance to write in the values
    t = float(raw_input("t=")) #to give the user a new chance to write in the values
    y = v0*t - 0.5*g*t*t #defining the formula
    print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y) #good looking print with decimals
    # no need to write sys.exit, since this is the last line of the program anyway

""" terminal >>> python ball_cml_qa.py 3 0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.

eller med IndexError:

terminal > python ball_cml_qa.py
There is an index error!
v0=3
t=0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.
"""
