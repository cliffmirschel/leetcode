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