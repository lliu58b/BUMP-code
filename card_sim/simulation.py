import random
import itertools


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
    print(p)
    print(len(p))
    print(p_map)
    print()
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


# The card simulation function. The input t stands for the number of times 
# swapping the cards. 
def card_sim(n, t):
    p_map, p = make_map(n)
    # each number in cards stands for a card
    cards = list(range(1, n+1))
    
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
        print(x, " ", p_map[list2string(x)])
    


# The following function checks whether uniform distribution has been reached.
# m stands for the dictionary (hashmap), p stands for the list of permutations
# that are keys in the hashmap
def check_relative(m, p, counter):
    num_permutations = len(p)
    for x in p:
        if counter == 0:
            return False
        if m[list2string(x)] < 0.95 * counter / num_permutations or m[list2string(x)] > 1.05 * counter / num_permutations:
            return False
    print(counter)
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


card_sim(4, 100000)















