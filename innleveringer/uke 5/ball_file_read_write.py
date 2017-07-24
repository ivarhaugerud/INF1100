#a)
def read_ball(filename): #making a function to open and read files with the variable as the filename
    infile = open(filename, "r") #opens a file
    line = infile.readline() #the variable "line" now reads the line you are on
    line = line.split() #splits the first line
    v0 = float(line[-1]) #the last string in the first line is now called v0
    infile.readline() #skips a line
    t_values = [] #makes an empty list
    for line in infile: #goes through the rest of the lines in the document
        line = line.split() #splits the lioes
        for t in line: #for each value in each line
            t_values.append(float(t)) #appends it to the empty list called t_values
    infile.close() #closes the files
    return v0, t_values #returning the values i need for later

#b)
def test_foo(): #test function
    t_test = [0.1, 0.2, 0.3, 0.4, 1.2, 15, 3.6] #can choose these values as whatever
    v0_test = 12.0 #this is random number as well
    with open("ball2.dat", "w") as outfile: #writes a file, names the file "ball2.dat"
        outfile.write("v0: %.2f \n" % (v0_test)) #writes out the values for v0
        outfile.write("t:\n") #writes "t:" like the example file from the task
        for i in range(len(t_test)): #a list that prints out the list of t values we made above
            outfile.write("%g " % (t_test[i])) #writes them with a good amount of decimals
    v0, t_values = read_ball("ball2.dat") #now the new values v0, and t_values are collected from the formula in a. We here run the text file we just made in the lines above in the function from a, this will read the file and give us values for v0 and many t-values
    read_ball("ball2.dat") # runs the function
    assert v0 == v0_test #is the excpected value we wrote into "ball2.txt" the same as the formula in a) thinks it is
    assert len(t_values) == len(t_test) #same as above, but for the length of the t-values
    for i in range(len(t_test)):
        assert t_values[i] == t_test[i] #checks that all of the t values are correct
test_foo() #runs the test function

#c)
v0 = 3 #defining some variables
g = 9.81 #defining gravity
def y(t_values): #function for height of the ball
    return v0*t_values - 0.5*g*(t_values)**2 #returns the function

def creat_collums(filename): #makes a formule
    with open("ball3.dat", "w") as outfile: #the text file with collums will be called "ball3.dat"
        v0, t_values = read_ball(filename) #collects the v0 and t_values from the file we called in the function argument
        sorted_t_values = sorted(t_values)
        outfile.write("t-values[s]  |    y-values[m] \n") #writes a header to the table
        for i in sorted_t_values: #gets the values from the list valled t_values which was collected using the read_ball formula
            outfile.write("%5.2f        |      %5.2f \n" % (i, y(i))) #writes this

creat_collums("ball2.dat") #runs the formula from task c, with the file called ball2.dat

"""
terminal > python ball_file_read_write.py
nothing really happens in terminal, but the code generates two files, which are called ball2.txt and ball3.txt
these text files are correct on my computer as to what i wanted them to do
"""
