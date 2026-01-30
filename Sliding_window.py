from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = Counter()
        n = len(s)
        left = 0
        res = 0
        for right in range(n):
            count[s[right]] += 1
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
    

"""
count = Counter()  # Dicionário para contar frequência de caracteres
n = len(s)         # Tamanho da string
left = 0           # Ponteiro esquerdo da janela deslizante
res = 0            # Resultado (comprimento máximo encontrado)

for right in range(n):
    count[s[right]] += 1  # Adiciona o caractere da direita ao contador

    while count[s[right]] > 2:  # Se algum caractere aparece mais de 2 vezes
        count[s[left]] -= 1      # Remove o caractere da esquerda
        left += 1                # Move o ponteiro esquerdo para a direita

    res = max(res, right - left + 1)  # Atualiza o comprimento máximo


"""