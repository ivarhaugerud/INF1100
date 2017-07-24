# a)
def H(x): 
    if x < 0:      #made an in test to which has the function to return the value i wanted depending on the value of X
        return 0
    else:  
        return 1

# b)
def test_H():               #made testfunction
    print "test_H is running" #to make sure the test is actually running
    testing_values = [-10, -10e-15, 0, 10e-15, 10]     #the values i want to test for
    expected_tested_results = [(0), (0), (1), (1), (1)]    # the expected values i got from doing the calculations by hand
    for i in range(0, 5, 1):                               # made a for list to make the code shorter and cleaner
        success = H(testing_values[i]) == expected_tested_results[i]  #Using the fuction H(x) from earlier, and testing if it will be correct. 
        msg = "wrong values for number %g  in the list testing_values! Expected value was %s and computed value was %s" % (i, expected_tested_results[i], H(testing_values[i]))
# the message that will appear if something goes wrong
        if success:
            print "Test number  %g was correct" % (i) #if a line is correct for the value i, it will print it, and say which value it was for i
        else:
            print "Test %g was incorrect" % (i) #the same as the one above, excpet for errors instead
        assert success, msg #for each time it runs through the list it will assert success or msg

test_H()  # running the test function to check if it works

"""
terminal > python heaviside3.py
test_H is running
Test number  0 was correct
Test number  1 was correct
Test number  2 was correct
Test number  3 was correct
Test number  4 was correct
"""



