"""
Hasmap/dicttonary -  conceitos
	- Conceito colisão de hash(como,quando)
    - Implementação hash

ALGORITMO
    1 -  Verificar se um número é primo.
    2 -  após dado a posição, retornal qual o numero primo referente. 

"""

## n = int(input("Digite: "))

def prim(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False 

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

p = int(input("Digite a posição: "))
r = 0
s = 2
val = 0
while r < p:
    if prim(s) == True:
        r +=1
        val = s
        s +=1
    else:
        s +=1

print(val)

### alterar as variavais pra ficar mais legivel

## 1 melhorar legibilidade e mantenabilidade do codigo










