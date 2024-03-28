from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        start, l, d = 0, 0, defaultdict(int)

        for i in range(len(nums)):
            l = max(l, i - start)
            d[nums[i]] += 1
            while d[nums[i]] > k:
                d[nums[start]] -= 1
                start += 1

        return max(l, len(nums) - start)