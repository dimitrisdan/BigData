import numpy as np
from scipy import optimize

f = open("listpoint.txt",'r')

x = []
y = []

for line in f.read().split('\n'):
       x.append(float(line.split(" ")[0]))
       y.append(float(line.split(" ")[1]))


z = np.polyfit(x, y, 3)
print x
print y

# A 3rd degree polynomial is expected to have 3 roots. 
# This has 1 real root and 2 imaginary
# scipy.optimize.fsolve will return the real root

p = np.poly1d(z)

#Polynomial coefficients
print p

print optimize.fsolve(p,[-2])
