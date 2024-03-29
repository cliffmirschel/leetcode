# First attempt, beats 97% of solutions 
def count_subarrays(nums: list[int], k:int):
    mx = max(nums)
    ans = cnt_mx = left = 0
    for x in nums:
        if x == mx:
            cnt_mx += 1
        while cnt_mx == k:
            if nums[left] == mx:
                cnt_mx -= 1
            left += 1
        ans += left
    return ans