import math
import numpy as np


STEP = 25
n = 5
x = np.zeros(n)
x[0] = 1.0
# x = np.array([1.0, 0.0, 0.0, 0.0, 0.0])


def mse(a):
    se = 0
    for j in a:
        se += (j - 1 / n)**2
    return se / n


for i in range(STEP):
    print(i + 1)
    print(x)
    print('the mse is', mse(x))
    for pointer in range(n):
        x[pointer] = 0.5 * (x[pointer] + x[(pointer + 1) % n])
        x[(pointer + 1) % 5] = 0.5 * (x[pointer] + x[(pointer + 1) % n])

