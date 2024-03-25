from collections import Counter
# First attempt -> Passed

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = {}
        res = []

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen[num] = True
        
        return res

# Optimzed solution
    
def find_duplicates(nums: list):
    c = Counter(nums)
    return [k for k, v in c.items() if v > 1]

print(find_duplicates([4,3,2,7,8,2,3,1]))