import numpy as np
import random
import matplotlib.pyplot as plt
#importing what I need, I decided to include a plot, I hope that is okay

def throw_2_die(N):#a function to throw two die
    eyes = {} #empty dictionary
    eyes_prob = [] #empty list
    array = np.zeros(11) #empty array, the holy trinity

    for t in range(2, 13):
        eyes[t] = 0 #desciding what values i want the array to include, this is the different possebilities for sums

    for i in range(N): #for "appending" into the dictionary
        die = np.random.randint(1, 7, 2) #getting an array of two die-eyes
        die_sum = np.sum(die) #sum the die toughether
        eyes[die_sum] += float(1) #the dictionary value will get one larger

    for k in range(2, 13): #to convert the sum of the dictionary into a percetage
        eyes_prob.append(float(eyes[k])/N) #the function
        array[k-2] = eyes[k] #I need the -2, since the sum is only defined from 2 - 12, but I want my array to start at zero

    return eyes, eyes_prob, array #what i am returning

N = 10000 #amount of runs
eyes, prob, sum_array = throw_2_die(N) #calling the function
exact_prob = [1.0/36, 2.0/36, 3.0/36, 4.0/36, 5.0/36, 6.0/36, 5.0/36, 4.0/36, 3.0/36, 2.0/36, 1.0/36] #the exact probabilty I calculated by hand


for i in range(11): #a print statement, i realised later i should probably have made a talbe, that would look better
    print "%3.0f was the sum %5.0f times, and propability for this was %2.0f percentage. The difference between the programmed percentage and the analytic precetnage is %g percentage points" % ((i+2), eyes[i+2], prob[i]*100, abs(prob[i]-exact_prob[i])*100)

#for fun I decided to make a plot
colour = ["yo", "ro", "yo", "ro", "yo", "ro", "yo"]
for i in range(13):
    plt.clf()
    percent_array = sum_array/N #finding the percentage
    x = np.linspace(2, 12, 11) #creating x-array which is the possible outcomes of sum when throwing two die
    plt.axis([1.5, 13.5, 0, 0.2]) #desciding axis
    plt.plot(x[:i], percent_array[:i], "g", label="juletre") #plotting the percentage
    plt.plot(x[:i], percent_array[:i], "ro", label="julepynt") #with red dots between each line
    plt.pause(0.4)
    plt.xlabel("dice-eye sum") #labels and titles are nice
    plt.ylabel("percentage of times the sum was achived")
    plt.title("Ha en gledelig jul!")
    plt.legend(loc="best") #it looks like a christmas tree!
    plt.draw()

for i in range(7):
    plt.clf()
    percent_array = sum_array/N #finding the percentage
    x = np.linspace(2, 12, 11) #creating x-array which is the possible outcomes of sum when throwing two die
    plt.axis([1.5, 13.5, 0, 0.2]) #desciding axis
    plt.plot(x, percent_array, "g", label="juletre") #plotting the percentage
    plt.plot(x, percent_array, "ro", label="julepynt") #with red dots between each line
    plt.plot(x[5], percent_array[5], colour[i], label="julestjernen")
    plt.pause(0.4)
    plt.xlabel("dice-eye sum") #labels and titles are nice
    plt.ylabel("percentage of times the sum was achived")
    plt.title("Ha en gledelig jul!")
    plt.legend(loc="best") #it looks like a christmas tree!
    plt.draw()
plt.show()

"""
python freq_2dice.py
  2 was the sum   299 times, and propability for this was  3 percentage. The difference between the programmed percentage and the analytic precetnage is 0.212222 percentage points
  3 was the sum   521 times, and propability for this was  5 percentage. The difference between the programmed percentage and the analytic precetnage is 0.345556 percentage points
  4 was the sum   858 times, and propability for this was  9 percentage. The difference between the programmed percentage and the analytic precetnage is 0.246667 percentage points
  5 was the sum  1150 times, and propability for this was 12 percentage. The difference between the programmed percentage and the analytic precetnage is 0.388889 percentage points
  6 was the sum  1369 times, and propability for this was 14 percentage. The difference between the programmed percentage and the analytic precetnage is 0.198889 percentage points
  7 was the sum  1643 times, and propability for this was 16 percentage. The difference between the programmed percentage and the analytic precetnage is 0.236667 percentage points
  8 was the sum  1348 times, and propability for this was 13 percentage. The difference between the programmed percentage and the analytic precetnage is 0.408889 percentage points
  9 was the sum  1119 times, and propability for this was 11 percentage. The difference between the programmed percentage and the analytic precetnage is 0.0788889 percentage points
 10 was the sum   846 times, and propability for this was  8 percentage. The difference between the programmed percentage and the analytic precetnage is 0.126667 percentage points
 11 was the sum   581 times, and propability for this was  6 percentage. The difference between the programmed percentage and the analytic precetnage is 0.254444 percentage points
 12 was the sum   266 times, and propability for this was  3 percentage. The difference between the programmed percentage and the analytic precetnage is 0.117778 percentage points
"""
