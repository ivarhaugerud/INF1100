Farenheit = range(0, 101,10) #made list, from zero to 100, increasing with 10 for each step. I had to write something larger than 100 so that it includes the value for 100
print "    F        C    C-approx"   #so it is clear what the three different values in the collums are
for i in Farenheit:              #collects values from the list called Farenheit
   t = (5.0/9.0)*(i-32)          #I called the accurat value for celcius t
   k = (i-30.0)/2.0             # I called the aprox value for celcius k
   print "%6.2f    %6.2f    %6.2f" % (i, t, k)             #prints the values for the temperatures with two decimal points and using 5 places so that they are equally apart

"""
terminal >>> python f2c_approx_table.py
"""
