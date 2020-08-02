import numpy as np
import math
import json


# parameters
n = 5
N = 10**6
pl = .25
pr = .25
ps = .5
epsilon = 0.0001


def check_equilibrium(v: np.array, num_points: int = n, e: float = epsilon) -> bool:
    """
    check whether the state vector v can be considered as reaching a uniform distribution
    :param v: the state vector represented in a numpy array
    :param num_points: the number of points around the circle
    :param e: error tolerance
    :return: true if v is near a uniform distribution, false otherwise
    """
    for i in v:
        if abs(i - (1 / num_points)) > e:
            return False
    return True


def sim():
    # create state vector
    v = np.zeros(n)
    v[0] = 1

