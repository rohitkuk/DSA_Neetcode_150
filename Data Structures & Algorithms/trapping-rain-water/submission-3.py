class Solution:
    def trap(self, height: List[int]) -> int:

        # The below is still a valid solution but without 2 pointer and memory of N

        # lmax = 0
        # left_maxes = [0] * len(height)
        # for i in range(len(height)):
        #     left_maxes[i] = lmax
        #     lmax = max(height[i], lmax)

        # rmax = 0
        # right_maxes = [0] * len(height)
        # for i in range(len(height)-1, -1, -1):
        #     right_maxes[i] = rmax
        #     rmax = max(height[i], rmax)
        # water = 0 
        # for i in range(len(height)):
        #     water+= max(0, min(left_maxes[i], right_maxes[i]) - height[i])
        # return water

        # O(1) memory solution

        lmax = 0
        rmax = 0
        l,r = 0, len(height)-1
        water = 0
        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                water += rmax - height[r]
                r-=1
        return water
                

