a = 100 #Start money
p = 5 #Interest rate
n = 0 #What year I start the calculation in
#Descided the different variables

outfile = open("money.txt", "w") #opens a file i called money.dat
outfile.write("  Year |    Money ") #For good looking formating
while n < 16: #The while-loop will last for 15 years
    b = a + (p/100.0)*a #a represents X[i+1] and a represents X[i], I do this so that I can skip having a list full of values
    outfile.write("\n%6.0f | %8.2f " % (n, b)) #writing out the numbers to the file opend above
    a = b #to contine finding new numbers, the old "b" has to become the new "a"
    n += 1 #So that the while-loop wont last forever
outfile.close() #Closing the file just created

"""
terminal >  python fortune_and_infaltion1.py
"""
