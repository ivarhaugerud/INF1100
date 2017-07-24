import sys #importing sys
g = 9.81 #defining gravity
try: #make the program try this, if there is an error it will skip to the except longer down
    v0 = float(sys.argv[1]) #taking the first value written
    t = float(sys.argv[2]) #taking the secound value written
    if t < 0: #since t has to be greter than 0, i write this, with a message to the user
        print "the time can not be negative!" #telling the user whats wrong
        sys.exit(1) #exiting the code
    elif t > 2*v0/g: #if the t value is too big it will this to the user as well
        print "the t value can not be that big!" #telling the user whats wrong
        sys.exit(1) #exiting the program
    else: #if t is the correct value, the program should excecute this
        y = v0*t - 0.5*g*t*t #defining the formula
        print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y) #a good looking print
except IndexError: #if the user did not write enough values earlier, the code should start here
    print "There is an index error!" #Telling the user what they did wrong
    v0 = float(raw_input("v0=")) #since the user did not assign any values, i will ask them more clearly to insert them here
    t = float(raw_input("t=")) #both time and starting velocity
    if t < 0: #t value still has to be correct, so i use the same code as above for ensuring that the the user puts in the correct values
        print "the time can not be negative!" #say what is wrong
        sys.exit(1) #exit program since the rest of the code below is now useless
    elif t < 2*v0/g: #for t values too big
        print "the t value can not be that big!" #to say what is wrong
        sys.exit(1) #the code below is useless, so i exit the code
    else: #if the t value is correct, then it will print!
        y = v0*t - 0.5*g*t*t #defining the formula
        print "After %.2f secounds, with a start velocity of %.2f the ball is %.3f meters above the ground." % (t, v0, y) #good looking print

"""
terminal >>> python ball_cml_tcheck.py 3 0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.

Med index error blir det:

terminal >>> python ball_cml_tcheck.py
There is an index error!
v0=3
t=0.6
After 0.60 secounds, with a start velocity of 3.00 the ball is 0.034 meters above the ground.

Hvis t er for stor paa sys.argv

python ball_cml_tcheck.py 5 5
the t value can not be that big!

hvis t er for liten paa raw_input
terminal >>> python ball_cml_tcheck.py
There is an index error!
v0=3
t=-5
the time can not be negative!
"""
