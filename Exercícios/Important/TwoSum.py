"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {} # cria o dicionário

        for idx, i in enumerate(nums): # para cada index e valor em NUMS ( o enumerate pega todo o valor do array e separa em index e valor)
            if hasher.get(i) is not None: #Verifica se o valor de i ja esta no hashmap, se sim continua pro return, se n ele sai do IF
                return [hasher.get(i), idx] # returna o valor e o index atual
            hasher[target-i] = idx 
        

