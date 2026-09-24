"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
strs = ["flower","flow","flight"]
class Solution:
    def longestCommonPrefix(slef, strs: list[str]) -> str:
        result = []
        comparative = list(strs[0])
        print(comparative)
        for word in strs:
            for idx, letter in enumerate(word): ## estou querendo comparar letra a letra, deixei uma variavel com uma palavra para base de comparação
                if letter == comparative[idx]:
                    result.append(letter)

        return result
        

print(Solution().longestCommonPrefix(strs))

## guardar letras da primeira palavra, e nas proximas comparar com a guardada, se achar mantem a letra la se n achar remover do array as letras n encontrada
