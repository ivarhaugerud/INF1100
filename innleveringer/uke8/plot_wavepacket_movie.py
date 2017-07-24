import numpy as np
import matplotlib.pyplot as plt
import glob, os
#importing what I need

for filename in glob.glob("anim_graph*.png"):
    os.remove(filename) #deleting previous files with the same name

plt.ion() #interactive mode is turned on
n = 60.0 #will use later, amount of times i run trough the animation

def f(x, t): #Defining the formula
  return np.e**(-(x-3*t)**2)*np.sin(3*np.pi*(x-t)) #this is what shall be returned

x_ary = np.linspace(-6, 6, 1001) #array of the x-values i will use, from -6 to +6 as the task says, with 1001 points

for i in range(int(n+1)): #61 image files will be saved since we do this 61 times
    plt.clf() #to clear the graph for each go in the for-loop
    plt.axis([-6, 6, -1.1, 1.1])
    plt.title("wavepacket") #title name
    plt.xlabel("length") #x-axis label
    plt.ylabel("height") #y-axis label
    plt.plot(x_ary, f(x_ary, -1+i/(n/2)), label="graph, t=%4.2f" % float((-1+i)/(n/2))) #the function, with uniformaly spaced t-values in the function
    plt.legend(loc="best") #places the box at the best possible spot
    plt.pause(1.0/6.0) #a pause which lasts the 1 sixth of a secound
    plt.draw() #drawing the function
    plt.savefig("anim_graph%04d.png" % (i+1)) #I need to write "%04d" because i want zeroes before the number of the file so they will be stored in the correct order

plt.show()#this will make it hold the image of the graph up on the screen after it is finished with all the short lasting pictures
plt.ioff() #interactive mode is turned off

""""
terminal > python plot_wavepacket_movie.py
# after the program is done storing the files I write:
convert anim_graph*.png anim_graph.gif
and all the files are converted to one gif
"""
