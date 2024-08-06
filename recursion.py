# sum of first n numbers natural numbers

# The naive way
'''
n = int(input("Enter a Number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
'''

# sum function

'''
def sum(n):
    ans = 0
    for i in range(1,n+1):
        ans += i
    return ans


print(sum(10))
'''

# recursion in python

'''
def sum_r(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


print(sum_r(10))
'''

# compute compound interest assuming the interest to be 10%

'''
def compound_interest(p, n):
    if n == 1:
        return (p * 1.1) - p
    else:
        amount = p * 1.1
        return (amount - p) + compound_interest(amount, n - 1)


print(compound_interest(2000,3))
'''

# compute the amount after n years assuming
# a compound interest rate of 10%

'''
def total_amount(p, n):
    if n == 1:
        return (p * 1.1)
    else:
        return total_amount(p, n - 1) * 1.1


print(total_amount(2000,3))
'''

# factorial using recursion

'''
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
    
n = int(input('Enter a number: '))
print(fact(n))
'''

# zero check in a list using recursion

'''
def check_zero(l):
    # if the list is empty return False
    if not l:
        # print("Empty")
        return False
    # if list is not empty
    if l[0] == 0:
        # if the first element is zero then return True
        return True
    else:
        # if first element in not zero then return rest of the list
        # print(l)
        return check_zero(l[1:])


l = [11, 12, 16, 2, 3, 4, 5, 6]
print(check_zero(l))
'''

# Sorting Recursively


def min_element(l):
    """finds the minimum element in the list"""
    min_value = l[0]
    for element in l:
        if min_value > element:
            min_value = element
    # print(min_value)
    return min_value


def sort_r(l):
    """sort the list recursively"""
    if l == [] or len(l) == 1:
        return l
    min_value = min_element(l)
    # print(l)
    l.remove(min_value)
    return [min_value] + sort_r(l)


l = [5, 6, 59, 19, 2, 1, 3, 6, 3, 1, 5]
print(sort_r(l))
