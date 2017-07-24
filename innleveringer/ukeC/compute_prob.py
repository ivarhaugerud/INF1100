import random

def play_game(i):
    N = 10**i
    M = 0
    for k in range(N):
        random_num = random.random()
        if random_num >= 0.5 and random_num <= 0.6:
            M += 1
    return float(M)/N

prob1 = play_game(1)
prob2 = play_game(2)
prob3 = play_game(3)
prob6 = play_game(6)

print prob1
print prob2
print prob3
print prob6
