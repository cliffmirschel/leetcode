# Optimized Solution

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for num in nums[:]:
            if num is val:
                # Remove element
                nums.remove(num)
            else:
                count +=1
        


        return count

def remove_element(nums: list[int], val:int):
    while val in nums:
        nums.remove(val)
     
