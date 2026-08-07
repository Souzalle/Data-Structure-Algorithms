import random

array = []
for _ in range(5):
    array.append(random.randint(1,10))
print(array)


result = []
for i,item in enumerate(reversed(array)):
    result.append(item)
print(result)


## ------------------------------------------------------------------------
result2 = []
array_len = len(array)-1
while array_len >= 0:
    result2.append(array[array_len])
    array_len = array_len -1
print(result2)
