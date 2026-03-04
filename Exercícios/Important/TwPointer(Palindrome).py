"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 # ponteiro esquerda
        r = len(s) - 1 # ponteiro direita

        while l < r: # enqt os ponteiros nao se encontrarem
            if not s[l].isalnum(): # se o ponteiro nao apontar para um caracter alfa numerico, ele pula uma casa pra frente
                l+=1 # adiciona 1, anda uma pra frente
            elif not s[r].isalnum(): # se o ponteiro nao apontar para um caracter alfa numerico, ele volta uma casa(ja q esse ponteiro esta vindo do final)
                r-=1 # remove 1, volto uma para tras
            elif s[l].lower() == s[r].lower(): # verifico se a letra no ponteiro da esquerda e direita sao iguals( como é um palindromo ela DEVE ser)
                l+=1 # apos verificado ando uma casa para frente
                r-=1 # apos vertificado ando uma para tras
            else:
                return False # se n foram iguais ja me retorna falso, nao é uum palindromo
        
        return True # se o while nao retornar falso, logo é um palindromo
