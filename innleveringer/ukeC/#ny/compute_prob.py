import random
#importing what I need

def play_game(i): #defining a class
    N = 10**i #the function depends on one value, that is what 10 is multiplied with
    M = 0 #this is the counter, which starts at zero
    for k in range(N): #a foor-loop which repeats N times
        random_num = random.random() #gets a random number between 0 and 1
        if random_num >= 0.5 and random_num <= 0.6: #if both of these are true, add one to M
            M += 1
    return float(M)/N #when the for-loop is finished it will take the amounts of success divided by amounts of tries

range_ = [1, 2, 3, 6] #the different values

for i in range_: #different i values
    print "number of runs = %g, probability = %g" % (10**i, play_game(i)) #a good looking print

"""
terminal > python compute_prob.py 
number of runs = 10, probability = 0.1
number of runs = 100, probability = 0.16
number of runs = 1000, probability = 0.096
number of runs = 1e+06, probability = 0.10019
"""
