import random
import itertools
import numpy as np
from numba import jit, cuda


# The following function makes a dictionary that contains all the permutations 
# starting with 1, assigns 0 to each key in the dictionary. 
# The input n is the number of cards
# @jit(target="cuda")
def make_map(n):
    a = list(range(1, n+1))
    p_map = {}
    
    # Get all the permutations of numbers from 1 to n
    whole_permutations = list(itertools.permutations(a))
    
    # Get all the permutations that starts with 1
    p = []
    for x in whole_permutations:
        if x[0] == 1:
            temp = list(x)
            p.append(temp)
            p_map[str(temp)] = 0
    print(p)
    print(len(p))
    print(p_map)
    print()
    return p_map, p


# The following function turns a list of numbers into a string with space 
# in between each number
# The input a_list is a list of numbers
# def str((a_)list):
#     s = ""
#     for x in range(len(a_list)):
#         s = s + str(a_list[x])
#         if x != (len(a_list) - 1):
#             s = s + " "
#     return s


# The card simulation function. The input t stands for the number of times 
# swapping the cards.
# @jit(target="cuda")
def card_sim(n, t):
    p_map, p = make_map(n)
    # each number in cards stands for a card
    cards = np.arange(1, n + 1)
    
    # Swap cards for t times
    counter = 0
    while counter < t and check_relative(p_map, p, counter) != True:
        r = random.randint(0, n-1)
        prob = random.random()
        # Swap one card and the one after it
        if prob > 0.5:
            if r == n-1:
                cards[r], cards[0] = cards[0], cards[r]
            else:
                cards[r], cards[r+1] = cards[r+1], cards[r]
        update(p_map, cards)
        counter += 1
    for x in p:
        print(x, " ", p_map[str(x)])
    return counter


# The following function checks whether uniform distribution has been reached.
# m stands for the dictionary (hashmap), p stands for the list of permutations
# that are keys in the hashmap
# @jit(target="cuda")
def check_relative(m, p, counter):
    num_permutations = len(p)
    for x in p:
        if counter == 0:
            return False
        if m[str(x)] < 0.9 * counter / num_permutations or m[str(x)] > 1.1 * counter / num_permutations:
            return False
    print(counter)
    return True


# The following function takes in a map m and the current card configuration 
# cards, and adds 1 to value of the corresponding key
# @jit(target="cuda")
def update(m, cards):
    index = list(cards).index(1)
    # The current configuration of the cards
    configuration = []
    for j in range(index, len(cards)):
        configuration.append(cards[j])
    for k in range(0, index):
        configuration.append(cards[k])
    m[str(configuration)] += 1


result = np.array([])
for num in range(10):
    s = 0
    DECK = 1000
    for i in range(DECK):
        s += card_sim(num + 1, 1000000)
    print("-------------")
    print(s/DECK)
    result = np.append(result, s / DECK)
    np.savetxt('result_error.txt', result)
    print("-------------")
