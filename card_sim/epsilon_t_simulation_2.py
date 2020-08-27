import random
import itertools
import pandas as pd
import numpy as np


# The card simulation function. The input t stands for the number of times 
# swapping the cards. Error e should fall in the open interval (0,1)
def card_sim(n, pofs, t, e):
    p_map, p = make_map(n)
    # each number in cards stands for a card
    cards = list(range(1, n+1))
    
    # Swap cards for t times
    counter = 0
    while counter < t and check_relative(p_map, p, counter, e) != True:
        r = random.randint(0, n-1)
        q = random.randint(0, n-1)
        prob = random.random()
        # Swap one card and the one after it
        if prob < pofs:
            while r == q:
                q = random.randint(0, n-1)
            cards[r], cards[q] = cards[q], cards[r]
        update(p_map, cards)
        counter += 1
    # print the observations of each simulation for all the buckets
    '''
    for x in p:
        print(x, " ", p_map[list2string(x)])
    '''
    return counter
    

# The following function makes a dictionary that contains all the permutations 
# starting with 1, assigns 0 to each key in the dictionary. 
# The input n is the number of cards
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
            p_map[list2string(temp)] = 0
    return p_map, p


# The following function turns a list of numbers into a string with space 
# in between each number
# The input a_list is a list of numbers
def list2string(a_list):
    s = ""
    for x in range(len(a_list)):
        s = s + str(a_list[x])
        if x != (len(a_list) - 1):
            s = s + " "
    return s


# The following function checks whether uniform distribution has been reached.
# m stands for the dictionary (hashmap), p stands for the list of permutations
# that are keys in the hashmap
def check_relative(m, p, counter, e):
    num_permutations = len(p)
    for x in p:
        if counter == 0:
            return False
        if m[list2string(x)] < (1-e) * counter / num_permutations or m[list2string(x)] > (1+e) * counter / num_permutations:
            return False
    return True


# The following function takes in a map m and the current card configuration 
# cards, and adds 1 to value of the corresponding key
def update(m, cards):
    i = cards.index(1)
    # The current configuration of the cards
    configuration = []
    for j in range(i, len(cards)):
        configuration.append(cards[j])
    for k in range(0, i):
        configuration.append(cards[k])
    m[list2string(configuration)] += 1

result = []

# error goes from 0.1 to 0.01, step length = -0.01
error = 0.1
while error >= 0.01:
    s = 0
    for j in range(1000):
        s += card_sim(4, 0.5, 1000000, error)
    s = s/1000
    result.append([n, 0.5, error, s, (error**2)*s])
    error -= 0.01
for item in result:
    print("When error is ", item[0], ", the mean steps to fully randomize is ", item[1])
    print(item[2])
'''
# Create Pandas dataframe for the data we collected
data = pd.DataFrame(np.array(result), columns=['e', 'avg_steps', 'e^2 * avg_steps'])

# Write csv file
data.to_csv('epsilon_t1.csv', index=False)

print(data)
'''