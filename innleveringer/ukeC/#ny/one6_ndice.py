import random
import numpy as np
import sys
#importing what I need

def play_game(): #a function for playing the game
        die_array = np.random.randint(1, 7, N) #getting an N-long array filled with dice-values
        number_of_sixes = len(die_array[die_array==6]) #the length of the array which is they array with only sixes
        if number_of_sixes >= 1: #check if its more than zero times that a 6 was included in one of them when you threw the dice N times
            return True #returning True means that an if-test will run if it calles a True, while if it returns a False, it means that the if-test will skip to the "else"
        else:
            return False

def simulator(M): #function for simulating the game
    counter = 0 #a counter
    for k in range(M): #runs the play_game function M times 
        if play_game(): #if it returns a True, it will add one to the counter
            counter += 1 
    return float(counter)/M #when it has done the play_game() M times, it will divided the counter with the amounts of run to find a percentage

N = int(sys.argv[1])
M = int(sys.argv[2])
#takes arguments from the command line
print "" #makes a space
print "When rolling %d die  %g times, the probabilityof getting at least one six is aproximatley  %g" % (N, M,  simulator(M))
#a good looking print statement which runs the functions above

print "" #makes a space
exact_prob = 11.0/36 #the exact prob, given in task
N = 2 #I will throw two die
for i in range(8): #and I will run the test with 8 different values of M
    print "When throwing two die the probabilty of getting at least on six is exactly %g, the computed prob with %6.0f throws = %10.10f, difference from exact prob = %10.10f" % (exact_prob, 5**i, simulator(5**i), abs(exact_prob - simulator(5**i)))
# a good looking print statement, i could have made this into a table, would have looked better

"""
terminal > one6_ndice.py 9 1000

When rolling 9 die  1000 times, the probabilityof getting at least one six is aproximatley  0.777

When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with      1 throws = 1.0000000000, difference from exact prob = 0.3055555556
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with      5 throws = 0.2000000000, difference from exact prob = 0.3055555556
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with     25 throws = 0.3200000000, difference from exact prob = 0.0255555556
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with    125 throws = 0.2320000000, difference from exact prob = 0.0304444444
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with    625 throws = 0.3216000000, difference from exact prob = 0.0064444444
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with   3125 throws = 0.3094400000, difference from exact prob = 0.0067644444
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with  15625 throws = 0.3040640000, difference from exact prob = 0.0038595556
When throwing two die the probabilty of getting at least on six is exactly 0.305556, the computed prob with  78125 throws = 0.3066880000, difference from exact prob = 0.0013116444
"""
