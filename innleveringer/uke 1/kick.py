from math import *

g = 9.81 #gravity acceleration, in meter pr. second
q = 1.2E-3 #air density, kilo grams pr. qubic meter
a = 0.11 #radius of ball in cm
A = pi*a**2 # Surface areal of the ball, measured in m^2
V = 120/3.6 #Velocity, divided by 3.6 to make it meters pr. sec.
m = 0.43 #mass, in kilo grams

Fg = m*g
Fd = 0.5 * Cd * q * A * V**2

print """Tyngdekraften på ballen fra jorda er %.2f Newton
 og luftmostanden på ballen er %.2f Newton""" % (Fg, Fd)
