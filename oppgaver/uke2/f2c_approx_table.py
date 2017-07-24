Farenheit = range(0, 101,10)
for i in Farenheit:
   t = (5.0/9.0)*(i-32)
   k = (i-30.0)/2.0
   print "the accurate value is %5.2f , the approximate value is %5.2f , the temeratue in Farenheit is %5.2f" % (t, k, i)

