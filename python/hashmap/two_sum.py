# Optimized Solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in cache:

                return [cache[complement], i]
            
            cache[num] = i

        return []