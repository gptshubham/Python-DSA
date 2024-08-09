import search
import time

# help(search.obvious_search)
# help(search.binary_search)

# L = [12, 15, 100, 121, 1001, 1024, 2016, 2021]

# print(search.binary_search(L,151))
# print(search.binary_search(L,1024))
# print(search.binary_search(L,2021))
# print(search.binary_search(L,2024))

# L = list(range(1000*1000*100))

# a = time.time(); print(search.obvious_search(L,-1)); b = time.time()
# print(f'Time taken by Obvious Search: {b - a}')
# a = time.time(); print(search.binary_search(L,-1)); b = time.time(); print(b - a)
# print(f'Time taken by Binary Search: {b - a}')

# k = L[len(L) - 1]

# a = time.time(); print(search.obvious_search(L, k)); b = time.time()
# print(f'Time taken by Obvious Search: {b - a}')

# a = time.time(); print(search.binary_search(L, k)); b = time.time()
# print(f'Time taken by Binary Search: {b - a}')

L = [1, 7, 10, 16, 100, 108, 1008]
k = 7
begin = 0
end = len(L) - 1
result = search.rbinary_search(L, k, begin, end)
print(result)

L = [1, 7, 10, 16, 100, 108, 1008]
k = -1
begin = 0
end = len(L) - 1
result = search.rbinary_search(L, k, begin, end)
print(result)

L = list(range(1000*1000*100))
k = 1000000
begin = 0
end = len(L) - 1
result = search.rbinary_search(L, k, begin, end)
print(result)
