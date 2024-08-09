# check if a given element k is present in a list L or not --> obvious_search
def obvious_search(L, k):
    """check if a given element k
    is present in the list L or not.
    This function was authored by SK Gupta"""
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


# Program: Write a Program that can search for a given element in the given list L
# faster than the obvious search algorithm
def binary_search(L,k):
    """This function is an alternative for the obvious search
    It does exactly what is expected from the obvious_search,
    but in an efficient way. This method is popularly called
    the binary_search."""
    begin = 0
    end = len(L) - 1

    # using the while loop to look up the list and keep halving it
    while (end - begin) > 1:
        # computing the mid which is the mid-point of begin to end
        mid = (begin + end) // 2
        # if mid is indeed k, then we return True and stop the code
        if L[mid] == k:
            return 1
        # If The middle element is greater than k, then cut the right side and
        # retain the left side
        if L[mid] > k:
            end = mid - 1

        # if the middle element is less than k, then cut the left side and
        # retain the right side
        if L[mid] < k:
            begin = mid + 1
    # This is outside the while loop. If we are here, it means that we haven't
    # found the element. Also, if we are here , it means that the while condition
    # is violated. Which means (end - begin) <= 1

    # If it is equal to 1, there is exactly two element
    if L[begin] == k or L[end] == k:
        return 1
    else:
        return 0


# Binary Search using Recursion
def rbinary_search(L, k, begin, end):
    """This function will recursively execute binary search"""
    # if begin and end are same, then just check if L[begin] is equal to k
    if begin == end:
        if L[begin] == k:
            return 1
        else:
            return 0
    # if begin and end are consecutive, then check them individually
    if (end - begin) == 1:
        if L[begin] == k or L[end] == k:
            return 1
        else:
            return 0
    # if (end - begin) > 1
    if (end - begin) > 1:
        # compute the middle element
        mid = (end + begin) // 2
        # if L[mid] is indeed equal to k
        if L[mid] == k:
            return 1
        if L[mid] > k:
            # discard the right and retain the left
            end = mid - 1
        if L[mid] < k:
            # discard the left and retain the right
            begin = mid + 1
    if (end - begin) < 0:
        return 0
    return rbinary_search(L, k, begin, end)
