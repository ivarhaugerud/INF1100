#a)
def read_densities(filename): #making function
    infile = open(filename, "r") #opening file
    densities = {} #creating empty dictinary
    for line in infile: #going trough each line in the file
        words = line.split() #split the line into words
        density = float(words[-1]) #creating variable density
        substance = " ".join(words[:-1]) #creating cariable substance, and join all the words, up to the last
        densities[substance] = density #creating a new variable in the dictionary
    infile.close()
    return densities #returning the finished dictionary

#b)
def read_density_strip(filename): #function for reading file
    infile = open(filename, "r") #opening the file
    densities = {} #empty list for numbers
    for line in infile: #a for loop for the rest of the file
        substance =  line[:12].strip() #the first 12 letters of each line, remove the empty space and then append to the empty list
        density = float(line[12:].strip()) #the last 12 letters/numbers if each line, I remove the empty space
        densities[substance] = density #creating new variable in the dictionary
    infile.close() #close the file
    return densities #return the list

#c)
def test_read_file(): #creating a test function
    densities1 = read_densities("densities.dat") #calling the first function and reading the file
    densities2 = read_density_strip("densities.dat") #calling the secound function and reading the file
    success = densities1 == densities2 #defining what success is
    msg = "something is wrong!" #will get printed if something is wrong
    assert success, msg #checking if its correct

test_read_file()

"""
terminal > density_improved.py
"""
