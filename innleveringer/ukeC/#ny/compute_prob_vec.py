import numpy as np
#using numpys random function

def play_game(i): #defining the function, takes one argument, as the previous task
    N = 10**i #how many runs I want
    
    random_num = np.random.random(N) #gets a random number between 0 and 1, and i get an array with N amounts of these numbers
    sum1 = random_num[random_num > 0.5] #first ruling out all the numbers that were below 0.5
    sum2 = sum1[sum1<0.6]#then ruling out the numbers above 0.6
    M = len(sum2) #the length of the array left is the amount of numbers that fits the criteria i set
    return float(M)/N #return the amount

range_ = [1, 2, 3, 6] #the different values

for i in range_: #different i values
    print "number of runs = %g, probability = %g" % (10**i, play_game(i)) #a good looking print

"""
terminal > compute_prob_vec.py
number of runs = 10, probability = 0
number of runs = 100, probability = 0.13
number of runs = 1000, probability = 0.09
number of runs = 1e+06, probability = 0.099732
"""
