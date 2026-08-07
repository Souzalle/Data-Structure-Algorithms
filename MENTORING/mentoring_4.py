"""

1 - conversor de celsius para fahrenheit
2 - calcular fatorial
3 - criar um vetor(arry) tamanho qualquer e preencher ele com valores aleatorios 
    -- depois retornar o vetor invertido
4 - gerar um vetor aleatorio, depois percorrer o vetor e gerar como saída um vetor apenas com os numeros primos do primeiro vetor, e como resultado a soma de todos os primos desse vetor

"""
## CELSIUS ---------------------------------------------------------------------------------------

celsius = float(input("Digite o valor em celsius: "))
fahr = (celsius * 1.8) + 32
print(f'{fahr:g}')

## -----------------------------------------------------------------------------------------------


## FATORAR ---------------------------------------------------------------------------------------
num_fatorar = int(input("Digite o número a ser fatorado: "))
while num_fatorar < 0:
    print('Números negativos não podem ser fatorados!')
    num_fatorar = int(input("Digite o numero a ser fatorado: "))


if num_fatorar == 0:  #--------| 
    print(1)          #        |
elif num_fatorar == 1:#        ## é possível remover o if e o elif, e deixar somente o FOR, ele ja cobre essas situações
    print(1)          #        | 
else:                 #--------|
    fatorado = 1
    for i in range(1,num_fatorar+1):
        fatorado = fatorado * i

    print(f'Fatorial é igual: {fatorado}')

## ----------------------------------------------------------------------------------------------


## ARRAY ALEATÓRIO e INVERTER  

import random

array = []
for _ in range(5):
    array = random.randint(1,10)
print(array)



result = []
for i,item in reversed(enumerate(array)):
    result.append(item)
print(result)





## ----------------------------------------------------------------------------------------------

## VETOR ALEATORIO -> APENAS PRIMOS -> SOMA DOS PRIMOS

import random

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

array = []
for _ in range(5):
    array.append(random.randint(1,10))
print(array)

for i in array:
    if prim(i) == False:
        array.remove(i)

print(array)

soma = 0

for i in array:
    soma = soma + i

print(soma)

