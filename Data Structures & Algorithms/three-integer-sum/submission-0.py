class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1 # why l i+1 ?
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l<r:
                if nums[l]+nums[r] + num > 0:
                    r -=1
                elif nums[l]+nums[r] + num< 0:
                    l+=1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
                    
                    

                    

        