"""

713. Subarray Product Less Than K
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106


"""
import math

# First attempt, brute force approach -> Too slow

def sub_less_than_k(nums: list[int], k: int):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if math.prod(nums[i:j + 1]) < k:
                count += 1
    
    return count

# Optimzed solution, sliding window

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = 0
        l,product = 0,1

        for r,num in enumerate(nums):
            product *=num
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans

print(sub_less_than_k([10,5,2,6],100))

print(sub_less_than_k([1,2,3],0))