import numpy as np
import sys
#importing what I need

def game(n): #function for the game
    die = np.random.randint(1, 7, n) #array with eyes-value for N throws
    sum_of_die = np.sum(die) #the sum of the array above
    return sum_of_die #returns the sum of the eyes of a throw with N die

def play_game(n, s, q, r, start_capital, number_of_games): #takes a lot of arguments, because I will use this one in the next task 
    for i in range(number_of_games): #number of games the player will play
        start_capital -=  q #for each game he or she playes, the player will have to pay an amount Q to join
        if game(n) < s: #if he wins, the player gains an amount of money, in euros, which equals r. He wins if the sum of the two die is lower than s
            start_capital += r

    return start_capital #returning the variabel start capital, which is now his finishing capital

if __name__ == "__main__": #the reason for this is that I will import the functions above, so I only want this to run when I actually call this text file in the terminal 
    r = float(sys.argv[1]) 
    number_of_games = int(sys.argv[2])
    #reading values from the command line
    end_capital = play_game(4, 9, 1, r, 100, 10000) #calls the function, with all its variables
    print "with a start value of 100, and a award of %g euros per win, and a price of 1 euros to join, the end capital is %g " % (r, end_capital)
    #a pint statement

"""
python sum_4dice.py 10 100000
with a start value of 100, and a award of 10 euros per win, and a price of 1 euros to join, the end capital is -4700 
"""
