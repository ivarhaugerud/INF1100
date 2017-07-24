initial_amount = 100
p = 1.23
amount = initial_amount
years = 0 
while amount <= 1.5*initial_amount:
    amount += p/100*amount
    years += 1
print years
