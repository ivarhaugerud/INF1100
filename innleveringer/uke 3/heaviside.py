# a)
def H(x):
    a = x < 0
    b = x >= 0
    return a, b

# b)
def test_H():
    print "test_H is running!"
    testing_values = [-10, -10e-15, 0, 10e-15, 10]
    expected_tested_results = [(True, False), (True, False), (False, True), (False, True), (False, True)]
    expected1 = expected_tested_results[0]
    computed1 = H(testing_values[0])
    expected2 = expected_tested_results[1]
    computed2 = H(testing_values[1])
    expected3 = expected_tested_results[2]
    computed3 = H(testing_values[2])
    expected4 = expected_tested_results[3]
    computed4 = H(testing_values[3])
    expected5 = expected_tested_results[4]
    computed5 = H(testing_values[4])
    success = expected1 == computed1 , expected2 == computed2, expected3 == computed3, expected4 == computed4, computed5 == expected5
    msg = "expected values were %s and computed value were %s " % (expected_tested_results, H(testing_values)) 
    if success:
        print "Every value was correct!"
    else:
        print "One or more values are incorrect!"
    assert success, msg

test_H()

"""
terminal > python heaviside.py
test_H is running!
Every value was correct!
""""
