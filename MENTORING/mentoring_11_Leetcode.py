"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

"""
s = "()"
class Solution:
    def isValid(self, s: str) -> bool:
        hash = {"(":")", "[":"]", "{":"}"} # quero usar o hash pra saber os pares, achar o inicio da string e usar os pares pra fechar
                                           # posso usar .pop() olhar começo e fim da string e ver se os pares batem, ou usar ponteiros






print(Solution().isValid(s))