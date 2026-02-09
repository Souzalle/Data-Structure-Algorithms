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
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    menores = [x for x in nums if x < pivot]
    iguais  = [x for x in nums if x == pivot]
    maiores = [x for x in nums if x > pivot]

    return quicksort(menores) + iguais + quicksort(maiores)

 

