## Fila e Pilha

'''
## Palindrome 

ARARA

## is input empty or null
## is input size 1
## is input size 2 and equal
## insert chars into the deque

[A, R, A, R, A]
 0  1  2  3  4  -  BigO(n/2)


ARARA

RemoveFromhead == RemoveFromTail
RemoveFromhead == RemoveFromTail



palindrome example: 'Roma é amor'

'''
from collections import deque
import re

s = input('Digite: ')
s = s.replace(' ','').lower()
p = deque(s)

##regex = re.sub(r'[^a-zA-Z0-9]+','', s) ## trata problemas de caracteres especiais
##print(regex)

if not p:
    print('empty')

elif len(p) == 1:
    print(f'{s} is a palindrome')

elif len(p) == 2:
    if p[0] == p[1]:
        print(f"Word {s} is a palindrome")
    else:
        print(f"Word {s} is NOT a palindrome")

else:   
    print(p)
    while len(p) > 1:
        if not p.pop() == p.popleft():
            print('Its not a palindrome')
            break
    else:
        print('Its a palindrome')







    
