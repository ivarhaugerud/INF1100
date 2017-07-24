import matplotlib.pyplot as plt
import numpy as np
#importing what I need

x = []
y = []
#creating empty lists

infile = open("data.txt", "r") #opening file
s = float(infile.readline()) #finding out what s is, that is the time period between each measurment
for line in infile: #for loop for each line left in the file
    line = line.split() #splitting the line into words
    x.append(float(line[0])) #the first word is the x-cordinates
    y.append(float(line[1])) #the secound word is the y-cordinates

x = np.array(x)
y = np.array(y)
#converting the lists into arrays

#a)
plt.plot(x, y, label="trip") #plot cordinates with label
plt.legend(loc="best") #showing the box
plt.xlabel("x-cordinates") #label for x-axis
plt.ylabel("y-cordinates") #label for y-axis
plt.title("trip cordinates") #title of the graph
plt.show() #showing the graph

#b)
Vx = np.zeros(len(x)-1)
Vy = np.zeros(len(y)-1)
t = np.zeros(len(y)-1)
#I need to derivate between each cordinate point, therefor i created empty arrays with one fewer point, because I need two points to find the average growth inbetween the points

for i in range(len(x)-1): #making the X, Y, and Time arrays in the same forloop
    Vx[i] = 1000*(float((x[i+1] - x[i])))/s #this is the formula for velocity on the x-axis
    Vy[i] = 1000*(float((y[i+1] - y[i])))/s #this is the formula for velocity on the y-axis
    t[i] = i*s #since the distance between each measurment is 15 secounds I multiply with 15

plt.plot(t, Vx, label="velocity x-direction")
plt.legend(loc="best")
plt.axis([0, 350, 8, 9])
plt.title("velocity y-direction")
plt.xlabel("time [s]")
plt.ylabel("velocity [m/s]")
plt.show()
#plotting the velocity in x-direction, making the box in the best possible spot, giving it a title and label for x and y axis
#i decided that the cordinates were measured in km, this is a guess. But i wanted to have units in my plot so i descided km
#then showing the graph
plt.plot(t, Vy, label="velocity y-direction")
plt.legend(loc="best")
plt.title("velocity y-direction")
plt.xlabel("time [s]")
plt.ylabel("velocity [m/s]")
plt.show()
#the same the notes from 45 to 47, but in the one above I included the plt.axis so that the graph is not sacled very small on the y-axis

"""
terminal > python position2velocity.py
first graph, comes up, when you close the first graph the secound one comes up, then the third graph comes up
"""
