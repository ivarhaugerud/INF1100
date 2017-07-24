import numpy as np

def play_game(i):
    N = 10**i
    M = 0
    random_num = np.random.random(N)
    sum1 = random_num[random_num > 0.5]
    sum2 = sum1[sum1<0.6]
    M = len(sum2)
    return float(M)/N

range_ = [1, 2, 3, 6]

for i in range_:
    print "number of runs = %g, probability = %g" % (10**i, play_game(i))
