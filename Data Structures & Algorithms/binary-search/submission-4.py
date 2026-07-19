import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) -1
        while l <=r:
            m = (l+r)//2
            check_num = nums[m]
            if check_num > target:
                r = m-1
            elif check_num < target:
                l = m+1
            elif check_num == target:
                return m
        return -1








            

