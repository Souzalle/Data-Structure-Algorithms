class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {} # criando dicionario vazio

        for idx, ch in enumerate(s):  # enumerate(s) percorre a string retornando pares (índice, caractere)
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] +=1
        
        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
        
        return -1
    

# OUTRA FORMA DE RSOLVER


from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = Counter(s)

        for i,ch in enumerate(s):

            if(freq[ch] == 1):
                return i
            
        return -1