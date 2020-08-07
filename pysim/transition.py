import numpy as np


n = 4  # number of points on a circle
L = 0.51  # prob of going left, right, and staying
R = 0.49
S = 0

# creating the transition matrix
P = np.zeros((n, n))
for row in range(n):
    P[row][row] = S
    P[row][(row + 1) % n] = L
    P[row][(row - 1) % n] = R

t = 10  # time step

# multiply the transition matrix t times, and record the result of each time
for i in range(t):
    P = np.dot(P, P)
    print(P)
    print()  # separation blank line
