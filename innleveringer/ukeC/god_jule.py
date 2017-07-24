import numpy as np
import matplotlib.pyplot as plt
def throw_2_die(N):
    eyes = {}
    eyes_prob = []
    array = np.zeros(11)

    for t in range(2, 13):
        eyes[t] = 0

    for i in range(N):
        die = np.random.randint(1, 7, 2)
        die_sum = np.sum(die)
        eyes[die_sum] += float(1)


    for k in range(2, 13):
        eyes_prob.append(float(eyes[k])/N)
        array[k-2] = eyes[k]

    return eyes, eyes_prob, array

N = 10000
eyes, prob, array = throw_2_die(N)

for i in range(11):
    print "%3.0f was the sum %2.0f times, and propability for this was %2.0f percentage" % ((i+2), eyes[i+2], prob[i]*100)
for i in range(12):
    x = np.linspace(2, 12, 11)
    plt.axis([2, 12, 0, 2000])
    plt.plot(x[:i], array[:i], "g")#, label="grantre")
    plt.plot(x[:i], array[:i], "ro")# label="julepynt")

    plt.title("Ha en gledelig jul!")
    plt.pause(0.3)
    plt.draw()
plt.legend(loc="best")
plt.show()
