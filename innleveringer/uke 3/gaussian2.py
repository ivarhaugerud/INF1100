from math import sqrt, e, pi #importing the math i need for the fuction

def gauss(x, m=0, s=1):      #defining the function with the variables
    fx = (1/(sqrt(2*pi)*s)*e**(-0.5*((x-m)/s))**2) #writing out the function
    return fx                #returning the function 

M = 0; s = 2; n = 2          #desciding values forfor my uniformaly spaced table
uniformly_spaced_values = range(M - 5*s, M + 5*s+1, n) #putting these values into a list, i made the max value a bit different because i wanted it to include the value for (M +5*s), and because of that i had to add a number smaller than two

for x in uniformly_spaced_values:               #collecting the values from the list, so that x is uniformly spaced 
    print "f(x) = %14.2f when x = %6.2f" % (gauss(x, m=0, s=1), x) #putting  each value in the list into the formula, and printing the formula, and the x-value each time in a good looking table. I was unsure weather or not this counts as a table? I could also write it out without the text, and just have two collums with text at the top. Since the values were so different i had to include 14 spaces for it to print into

