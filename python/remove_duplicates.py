# First attempt -> Passed

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen[num] = True
        
        return res