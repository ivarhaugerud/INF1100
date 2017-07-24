import numpy as np
import matplotlib.pyplot as plt
#Importing what I need for the task

epsilon = []
exact_error = []
n = []
#Creating empty lists

infile = open("lnsum.dat", "r") #open file
for i in range(24):
    infile.readline()
for line in infile: #go trough every line within a for-loop
    line = line.replace("\n", "") #at the end of each line it says "\n" to create a new line, with this command i remove the letters "\n" from the end of each line
    epsilon.append(float(line[9:14])) #convert to float and append, no need to strip the numbers
    exact_error.append(float(line[29:37])) #convert to float, then append. No need to stip the numbers
    n.append(int(line[41:])) #append the n-value as integers
    #Reading of the file

eps = np.array(epsilon)
ext_err = np.array(exact_error)
n = np.array(n)
#"converting" the lists into arrays

plt.yscale('log') #making a logarytmic y-axis. I gogeld and found this way, if there is a more common way can you tell me in the feedback on devilry?
plt.plot(n, eps, "ro", label="epsilon values") #ploting the epsilon values as red dots
plt.plot(n, ext_err, "bo", label="exact error") #ploting the exact errors as blue dots
plt.title("epsilon-error graph") #graph titile
plt.legend(loc="best") #a box where the title of each graph will be displayed, this box will also be displayed the best possible spot
plt.xlabel("n-value") #choosing x-label
plt.ylabel("scalar") #choosing y-label, i think this one is ok
plt.show() #in the end showing the graph

infile.close() #closing the file i used earlier

"""
terminal > python read_error.py
# a good looking graph pops up
"""
