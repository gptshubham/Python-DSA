# check if a given element k is present in a list L or not --> obvious_search
def obvious_search(L, k):
    '''check if a given element k
    is present in the list L or not.
    This function was authored by SK Gupta'''
    for x in L:
        if x == k:
            return True
    return False


# L = list(range(100))
# print(obvious_search(L, 200))

# Example demonstrating use of time module
'''
import time
# function for sum of first n natural numbers
def sum(n):
    ans = 0
    for i in range(n):
        ans += (i + 1)
    return ans


start = time.time(); print(sum(10000000)); end = time.time(); print(end - start)

# multiple print statements in a single line --> ";"
print('First Command');print('Second Command');print(sum(100));print('Last One')

# help(time.time)

help(obvious_search)
'''

