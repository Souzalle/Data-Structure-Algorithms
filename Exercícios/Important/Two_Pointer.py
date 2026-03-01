
'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ") # pego a string dada salva em S e divido ela a cada espaço vazio, e salvo em words separadamente por virgula
        invWord = [] # crio um array vazio

        for word in words: # para cada word dentro do array words rodo o codigo
            inv = word[::-1] # Inv recebe a palavra em word e inverte ela com o comando[::-1]
            invWord.append(inv) # invWord recebe a variavel inv

        res = " ".join(invWord) # res receve tudo dentro de invword, porem com metodo (" ".join) ele vai adicionar um espaço entre cada palavra e atribuir ao res 

        return res # retorna meu res
    
"""OUTRA SOLUÇÃO """

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i, word in enumerate(words):
            words[i] = word[::-1]

        return " ".join(words)