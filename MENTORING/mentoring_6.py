'''

Given an array of integers A and an integer number X, 
find all pairs of indexes (i, j), i < j, such that A[i] * A[j] == X.

o(n²)

'''

import random

X = 81

pairs = []
A = [1,2,3,4,6,9,12,9]

 
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] * A[j] == X:
            pairs.append((i, j))

print(pairs)


