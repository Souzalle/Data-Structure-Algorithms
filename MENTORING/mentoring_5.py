"""

Algoritmo de ordenação




array = [2, 4, 5, 2, 3]

print(array)

array[2], array[3] = array[3], array[2] ## swap de valores dentro de array

print(array)

print(array[0])


Dado um array X

enquanto xxx:

para cada index, verificar se o valor do item é maior que o seu proximo

se for maior, inverter os dois valores

mostro o array

 o(n²)
"""
import random

array = []
for _ in range(10):
    array.append(random.randint(1,30))

is_sorted = False

print(array)

while is_sorted == False:
    is_sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            is_sorted = False

print(array)