"""

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_number = str(x)
        result = False
        right = 0
        left = len(string_number) - 1
        
        while right <= left:
            if len(string_number) == 1:
                result = True
                break
            elif string_number[right] == string_number[left]: 
                right+=1
                left-=1
                result = True
            else:
                result = False
                break
                  
        return result
            

print(Solution().isPalindrome(121))