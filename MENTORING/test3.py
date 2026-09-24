hash = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

s = "XIV"
result = 0

for idx, letter in enumerate(s):
    atual = hash[letter]
    if idx + 1 < len(s) and atual < hash[s[idx + 1]]:
        result =  result - atual
    else:
        result = result + atual


print(result)