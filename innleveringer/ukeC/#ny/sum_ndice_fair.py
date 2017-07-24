import numpy as np
from sum_4dice import play_game, game
#importing what I need
#this inclued the two functions from the previous task, this saves me a lot of typing

def finding_precentage(s, number_of_games, n): #creating a function for finding the percentage of times the player actually win
    M = 0 #a counter 
    for i in range(number_of_games): #number of times he will try to play
        if game(n) < s: #does the player win? if so:
            M += 1 #one more for each time the player wins

    return float(M)/number_of_games #returning the percentage odds that the player wins, this value can I use to find a fair value for winning the game

number_of_games = 100000 #amount of times the player will play
start_capital = 100 #his start capital
p = finding_precentage(9, number_of_games, 4) #the chance that he wins the game when throwing 4 die, and wanting the value to be lower than 9
q = 1 #the money the player has to pay for each game
r = float(q)/p #this is the correct r-value for a fair game, i used the reasoning in section 8.3.2

das_capital = play_game(4, 9, q, r, 100, 1000) #calls the function with these arguments, and returns the player end capital, a reference to Karl Marx

print "with start capital %g euros, and with a win reward %g euros, the end amount is %g. Which is %g euros differnt from the start amount!"  % (start_capital, r, das_capital, abs(das_capital - start_capital))
#good looking print statement

"""
terminal > python sum_ndice_fair.py 
with start capital 100 euros, and with a win reward 18.4945 euros, the end amount is 80.2108. Which is 19.7892 euros differnt from the start amount!
#the amount changes for each runs, depends on how lucky the player is, but average difference should be zero
"""
