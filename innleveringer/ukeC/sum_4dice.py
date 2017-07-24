import numpy as np
import sys

def game(n):
    die = np.random.randint(1, 7, n)
    sum_of_die = np.sum(die)
    return sum_of_die

def play_game(n, s, q, r, start_capital, number_of_games):
    for i in range(number_of_games):
        start_capital -=  q
        if game(n) < s:
            start_capital += r

    return start_capital

if __name__ == "__main__":
    r = float(sys.argv[1])
    number_of_games = int(sys.argv[2])

    end_capital = play_game(4, 9, 1, r, 100, 10000)
    print "with a start value of 100, and a award of %g euros, and a price of 1 euros, the end capital is %g " % (r, end_capital)
