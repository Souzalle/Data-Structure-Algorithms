"""

QUICKSORT -- Dividir e conquistar


Complexidade Temporal
    Melhor do casos: N log N
    Pior  dos casos: N²

Complexidade Espacial:
    - Melhor: log n
    - Pior: N 

"""


def quicksort(nums):
    if len(nums) <= 1: # verificar se a lista tem mais de 1 elemento para ser ordenado, caso contrario n é necessário ordenar
        return nums

    pivot = nums[len(nums) // 2] # escolhendo o pivot, valor central

    menores = [x for x in nums if x < pivot] # Para cada x em nums, verifique se x é menor que o pivô; se for, x entra na lista.
    iguais  = [x for x in nums if x == pivot]
    maiores = [x for x in nums if x > pivot]

    return quicksort(menores) + iguais + quicksort(maiores)

 

