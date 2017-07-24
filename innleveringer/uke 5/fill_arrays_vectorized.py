import numpy as np #importing numpy because i am going to use arrays
def h(x): #defining a function
    return 1/(np.sqrt(2*np.pi))*np.exp(-0.5*x**2) #returning the function, remember np. before math notations

x_values = np.linspace(-4, 4, 41) #using the linspace function i can make an array from -4 to 4 with 41 points
y_values = h(x_values) #using the x_values inside the function above to make y_values
#good looking print
print "----------------------"
print "x-values  |   y-values"
print "----------------------"
for i in x_values:
    print "%5.2f     |    %5.6f" % (i, h(i)) # a lot decimals in y-value because the values are so small
print "----------------------" #the numbers I get here should be equal to the numbers i gor from fill_arrays_loop.py
#and the values are the same

"""
terminal > python fill:arrays_vectorized.py
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
