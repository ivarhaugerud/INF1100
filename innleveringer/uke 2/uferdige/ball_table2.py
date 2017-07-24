g = 9.81
v0 = 5.0
a = 10/9.81
n = 5
t_stop = 2.0*v0/g
dt = t_stop/n

hight = []
time = []

for i in range(0, n+1):
   t = i*dt
   y = v0*t - 0.5*g*t**2
   hight.append(y)
   time.append(t)

for i in range (len(hight)):
   print "the height is %5.2f meters after %5.2f secounds" % (hight[i], time[i])

