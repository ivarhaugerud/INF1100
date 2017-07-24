import numpy as np
import matplotlib.pyplot as plt
#importing what I need

# a)
"""
Task a I did by hand. I am unsure about how to show my calculations, I hope this is good enough:
I did the calculations by hand.
A[j] = the taylor function for cos(x) for one value of n
Wrote A[j] / A[j-1] on a piece of paper and could shorten the anser down to:
-(x**2)/((2j-1)*2j)
therefor A[j] can be expressed with the function on line 11, multiplied with A[j-1]
I use this in task b). A good thing with the new way to write A[j] is that we do not need factorial, because
factorial can lead to very large answers.
"""

#b)
def t_cos(x, n): #defining a formula for the taylor function for cos x
    Sp = 0 #start values for the sum
    Ap = 1 #start values for cos x, when a = 0
    for i in range(1, n+1): #a for look starting with i = 1, and ending in i = n
        App = -((x**2)/float(((2.0*i-1.0)*(2*i))))*Ap #the function for A[j], showed in task a) how i got this. I express this without saving it in arrays so it is easier for the computer to handle
        Spp = Ap + Sp #The sum equals
        Ap = App #changing the App to the Ap, so we use this the next run of the for-loop
        Sp = Spp #Changing Sp to be the old Spp so we use this for the sum
    return Spp, abs(App) #returning what i need

#c)

def test_taylor_cos(): #making a test function
    computed_value1, computed_value2 = t_cos(3, 2) #testing for x = 3, and n = 2
    tol = 10**(-10) #desciding a tolerance
    expected_value1 = -3.5
    expected_value2 = 3.375 #my hand calculations gave me these two ansers
    success = abs(computed_value1 - expected_value1) < tol and abs(computed_value2 - expected_value2) < tol #if both are true it is a success
    msg = "something worng happend!" #if one of the parts on line 35 are False, this will print because of the assert on line 37
    assert success, msg #asserting

test_taylor_cos() #running the test function and testing if i get en error or not

#d
x = np.linspace(0, 4*np.pi, 100) #array of x-values
plt.plot(x, np.cos(x), label="cos(x)") #ploting the real graph
for i in range(2 , 17, 2): #plotting some different graphs with with differnt n values
    a, b = t_cos(x, i) #x is always the same, i increases to show how the taylor polynom looks more and more like the original graph when n increases
    plt.plot(x, a, label="cos(x), n = %d" %i) #plotting the Spp value from the function called above, i do not use the App
    plt.legend(loc="best") #putting the label box the best possible place. I am unsure if I should include labels or not, since there are so many graphs in the same pic. Would be nice if you could clear this up in the feedback on devilry
    plt.title("Taylor of cos(x)") #title
    plt.xlabel("x-value") #xlabel
    plt.ylabel("y-value") #ylabel
    plt.axis([0, 4*np.pi, -2, 2]) #desciding what the axis should be
plt.show() # showing the final graph with all the things written above

"""
terminal > python cos_Taylor_series_diffeq.py
"""
