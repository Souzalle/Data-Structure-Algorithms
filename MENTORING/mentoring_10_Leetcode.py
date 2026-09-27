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
strs = ["ab", "a"]
class Solution:
    def longestCommonPrefix(slef, strs: list[str]) -> str:
        result = []
        comparative = strs[0]    
        for idx, letter in enumerate(comparative):
            for word in strs:
                if idx >= len(word):
                    return "".join(result)
                if word[idx] != letter:
                    return "".join(result)
            
            result.append(letter)  
        return "".join(result)

print(Solution().longestCommonPrefix(strs))
