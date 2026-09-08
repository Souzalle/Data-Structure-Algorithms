'''
Given an array of integers A and an integer number X, 
find all pairs of indexes (i, j), i < j, such that A[i] * A[j] == X.

o(n²)

import random

X = 81

pairs = []
A = [1,2,3,4,6,9,12,9]

 
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] * A[j] == X:
            pairs.append((i, j))

print(pairs)



TENTAR RESOLVER O MESMO EXERCICIO DE FORMA LINEAR

tentativa 1: pra cada valor eu checo se o meu X dividido pelo meu i da o resultado 0, se sim os numeros se multiplicam e eu salvo os dois.
tentativa 2:  pego meu valor atual e vejo qual numero q preciso pra multiplicar por ele e dar X, se esse valor existir eu passo verificando se ele existe no array.

'''
X = 36
A = [1,2,3,4,6,9,12,36]


def find_pairs(A, X):
    result = []
    for idx, valor in enumerate(A): 
        search = X / valor
        if search in A and search > valor:
            result.append((idx, A.index(search)))

    return result 

print(find_pairs(A, X))


