import numpy as np #importing numpy, need this for arrayz
def h(x): #making the formula that i need
    return 1/(np.sqrt(2*np.pi))*np.exp(-0.5*x**2) #returning it

x_empty = np.zeros(41) #making "empty" arrays, they are not really empty, but just 41 zeroes
y_empty = np.zeros(41) #arrays can not be made larger, so i will just change out the 0`s with the numbers i want later
for i in range(41): #i need 41 values
    x_empty[i] = -4+i*0.2 #starting at negative 4 moving up to positive 4, with 41 points, which equals a uniform distance of 0.2 between each point, did this math on paper
for i in range(41): #the y-values should also be 41 long
    y_empty[i] = (h(x_empty[i])) #the values "appendend" (not really appended) in are the i values put into the formula h(x)

print "----------------------" #making a nice printing statement
print "x-values  |   y-values"
print "----------------------"
for i in x_empty:
    print "%5.2f     |    %5.6f" % (i, h(i)) #6 decimals for the y-value so we can differenciate between each of the x - values, since the y-values are so small
print "----------------------"

"""
terminal > python fill_arrays_loop.py
----------------------
x-values  |   y-values
----------------------
-4.00     |    0.000134
-3.80     |    0.000292
-3.60     |    0.000612
-3.40     |    0.001232
-3.20     |    0.002384
-3.00     |    0.004432
-2.80     |    0.007915
-2.60     |    0.013583
-2.40     |    0.022395
-2.20     |    0.035475
-2.00     |    0.053991
-1.80     |    0.078950
-1.60     |    0.110921
-1.40     |    0.149727
-1.20     |    0.194186
-1.00     |    0.241971
-0.80     |    0.289692
-0.60     |    0.333225
-0.40     |    0.368270
-0.20     |    0.391043
 0.00     |    0.398942
 0.20     |    0.391043
 0.40     |    0.368270
 0.60     |    0.333225
 0.80     |    0.289692
 1.00     |    0.241971
 1.20     |    0.194186
 1.40     |    0.149727
 1.60     |    0.110921
 1.80     |    0.078950
 2.00     |    0.053991
 2.20     |    0.035475
 2.40     |    0.022395
 2.60     |    0.013583
 2.80     |    0.007915
 3.00     |    0.004432
 3.20     |    0.002384
 3.40     |    0.001232
 3.60     |    0.000612
 3.80     |    0.000292
 4.00     |    0.000134
"""
