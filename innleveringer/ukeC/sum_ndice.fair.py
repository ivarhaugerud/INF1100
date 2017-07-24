import numpy as np
from sum_4dice import play_game, game

def finding_precentage(s, number_of_games, n):
    M = 0
    for i in range(number_of_games):
        if game(n) < s:
            M += 1

    return float(M)/number_of_games

number_of_games = 100000
start_capital = 100
p = finding_precentage(9, number_of_games, 4)
print p
q = 1
r = float(q)/p

das_capital = play_game(4, 9, q, r, 100, 1000)

print "with start capital %g euros, and with a win reward %g euros, the end amount is %g. Which is %g euros differnt from the start amount!"  % (start_capital, r, das_capital, abs(das_capital - start_capital))
