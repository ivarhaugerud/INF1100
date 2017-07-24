s = 0.0; k = 1; M = 3
while k <= M:    # Error 1: Changed the "<" with "<=" beacause i wanted the highet value to be M, not (M-1)
    s += (1.0/k) # Error 2: Here i changed it from int to float by using decimals for the value 1.0 and in the definition of k above
    k += 1       # Error 3: The value k did not increase, therefor the while loop lasted forever because k was never bigger than M
    
print s          #My hand calculations are the same as with python

"""
terminal >>> python sum_while.py
1.83333333333
"""

