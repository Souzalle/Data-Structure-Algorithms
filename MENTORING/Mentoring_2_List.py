"""
LISTA


Estudar --

Exercicio: Algoritmo que verifique quantas vezes um carácter aparece em uma string.

"""
from collections import Counter

s = list(input('Digite: ').lower())

check = {}

for i in s:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1       

print(check)


    
## Posso usar o 'Counter' par fazer isso de forma rapida
##    -----   print(Counter(s)) -------


