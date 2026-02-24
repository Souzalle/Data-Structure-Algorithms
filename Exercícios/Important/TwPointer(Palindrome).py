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
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
        return True
