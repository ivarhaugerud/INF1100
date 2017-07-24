s = 0.0
k = 1
M = 100
while k <= M:  # Changed the "<" with "<=" beacause i wanted to include the value for M
    s += (1.0/k) # Here i changed it from INT to Float by using decimals
    k += 1  # it was an error here, because the value k did not increase, therefor the while loop lasted forever
    
print s

