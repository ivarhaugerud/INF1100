g = 9.81 #sorry in advane for grammar mistakes
v0 = 5.0
a = 10/9.81
n = 5
t_stop = 2.0*v0/g
dt = t_stop/n      #decide the name of the variables

y1 = []
t1 = []            #create two empty lists

for i in range(0, n+1):
   t = i*dt
   y = v0*t - 0.5*g*t**2
   y1.append(y)
   t1.append(t)   #fill the empty lists with values for both time and height
# a)
ty1 = []          #created empty list
ty1.append(y1)
ty1.append(t1)    #added the two lists from earlier into the new and empty list
print " "
print "  hight time" #added this to make it look better
for i in range(len(ty1[0])): 
   print " %5.2f %5.2f " % (ty1[0][i], ty1[1][i]) #first use the presentage sign to create clearer and better looking printing, and then decide which values the for-loop is going to collect from the list. First i write [0] because i want it to collect it from the first list, and from that list collect a value [1]. After it has collected this, i move over to the secound list it is going to collect data from. Since this list is the secound list in ty1, I have to write ty[1], and then specify to to collect the value i. 

print " "   # made this to make the print look better

# b)
print "  hight time"     #this is also just for it to look better
ty2 = [[y, t] for y, t in zip(y1, t1)] #the list ty2 is made from zipping the two other lists tougheter, with the value y and t
for y, t in ty2:        #then i ask the program to print the values from the newly created list. 
    print " %5.2f %5.2f" % (y, t)
print " "

"""
terminal >>> python ball_table3.py
 
  hight time
  0.00  0.00 
  0.82  0.20 
  1.22  0.41 
  1.22  0.61 
  0.82  0.82 
  0.00  1.02 
 
  hight time
  0.00  0.00
  0.82  0.20
  1.22  0.41
  1.22  0.61
  0.82  0.82
  0.00  1.02
 
"""
