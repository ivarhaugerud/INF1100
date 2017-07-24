import random
import numpy as np

def play_game():
        die_array = np.random.randint(1, 7, N)
        number_of_sixes = len(die_array[die_array==6])
        if number_of_sixes >= 1:
            return True
        else:
            return False

def simulator(M):
    counter = 0
    for k in range(M):
        if play_game():
            counter += 1
    return float(counter)/M

N = int(raw_input("number of dices to be thrown = "))
M = int(raw_input("number of experiments = "))

print "When rolling the dice %d times, the probabilityof getting at least one six is %g" % (N, simulator(M))

print ""
exact_prob = 11.0/36
N = 2
for i in range(8):
    print "When throwing two die the probabilty of getting at least on six is exactly %g, the computed prob with %g throws = %10.10f, difference from exact prob = %10.10f" % (exact_prob, 5**i, simulator(5**i), abs(exact_prob - simulator(5**i)))
