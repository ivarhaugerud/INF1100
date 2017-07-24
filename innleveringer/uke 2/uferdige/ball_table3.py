g = 9.81
v0 = 5.0
a = 10/9.81
n = 5
t_stop = 2.0*v0/g
dt = t_stop/n

y1 = []
t1 = []

for i in range(0, n+1):
   t = i*dt
   y = v0*t - 0.5*g*t**2
   y1.append(y)
   t1.append(t)

# a)
ty1 = []
ty1.append(y1)
ty1.append(t1)
print " "
print "  hight time"
for i in range(len(ty1[0])):
   print " %5.2f %5.2f " % (ty1[0][i], ty1[1][i])

#import pprint
#pprint.pprint(ty1)
print " " 

# b)
print " "
print "  hight time"
ty2= [[y, t] for y, t in zip(y1, t1)]
for y, t in ty2:
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
