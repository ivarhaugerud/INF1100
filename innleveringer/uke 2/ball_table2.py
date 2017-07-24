g = 9.81 #sorry in advance for the grammer, hight = height
v0 = 5.0
a = 10/9.81
n = 5
t_stop = 2.0*v0/g
dt = t_stop/n       #desciding the variables and a good way to know what values for time to use later

hight = []
time = []           # made empty lists I can .append the values into

for i in range(0, n+1):
   t = i*dt
   y = v0*t - 0.5*g*t**2 
   hight.append(y)
   time.append(t)         #appending the values into the lists

for i in range (len(hight)): #getting the value 1 from each of the lists, and doing this untill the list is empty
   print "the height is %5.2f meters after %5.2f secounds" % (hight[i], time[i])  # Collects the value one by one in each of the lists and uses this value, then  printing the values from the list  in a nice, and clear way with two decimals.
   

"""
terminal >>> python ball_table2.py
the height is  0.00 meters after  0.00 secounds
the height is  0.82 meters after  0.20 secounds
the height is  1.22 meters after  0.41 secounds
the height is  1.22 meters after  0.61 secounds
the height is  0.82 meters after  0.82 secounds
the height is  0.00 meters after  1.02 secounds
"""
